# self-hosted-runners-arc

Configuration for Actions Runner Controller: a kind cluster config, scale set Helm values and a job that targets the runners.

## Goal

Show how self-hosted runners scale from zero on Kubernetes using the runner scale set chart.

## Run it

```
python3 self-hosted-runners-arc/validate.py
```
Expected: `ok` lines for `job.yml` (workflow), `kind-config.yml` (config) and `runner-scale-set-values.yml` (config).

Not run end to end: no kind cluster was created and ARC was not installed. The values point at the repository `adrianrevilla009/orders` and need a GitHub App you create yourself. The validator only parses the files and checks scale bounds and the secret reference.

## What it proves

- `runner-scale-set-values.yml` sets `minRunners: 0` and `maxRunners: 3`, so no runner pods exist while idle and at most three run together.
- `githubConfigSecret` is only a Secret name (`arc-github-app`) created outside git; the validator fails if it is not a string, so credentials are never inline.
- `job.yml` uses `runs-on: arc-runner-set`, which must match the Helm release name, and `kind-config.yml` defines a one-node local cluster.

## Trade-offs

- `containerMode: dind` runs privileged containers, which is a security risk on shared clusters.
- Scale-from-zero adds a cold start to each job.
- You operate the cluster, upgrades and runner image yourself; the values pin runner image 2.321.0 but the chart version must be pinned at install time.

## When not to use it

- For public repositories or light workloads, GitHub-hosted runners avoid the operational cost.
