# Copier Template Python Backend

Copier template for a neutral Python backend application with explicit
architectural roles, strict typing, uv, Ruff, mypy, Pyright, pytest, and
dependency-injector containers.

## Generate a project

From this template directory:

```bash
copier copy . ../my-python-backend
```

Or with uvx:

```bash
uvx copier copy . ../my-python-backend
```

## Generated structure

The generated application keeps `app/` as the application package and separates
architecture by responsibility:

- `contracts/`
- `containers/`
- `use_cases/`
- `orchestrators/`
- `pipelines/`
- `operators/`
- `repositories/`
- `registries/`
- `facilitators/`
- `utilities/`
- `adapters/`
- `clients/`
- `gateways/`
- `transformers/`
- `schemas/`

The generated project includes `app/services/README.md` only to document that
`services` is a forbidden category. Do not add Python files there and do not turn
it into a package. Use the concrete architectural role that owns the behavior
instead.

Copier answers are written to `.dev_tools/copier/.copier-answers.yml`, keeping
template metadata with local development context instead of the project root.

Recopy or update generated projects with the explicit answers path:

```bash
copier recopy --answers-file .dev_tools/copier/.copier-answers.yml
copier update --answers-file .dev_tools/copier/.copier-answers.yml
```

## Verify a generated project

```bash
uv sync
uv run ruff check .
uv run mypy .
uv run pyright
uv run pytest
```
