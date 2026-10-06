# oidc-to-cloud

A deploy workflow, `deploy.yml`, that authenticates to AWS with GitHub OIDC, and the IAM trust policy, `trust-policy.yml`, that allows it.

## Goal

Show keyless cloud authentication: the job gets a short-lived token from GitHub and exchanges it for AWS credentials, with no stored access keys.

## Run it

```
python3 oidc-to-cloud/validate.py
```
Expected: `ok   deploy.yml (workflow)` and `ok   trust-policy.yml (config)`.

Not run end to end: it needs a real AWS account, an IAM OIDC provider and a role, and nothing was applied. The validator checks the YAML only.

## What it proves

- `deploy.yml` sets `permissions: id-token: write` and calls `aws-actions/configure-aws-credentials@v4` with a `role-to-assume`; it references no `secrets.` at all, which the validator checks.
- `trust-policy.yml` trusts the GitHub OIDC provider for `sts:AssumeRoleWithWebIdentity` and pins `aud` to `sts.amazonaws.com`.
- The `sub` condition is `repo:adrianrevilla009/orders:environment:production` with no wildcard, so only that repository and environment can assume the role.

## Trade-offs

- The account id `123456789012` in the role and provider ARNs is an example value and must be replaced.
- Pinning to an environment ties deploys to its approval rules, but you must keep the job and the trust policy in step.
- The trust policy is written as YAML for readability; AWS expects JSON.

## When not to use it

- For clouds or registries without OIDC federation, you still need stored credentials.
