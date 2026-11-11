#!/usr/bin/env python3
"""Aggregate findings for the Big Ten jobs case study. Reads the jobs database, prints JSON.

    python3 tools/big_ten_findings.py ~/um-careers-data/um_careers.db > big_ten_findings.json

Against the live database on the host, from the laptop (host.sh is in ec2-apps):

    B64=$(base64 < tools/big_ten_findings.py | tr -d '\n')
    /path/to/ec2-apps/scripts/host.sh "echo $B64 | base64 -d | python3 - /data/apps/big-ten-jobs-data/um_careers.db" > big_ten_findings.json

Read-only (opens the file with mode=ro). Output is counts and medians by school only: no job titles,
descriptions or URLs, and nothing from the personal feed table. Standard library only.

What it reports
  overview      rows, active postings and the date range seen, per school
  weekly_new    postings first seen per ISO week, per school (each school's first crawl day is left out,
                because that day is the backlog, not new postings)
  days_open     for postings that have closed: quartiles of last_seen - first_seen, per school
                (same first-day exclusion; still-open postings are not counted, so this understates
                long-running ones)
  salary        share of active postings with a parsed salary, and the median midpoint, per school and kind
  work_mode     Michigan only: active postings by mode of work
  gaps          per school, dates between its first and last crawl on which no posting was first seen
                or last seen (most likely a missed crawl; a quiet day at a small school looks the same)
"""
import json
import sqlite3
import statistics
import sys
from collections import defaultdict
from datetime import date, timedelta


def quartiles(xs):
    xs = sorted(xs)
    if not xs:
        return None
    if len(xs) < 4:
        return {"n": len(xs), "median": statistics.median(xs)}
    q1, q2, q3 = statistics.quantiles(xs, n=4)
    return {"n": len(xs), "p25": round(q1, 1), "median": round(q2, 1), "p75": round(q3, 1)}


def main(path):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    q = lambda sql, *a: con.execute(sql, a).fetchall()
    out = {"generated": date.today().isoformat()}

    first_day = {r["school_id"]: r["d"] for r in q("SELECT school_id, MIN(first_seen) d FROM jobs GROUP BY school_id")}

    out["overview"] = [dict(r) for r in q(
        """SELECT school_id, COUNT(*) AS postings, SUM(active) AS active,
                  MIN(first_seen) AS first_seen, MAX(last_seen) AS last_seen
           FROM jobs GROUP BY school_id ORDER BY postings DESC""")]

    weekly = defaultdict(dict)
    for r in q("""SELECT school_id, strftime('%G-W%V', first_seen) AS wk, first_seen, COUNT(*) AS n
                  FROM jobs WHERE first_seen IS NOT NULL GROUP BY school_id, first_seen"""):
        if r["first_seen"] == first_day[r["school_id"]]:
            continue
        weekly[r["school_id"]][r["wk"]] = weekly[r["school_id"]].get(r["wk"], 0) + r["n"]
    out["weekly_new"] = {s: dict(sorted(w.items())) for s, w in sorted(weekly.items())}

    open_days = defaultdict(list)
    for r in q("""SELECT school_id, first_seen, julianday(last_seen) - julianday(first_seen) AS d
                  FROM jobs WHERE active = 0 AND first_seen IS NOT NULL AND last_seen IS NOT NULL"""):
        if r["first_seen"] != first_day[r["school_id"]] and r["d"] is not None and r["d"] >= 0:
            open_days[r["school_id"]].append(r["d"])
    out["days_open"] = {s: quartiles(v) for s, v in sorted(open_days.items())}

    sal = {}
    for r in q("SELECT school_id, COUNT(*) n, SUM(salary_min IS NOT NULL) w FROM jobs WHERE active = 1 GROUP BY school_id"):
        sal[r["school_id"]] = {"active": r["n"], "with_salary": r["w"],
                               "coverage_pct": round(100 * r["w"] / r["n"], 1) if r["n"] else None}
    mids = defaultdict(list)
    for r in q("""SELECT school_id, salary_kind, (salary_min + COALESCE(salary_max, salary_min)) / 2.0 AS mid
                  FROM jobs WHERE active = 1 AND salary_min IS NOT NULL AND salary_kind IS NOT NULL"""):
        mids[(r["school_id"], r["salary_kind"])].append(r["mid"])
    for (school, kind), v in sorted(mids.items()):
        sal[school][f"median_{kind}"] = round(statistics.median(v), 2)
        sal[school][f"n_{kind}"] = len(v)
    out["salary"] = sal

    out["work_mode"] = [dict(r) for r in q(
        """SELECT COALESCE(NULLIF(TRIM(modes_of_work), ''), '(not stated)') AS mode, COUNT(*) AS n
           FROM jobs WHERE school_id = 'umich' AND active = 1 GROUP BY 1 ORDER BY n DESC""")]

    gaps = {}
    for school in first_day:
        seen = set()
        for col in ("first_seen", "last_seen"):
            seen |= {r[0] for r in q(f"SELECT DISTINCT {col} FROM jobs WHERE school_id = ? AND {col} IS NOT NULL", school)}
        if not seen:
            continue
        d, end, missing = date.fromisoformat(min(seen)[:10]), date.fromisoformat(max(seen)[:10]), []
        while d <= end:
            if d.isoformat() not in {s[:10] for s in seen}:
                missing.append(d.isoformat())
            d += timedelta(days=1)
        gaps[school] = {"days_with_no_activity": len(missing), "longest_run": _longest_run(missing),
                        "dates": missing if len(missing) <= 15 else missing[:15] + ["..."]}
    out["gaps"] = gaps

    json.dump(out, sys.stdout, separators=(',', ':'))  # compact: SSM truncates output at 24,000 characters
    print()


def _longest_run(dates):
    best = run = 0
    prev = None
    for s in dates:
        d = date.fromisoformat(s)
        run = run + 1 if prev and (d - prev).days == 1 else 1
        best, prev = max(best, run), d
    return best


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
