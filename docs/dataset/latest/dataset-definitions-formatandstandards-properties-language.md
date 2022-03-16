# Language Schema

```txt
#/properties/accessibility/formatAndStandards/language#/definitions/formatAndStandards/properties/language
```

This should list all the languages in which the dataset metadata and underlying data is made available.

> dct:language. FIXME: Conforms to spec, but may be a list of strings given cardinality 1:\*. Validate against external list of languages. Resources defined by the Library of Congress (ISO 639-1, ISO 639-2) SHOULD be used.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## language Type

merged type ([Language](dataset-definitions-formatandstandards-properties-language.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-1.md "check type definition")

## language Default Value

The default value is:

```json
"en"
```
