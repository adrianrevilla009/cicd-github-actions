# composite-action

A local composite action, `action.yml`, that sets up JDK 21 and runs a Maven build, plus `use.yml` that calls it.

## Goal

Show how to package several steps into one reusable action with an input and an output, without publishing it.

## Run it

```
python3 composite-action/validate.py
```
Expected: `ok   action.yml (action)` and `ok   use.yml (workflow)`.

Not run end to end: it needs a GitHub runner and a Maven project, so only the YAML shape is validated.

## What it proves

- `action.yml` has `runs.using: composite` with three steps: `setup-java` (Temurin 21, Maven cache), a step that reads the project version into `$GITHUB_OUTPUT`, and a Maven run using the `goals` input (default `verify`).
- Every `run` step sets `shell: bash`, which composite actions require; the validator fails if one does not.
- `use.yml` calls it with `uses: ./composite-action` and prints `steps.orders.outputs.version`, which the action exposes as its `version` output.

## Trade-offs

- A composite action runs inside the caller's job: it cannot declare its own `runs-on` or split work into jobs.
- Logs show the inner steps flat, with less structure than a reusable workflow.
- The JDK version is hard-coded to 21 rather than an input.

## When not to use it

- When you need separate jobs, different runners or secrets handling, use a reusable workflow instead.
