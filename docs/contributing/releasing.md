# Releasing a version

After writing a new schema version (see [Writing a schema](writing.md)), you need to regenerate the derived artefacts and update the documentation before opening a pull request.

## 1. Regenerate `schema.json` and `available.json`

```bash
python hdr_schemata/utils/build.py
```

This script:

- Scans every family directory (`HDRUK/`, `GWDM/`, `CRUK/`, `SchemaOrg/`) for `vX_Y_Z` sub-modules registered in each family's `__init__.py`
- Generates `schema.json` in an isolated subprocess for each version (to avoid `$defs` cross-contamination between families)
- Writes the updated `available.json` at the repo root

!!! warning "CI enforces this"
    The CI `test` job re-runs `build.py` and fails if the output differs from what's committed. Always run this locally and commit the result before pushing.

## 2. Regenerate the docs markdown

```bash
python hdr_schemata/utils/create_markdown.py
```

This generates three files per schema version in `docs/`:

| File | Contents |
|------|----------|
| `{family}/{version}.md` | Human-readable field reference tables |
| `{family}/{version}.form.json` | Form schema (used by the Gateway UI) |
| `{family}/{version}.structure.json` | Structural definition |

Commit all generated files alongside your Pydantic model changes.

## 3. Update `mkdocs.yml`

Add the new version to the `nav` section so it appears in the documentation site:

```yaml
nav:
    - Schemata:
          - HDRUK:
                # ... existing versions ...
                - Version X.Y.Z: HDRUK/X.Y.Z.md   # add this line
    - Schema Change Log:
          - HDRUK:
                # ... existing entries ...
                - X.Y.Z: HDRUK/X.Y.Z.change.md    # if you wrote a change log
```

## 4. Write a change log (recommended)

For any version published externally, create `docs/HDRUK/X.Y.Z.change.md` (or `docs/GWDM/X.Y.change.md`) describing what changed from the previous version. Reference it in the `Schema Change Log` nav section of `mkdocs.yml`.

## 5. Run the full test suite

```bash
pytest hdr_schemata/tests/
```

## Branch and PR workflow

```
dev  →  preprod  →  master
```

- **`dev`** — active development; CI runs tests and triggers the downstream `traser` service CI
- **`preprod`** — staging; same CI checks apply
- **`master`** — production; merging here automatically deploys the documentation to GitHub Pages

Open PRs against `dev` unless you have a specific reason to target another branch. The CI pipeline will validate `available.json`, run all pytest suites, and verify that `schema.json` files are in sync with the Pydantic models.
