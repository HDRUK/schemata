# Releasing a version

After writing a new schema version (see [Writing a schema](writing.md)), you need to regenerate the derived artefacts and update the documentation before opening a pull request.

## 1. Regenerate every derived artefact

```bash
python -m hdr_schemata.build
```

One command produces everything. It:

- Scans every family directory (`HDRUK/`, `GWDM/`, `CRUK/`, `SchemaOrg/`) for the
  `vX_Y_Z` modules registered in that family's `__init__.py` — registering your class
  there is what makes it build
- Writes `schema.json` per version and the updated `available.json` at the repo root
- Generates the docs for each version and rewrites the `nav` in `mkdocs.yml`

| File | Contents |
|------|----------|
| `hdr_schemata/models/{family}/{version}/schema.json` | the published JSON Schema |
| `docs/{family}/{version}.md` | human-readable field reference tables |
| `docs/{family}/{version}.form.json` | form schema (used by the Gateway UI) |
| `docs/{family}/{version}.structure.json` | structural definition |
| `docs/{family}/{version}.change.md` | generated diff against the previous version |

Commit all generated files alongside your Pydantic model changes.

!!! warning "CI enforces this"
    The CI `test` job runs `python -m hdr_schemata.build --check` and fails with a list
    of stale files if the committed output differs from the models. Always run the build
    locally and commit the result before pushing.

!!! danger "Use Python 3.11 with pydantic 2.4.2"
    The generated markdown and `form.json` depend on the interpreter's type-annotation
    reprs. On Python 3.9 the generator drops whole field blocks from `form.json` and
    renders `typing.List[...]` instead of `List`. Building on any other version produces
    a spurious diff that CI will then reject.

## 2. Do not hand-edit the generated files

The nav in `mkdocs.yml` and every `{version}.change.md` are **generated**. The build
rewrites `mkdocs.yml` wholesale through PyYAML, so hand-added comments there are lost,
and a hand-written change log is overwritten on the next run.

The change log is a mechanical diff of each version against its predecessor, covering
field type, required and list-ness changes. If a release needs narrative release notes,
put them in a page of their own and add it to the nav by hand — outside the generated
version list.

## 3. Run the full test suite

```bash
cd hdr_schemata/tests/ && pytest
```

Run it as a single invocation rather than per-file. Every family is imported into one
process, which is what keeps annotation resolution honest: `test_annotations.py` asserts
that a version's annotations do not depend on the order families are imported in, and
the per-family `test_json_schema` tests compare an in-process build against the
committed `schema.json`.

## Branch and PR workflow

```
dev  →  preprod  →  master
```

- **`dev`** — active development; CI runs tests and triggers the downstream `traser` service CI
- **`preprod`** — staging; same CI checks apply
- **`master`** — production; merging here automatically deploys the documentation to GitHub Pages

Open PRs against `dev` unless you have a specific reason to target another branch. The CI pipeline will validate `available.json`, run all pytest suites, and verify that `schema.json` files are in sync with the Pydantic models.
