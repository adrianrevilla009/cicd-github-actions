# cicd-github-actions

Ten small GitHub Actions patterns for a Maven project, each checked offline so you can see how it is wired in a couple of minutes.

## What is inside

| Folder | What it shows | Run |
| --- | --- | --- |
| [`build-test-matrix`](./build-test-matrix) | OS and Java matrix with `include`, `exclude` and an experimental leg | `python3 build-test-matrix/validate.py` |
| [`reusable-workflows`](./reusable-workflows) | `workflow_call` workflow with inputs, a secret and an output, and its caller | `python3 reusable-workflows/validate.py` |
| [`composite-action`](./composite-action) | Local composite action with an input and an output | `python3 composite-action/validate.py` |
| [`oidc-to-cloud`](./oidc-to-cloud) | Keyless AWS login with GitHub OIDC and a pinned trust policy | `python3 oidc-to-cloud/validate.py` |
| [`caching`](./caching) | Maven cache with a content-hash key and restore fallback | `python3 caching/validate.py` |
| [`environments-approvals`](./environments-approvals) | Staging then production behind an environment, with non-cancelling concurrency | `python3 environments-approvals/validate.py` |
| [`release-please`](./release-please) | Release pull requests and changelog from conventional commits | `python3 release-please/validate.py` |
| [`docker-publish`](./docker-publish) | Image build and push to GHCR on version tags | `python3 docker-publish/validate.py` |
| [`self-hosted-runners-arc`](./self-hosted-runners-arc) | Runner scale set on Kubernetes (kind) scaling from zero | `python3 self-hosted-runners-arc/validate.py` |
| [`monorepo-path-filters`](./monorepo-path-filters) | Per-service jobs gated on changed paths | `python3 monorepo-path-filters/validate.py` |

The examples use a shared Orders domain. Nothing here contacts GitHub or a cloud account: each folder has a `validate.py` that parses its YAML and checks a few key rules, and the workflows themselves have not been run on GitHub.

## Prerequisites

- Python 3 with PyYAML (`pip install pyyaml`) to run the `validate.py` scripts.
- To use the workflows for real: a GitHub repository, a Maven project on Java 21, and for some folders AWS, Docker, or kind and Helm.

## How to read it

Start with `build-test-matrix`, then `reusable-workflows` and `composite-action`. Each folder README says what was checked and what was not run end to end.
