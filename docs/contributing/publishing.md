# Publishing docs

Documentation is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to GitHub Pages automatically on every merge to `master`.

## Local preview

```bash
pip install -r requirements.txt   # install mkdocs-material and dependencies
mkdocs serve                      # starts a dev server at http://127.0.0.1:8000
```

Changes to `mkdocs.yml` or any file in `docs/` are hot-reloaded automatically. Use this to verify your contributor docs or schema reference pages look correct before pushing.

## Validate without serving

```bash
mkdocs build --strict
```

Runs a full build and treats any warnings as errors. Useful in a pre-push check or when you want to verify all nav entries resolve to real files.

## How CI deploys

The `.github/workflows/ci.yml` `deploy` job runs on every push to `master` after tests pass:

```yaml
- run: mkdocs gh-deploy --force
```

`mkdocs gh-deploy` builds the site and force-pushes the output to the `gh-pages` branch of the repository. GitHub Pages serves that branch at:

```
https://hdruk.github.io/schemata-2/
```

No manual action is needed — merging to `master` is sufficient.

!!! note "Docs are not regenerated in CI"
    The markdown files in `docs/` are committed to the repository. CI does **not** re-run `create_markdown.py`. Always run it locally and commit the output before merging (see [Releasing a version](releasing.md)).

## Adding new pages

1. Create a `.md` file anywhere under `docs/`
2. Add it to the `nav` section of `mkdocs.yml`
3. Preview with `mkdocs serve` and commit

Pages not listed in `nav` are still built but won't appear in the site navigation.

## MkDocs Material features available

The following features are enabled in `mkdocs.yml` and ready to use in any page:

| Feature | Syntax |
|---------|--------|
| Admonitions | `!!! note "Title"` / `!!! warning` / `!!! tip` |
| Collapsible admonitions | `??? note "Title"` |
| Code copy button | Enabled on all fenced code blocks |
| Tabbed code examples | ` === "Tab name"` blocks inside ` ``` ` |
| Syntax highlighting | Fenced blocks with a language identifier |

Example admonition:

```markdown
!!! warning "Run build.py before committing"
    CI will fail if schema.json files are out of sync with the Pydantic models.
```

Example tabbed code block:

```markdown
=== "HDRUK"

    ```bash
    pytest hdr_schemata/tests/test_hdruk.py
    ```

=== "GWDM"

    ```bash
    pytest hdr_schemata/tests/test_gwdm.py
    ```
```
