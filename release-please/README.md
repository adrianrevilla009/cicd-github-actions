# release-please

A release-please workflow, `release-please.yml`, with its config and manifest JSON files.

## Goal

Show automated release pull requests and changelogs driven by conventional commits.

## Run it

```
python3 release-please/validate.py
```
Expected: `ok   release-please.yml (workflow)`; the validator also parses both JSON files and fails if either is missing or invalid.

Not run end to end: it needs a real repository with commit history on `main`. The validator only checks the workflow shape and that the JSON parses.

## What it proves

- `release-please.yml` runs `googleapis/release-please-action@v4` on pushes to `main` with `contents: write` and `pull-requests: write`.
- `release-please-config.json` sets a single package `.` with `release-type: maven` and `changelog-path: CHANGELOG.md`.
- `.release-please-manifest.json` records the current version `0.1.0`, which release-please updates in the release pull request.

## Trade-offs

- It depends on conventional commit messages; unstructured history yields no release.
- Releases created with the default `GITHUB_TOKEN` do not trigger other workflows; a personal token or app is needed for that.
- Version bumps in a Maven project touch the POM, so the POM version must match the manifest.

## When not to use it

- For libraries released by hand on an irregular cadence, or teams that will not use conventional commits, it adds friction.
