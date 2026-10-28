# Contributing

- Keep the observer strictly read-only and avoid cross-repository command execution.
- Preserve explicit provenance and source ownership for every report field.
- If an API endpoint cannot be read, return UNKNOWN; do not convert errors to zero.
- Add offline tests for failure, truncation, missing permission, schema mismatch and source integrity.
- Treat historical diagnostic reports as evidence *claims*, not verified proof.
- Validate changes locally with `python -m unittest discover -s tests -v`.
