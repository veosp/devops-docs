# Operations

## Publication

1. Confirm that the `pylint` check passed on the pull request.
2. Merge into `main`.
3. Open Actions → Publish documentation.
4. Wait for the `build` and `deploy` jobs to succeed.
5. Open the URL from the `github-pages` environment and check the home page.

## Manual Run

To publish again, open Actions → Publish documentation → Run workflow.

## Diagnosis

Identify the stage that failed: CI, site build, artifact upload, or deployment.
Read the log for that step before retrying.

## Recovery

Review the [incident log](recovery.md) before restoring the site.
