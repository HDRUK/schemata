# HDRUK Schema

This repository defines the canonical metadata schemas used across the HDR UK Gateway platform. Schemas are authored as [Pydantic v2](https://docs.pydantic.dev/latest/) models in Python, from which JSON Schema files and reference documentation are automatically generated.

## Schema families

| Family | Versions | Description |
|--------|----------|-------------|
| **HDRUK** | 2.1.2 – 4.0.0 | Core HDR UK dataset metadata standard |
| **GWDM** | 1.0 – 3.0 | Gateway Data Model — the internal exchange format |
| **CRUK** | 1.0.0 | Cancer Research UK schema |
| **SchemaOrg** | BioSchema, default, GoogleRecommended | Schema.org mappings |

## Quick links

- [Contributing overview](contributing/index.md) — prerequisites and repository layout
- [Writing a schema](contributing/writing.md) — how to add or modify a schema version
- [Releasing a version](contributing/releasing.md) — regenerating JSON Schema and docs
- [Publishing docs](contributing/publishing.md) — local preview and CI deployment
