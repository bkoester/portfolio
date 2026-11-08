---
title: Self-healing EC2 host
bucket: live
status: todo
visibility: public
repos: [ec2-infra, ec2-apps]
papers: []
next: Delete the committed Terraform plan from ec2-infra and purge it from history
---

# Self-healing EC2 host

A personal cloud that repairs itself: one Terraform-managed Docker host on a Spot instance that survives being
reclaimed, comes back with the same IP and data, and runs seven apps for a few dollars a month.

## The problem

Running several small apps cheaply means Spot instances, and Spot instances disappear on two minutes' notice.
The host has to lose nothing and need no hands when that happens.

## Approach

- **Compute**: t4g.large ARM Spot instance in an auto-scaling group (desired = 1)
- **Storage**: encrypted gp3 volume at `/data`, a standalone resource that re-attaches to every replacement
- **Networking**: Elastic IP re-associated on boot; zero inbound security-group rules; SSM Session Manager only;
  IMDSv2 enforced
- **Resilience**: Spot interruption handler stops containers and flushes writes on the two-minute warning
- **Cost**: scales to zero at midnight Eastern and back at 7am; AWS Budget alerts
- **Backup**: volume snapshots every 12 hours, 7 days retained
- **Monitoring**: CloudWatch Logs and alarms (CPU, disk, boot errors, instance count) with SNS email alerts
- **Two-repo design**: ec2-infra (Terraform, from the laptop) knows nothing about apps; ec2-apps (compose file,
  app manifest, systemd timers) is pulled on every boot
- **AI on the host**: Claude Code through Bedrock via the instance role

## Apps it runs

big-ten-jobs (scraper, feed and explorer), ask-ben (database, API, eval), wcc-pathfinder, a solar dashboard and
Discord bot, a journal dashboard, the workspace project-notes agent, and fantrax. Public apps are exposed
through tunnels, not open ports.

## Results

Open question: real numbers worth stating — monthly cost, Spot replacements survived, time to recover.

## Code

- ec2-infra, ec2-apps (private until cleaned up)

## To resolve

- [ ] Delete terraform/tfplan and purge it from history (plan files can hold resolved values); add it to .gitignore
- [ ] Strip account-specific IDs; keep terraform.tfvars.example as the only config sample
- [ ] Review ec2-apps for secrets
- [ ] Architecture diagram for the case study
- [ ] Consider publishing as a reusable template
