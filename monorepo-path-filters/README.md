# monorepo-path-filters

A workflow, `services.yml`, that builds only the services whose files changed in a pull request.

## Goal

Show how a monorepo skips unrelated builds by computing changed paths first and gating jobs on the result.

## Run it

```
python3 monorepo-path-filters/validate.py
```
Expected: `ok   services.yml (workflow)`.

Not run end to end: it needs a pull request in a repository with `services/orders` and `services/billing` modules. The validator only checks the YAML and the gating.

## What it proves

- A `changes` job runs `dorny/paths-filter@v3` with filters for `orders` (`services/orders/**`, `libs/common/**`) and `billing` (`services/billing/**`, `libs/common/**`) and exposes them as outputs.
- The `orders` and `billing` jobs both need `changes` and have an `if:` on its output; the validator fails if either is not gated.
- A change under `libs/common/**` triggers both services, and `paths-ignore: ["**.md"]` skips the whole workflow for Markdown-only changes.

## Trade-offs

- Filters are maintained by hand and drift when directories move.
- If a gated job is a required status check, a skipped job can block merging unless the branch rules account for it.
- The `mvn -pl ... -am` commands assume a multi-module Maven build with those module paths.

## When not to use it

- For a small repository where a full build takes a minute or two, filtering adds complexity for little saving.
