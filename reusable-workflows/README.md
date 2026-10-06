# reusable-workflows

A reusable workflow, `reusable-build.yml`, and a `caller.yml` that invokes it with inputs and reads its output.

## Goal

Show how a build is defined once with `workflow_call` and reused by other workflows, the pattern shared workflow repositories rely on.

## Run it

```
python3 reusable-workflows/validate.py
```
Expected: `ok   caller.yml (workflow)` and `ok   reusable-build.yml (workflow)`.

Not run end to end: GitHub resolves the `uses:` reference only inside a repository with a `.github/workflows` folder, and the build needs a Maven module named `orders-service`. The validator only checks the YAML shape.

## What it proves

- `reusable-build.yml` declares `workflow_call` with inputs `java-version` (default 21) and `module` (required), an optional `registry-token` secret, and an `artifact` output.
- `caller.yml` job `orders` has `uses:` and no `runs-on`, passes `module: orders-service` and `secrets: inherit`; the validator enforces this shape.
- The `report` job in the caller reads `needs.orders.outputs.artifact`, which the reusable workflow sets to `orders-<module>`.

## Trade-offs

- `caller.yml` points at `./.github/workflows/reusable-build.yml`, so both files must be moved into `.github/workflows/` of a repository to run; here they sit side by side.
- `secrets: inherit` is convenient but passes every secret; naming them explicitly is stricter.
- Reusable workflows cannot change the caller's triggers, and nesting depth is limited.

## When not to use it

- For a build used by one repository and one workflow, a plain job is simpler than a reusable workflow.
