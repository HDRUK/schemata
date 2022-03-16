# Title Schema

```txt
#/summary/title#/definitions/summary/properties/title
```

Title of the dataset limited to 80 characters. It should provide a short description of the dataset and be unique across the gateway. If your title is not unique, please add a prefix with your organisation name or identifier to differentiate it from other datasets within the Gateway. Please avoid acronyms wherever possible. Good titles should summarise the content of the dataset and if relevant, the region the dataset covers.

> dct:title. title is reserved word in json schema

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## title Type

merged type ([Title](dataset-definitions-summary-properties-title.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-title-allof-0.md "check type definition")

## title Examples

```json
[
  "North West London COVID-19 Patient Level Situation Report"
]
```
