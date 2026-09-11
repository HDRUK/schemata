# HDRUK Schema

This repository defines the canonical metadata schemas used across the HDR UK Gateway platform. Schemas are authored as [Pydantic v2](https://docs.pydantic.dev/latest/) models in Python, from which JSON Schema files and reference documentation are automatically generated.

## Schema families

| Family | Versions | Description |
|--------|----------|-------------|
| **HDRUK** | 2.2.0 – 4.1.0 | Core HDR UK dataset metadata standard |
| **GWDM** | 2.0 – 2.2 | Gateway Data Model — the internal exchange format |
| **CRUK** | 1.0.0 | Cancer Research UK schema |
| **SchemaOrg** | BioSchema, default, GoogleRecommended | Schema.org mappings |

### Frozen versions

GWDM 1.0–1.2 and HDRUK 2.0.2–2.1.3 are **frozen**. They are still published and can
still be resolved by name and version, so stored records stamped with them keep
validating, but they are no longer built from Pydantic models and have no
documentation pages here. Their `schema.json` files remain at their usual paths and are
listed in `available.json`; the set of versions is recorded in `frozen.json`.

## Quick links

- [Contributing overview](contributing/index.md) — prerequisites and repository layout
- [Writing a schema](contributing/writing.md) — how to add or modify a schema version
- [Releasing a version](contributing/releasing.md) — regenerating JSON Schema and docs
- [Publishing docs](contributing/publishing.md) — local preview and CI deployment
