# docker-publish

A workflow, `publish.yml`, that builds a Docker image and pushes it to GitHub Container Registry on version tags.

## Goal

Show an image publish pipeline that uses the built-in token, derives tags from the git tag and reuses build cache.

## Run it

```
python3 docker-publish/validate.py
```
Expected: `ok   publish.yml (workflow)`.

Not run end to end: it needs a tag push, a Dockerfile and GHCR. The validator only checks the YAML and the `packages: write` permission.

## What it proves

- The workflow triggers on tags matching `v*` and logs in to `ghcr.io` with `secrets.GITHUB_TOKEN`, so no registry password is stored.
- The job grants `packages: write` and `contents: read` only; the validator fails if `packages: write` is missing.
- `docker/metadata-action` produces a semver tag and a `sha` tag, and `build-push-action` uses `cache-from` and `cache-to` of `type=gha`.

## Trade-offs

- The build uses `context: .`, so the repository needs a `Dockerfile` at its root; none is included here.
- The GitHub Actions cache has a size limit and is shared with other caches.
- There is no image signing and no vulnerability scan step.

## When not to use it

- For images that go to a private cloud registry, log in there with OIDC instead of using GHCR.
