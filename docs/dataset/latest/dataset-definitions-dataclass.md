# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/dataClass#/definitions/dataClass
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## dataClass Type

unknown

# dataClass Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                |
| :-------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)               | `string` | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-table-name.md "#/properties/dataClass/name#/definitions/dataClass/properties/name")                      |
| [description](#description) | Merged   | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-table-description.md "#/properties/dataClass/description#/definitions/dataClass/properties/description") |
| [elements](#elements)       | `array`  | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-data-elements.md "#/properties/dataClass/elements#/definitions/dataClass/properties/elements")           |

## name

The name of a table in a dataset.

> Should be limited to 255 Characters, abstract text requires rewrite.

`name`

*   is required

*   Type: `string` ([Table Name](dataset-definitions-dataclass-properties-table-name.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-table-name.md "#/properties/dataClass/name#/definitions/dataClass/properties/name")

### name Type

`string` ([Table Name](dataset-definitions-dataclass-properties-table-name.md))

## description

A description of a table in a dataset.

`description`

*   is optional

*   Type: merged type ([Table Description](dataset-definitions-dataclass-properties-table-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-table-description.md "#/properties/dataClass/description#/definitions/dataClass/properties/description")

### description Type

merged type ([Table Description](dataset-definitions-dataclass-properties-table-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-dataclass-properties-table-description-allof-0.md "check type definition")

## elements

A list of data elements contained within a table in a dataset.

`elements`

*   is required

*   Type: an array of merged types ([Details](dataset-definitions-dataclass-properties-data-elements-items.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataclass-properties-data-elements.md "#/properties/dataClass/elements#/definitions/dataClass/properties/elements")

### elements Type

an array of merged types ([Details](dataset-definitions-dataclass-properties-data-elements-items.md))
