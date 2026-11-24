# Incident Log

| Incident | Symptom | First place to check |
|---|---|---|
| Unused variable | The `pylint` check fails on the pull request | Static analysis log |
| Insufficient deployment permissions | `build` succeeds and `deploy` cannot obtain an OIDC token | `deploy-pages` log and workflow `permissions` |
| Broken link | `mkdocs build --strict` fails | Build documentation log |
| Old content after a successful deployment | The workflow passes and the browser shows an older version | Environment URL, deployment time, and browser cache |

## Incident Review

Record the symptom, affected component, log evidence, cause, fix, and recovery check.
