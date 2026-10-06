# build-test-matrix

A GitHub Actions workflow, `ci.yml`, that runs a Maven build across an OS and Java version matrix.

## Goal

Show how a build matrix covers several operating systems and JDKs with one job definition, including an allowed-to-fail experimental leg.

## Run it

```
python3 build-test-matrix/validate.py
```
Expected: `matrix expands to 3 jobs` and `ok   ci.yml (workflow)`.

Not run end to end: the workflow needs GitHub-hosted runners and a Maven project. `validate.py` only parses the YAML, checks that a trigger exists and counts the expanded matrix.

## What it proves

- `matrix` crosses `os` (ubuntu-24.04, windows-2022) with `java` (17, 21); the `exclude` entry drops windows-2022 with Java 17, so the validator counts 3 jobs.
- `include` adds `experimental: true` to the ubuntu-24.04 / Java 21 leg, and `continue-on-error: ${{ matrix.experimental == true }}` lets only that leg fail without failing the run.
- `fail-fast: false` keeps the other legs running when one breaks, and `setup-java` with `cache: maven` caches the local repository per leg.

## Trade-offs

- More legs multiply runner minutes; Windows runners cost more than Linux ones.
- `include` entries that match an existing combination add keys to it rather than creating a new job, which is easy to misread.
- The workflow assumes a Maven project with a `pom.xml` at the repository root.

## When not to use it

- For a single-target service that ships on one OS and one JDK, a matrix only adds cost.
