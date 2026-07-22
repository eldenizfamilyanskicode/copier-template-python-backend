# AGENTS.md instructions

This directory intentionally contains example domain primitive types.

Before writing, changing, or reviewing any project primitive type in this
directory, read the relevant example file first:

- `ids.py` for plain UUID-backed typed IDs.
- `prefixed_id.py` for prefixed UUID-backed typed IDs.
- `strings.py` for domain strings.
- `constrained_strings.py` for domain strings with reusable value invariants.
- `integers.py` for domain integers.
- `constrained_integers.py` for domain integers with reusable value invariants.
- `booleans.py` for boolean aliases.
- `floats.py` for float aliases.

When a string or integer constraint is an invariant of a named domain type,
declare it on a `BaseConstrainedTypedString` or `BaseConstrainedTypedInt`
subclass. Do not compose reusable domain primitives from `Annotated`,
`AfterValidator`, or `StringConstraints`.

Each typed primitive represents exactly one domain meaning. Validation,
transformation, string processing, and arithmetic are semantic boundaries. Do
not reconstruct the source type after such an operation. Validate the result
and construct a different, explicitly named primitive when the result has a
domain meaning. A plain `str` or `int` result deliberately signals that the
source semantic guarantee has been lost.

Semantic stages must be sibling types. For example,
`RawUserInput(BaseTypedString)` becomes
`ValidatedUserInput(BaseTypedString)` after validation; do not inherit the
validated type from the raw type. Adding a delta to
`CurrentTimeInSeconds(BaseTypedInt)` must likewise produce a separately named
and validated destination type.

Multiple inheritance is forbidden for domain primitives. Never compose
meanings or constraints such as
`DivisibleBySix(DivisibleByTwo, DivisibleByThree)`. Declare the combined meaning
as an independent type such as `DivisibleBySix(BaseTypedInt)`.

Never delete the example typing files during cleanup, simplification, or
generated project maintenance. They document the supported primitive patterns.

If the examples become outdated, update them in place so the generated project
continues to show the supported typing patterns.
