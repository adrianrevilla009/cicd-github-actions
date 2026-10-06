# environments-approvals

A two-stage workflow, `release.yml`, that deploys to `staging` and then to `production` behind an environment.

## Goal

Show how environments gate a deploy so that production waits for a reviewer and two production deploys never overlap.

## Run it

```
python3 environments-approvals/validate.py
```
Expected: `ok   release.yml (workflow)`.

Not run end to end: environments, reviewers and the approval pause are GitHub features and nothing was configured. The validator checks job dependency and concurrency only.

## What it proves

- The `production` job has `needs: staging`, so it only starts after staging succeeds; the validator checks this.
- Both jobs use `environment:`; the comment in the file notes that required reviewers and a main-only branch rule are set in repository Settings, not in YAML.
- The `production` job uses `concurrency: group: production` with `cancel-in-progress: false`, so a queued deploy is never cancelled by a newer one; the validator checks this too.

## Trade-offs

- The approval rules live outside the repository, so the YAML alone does not prove that production is protected.
- Required reviewers on private repositories depend on the GitHub plan.
- Deploy steps are `echo` commands; only the control flow is shown.

## When not to use it

- For a project with a single environment and no approval needs, plain jobs are enough.
