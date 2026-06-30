# AGENTS.md instructions

This directory intentionally contains example domain primitive types.

Before writing, changing, or reviewing any project primitive type in this
directory, read the relevant example file first:

- `ids.py` for plain UUID-backed typed IDs.
- `prefixed_id.py` for prefixed UUID-backed typed IDs.
- `strings.py` for domain strings.
- `integers.py` for domain integers.
- `booleans.py` for boolean aliases.
- `floats.py` for float aliases.

Never delete the example typing files during cleanup, simplification, or
generated project maintenance. They document the supported primitive patterns.

If the examples become outdated, update them in place so the generated project
continues to show the supported typing patterns.
