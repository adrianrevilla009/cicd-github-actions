# caching

A workflow, `cache.yml`, that caches the Maven local repository with `actions/cache`.

## Goal

Show a content-addressed cache key with a fallback, and how to see whether the cache was hit.

## Run it

```
python3 caching/validate.py
```
Expected: `ok   cache.yml (workflow)`.

Not run end to end: cache behaviour only exists on a GitHub runner. The validator checks the key expression and the presence of `restore-keys`, not actual hits.

## What it proves

- The key `m2-${{ runner.os }}-${{ hashFiles('**/pom.xml') }}` changes whenever any POM changes; the validator fails if `hashFiles` is missing.
- `restore-keys` falls back to the newest cache with the `m2-<os>-` prefix, so a changed POM still starts from a mostly warm cache; the validator also requires it.
- The last step prints `steps.m2.outputs.cache-hit`, which is `true` only on an exact key match.

## Trade-offs

- Prefix restores accumulate stale dependencies, so the cache grows until eviction.
- Caches are scoped by branch: a pull request can read the base branch's cache but not other pull requests' caches.
- `setup-java` with `cache: maven` does the same in one line; this folder spells it out to show the mechanics.

## When not to use it

- For small builds with few dependencies the restore and save time can exceed the download time.
