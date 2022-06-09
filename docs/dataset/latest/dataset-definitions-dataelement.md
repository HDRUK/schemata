# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/dataElement#/definitions/dataElement
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## dataElement Type

unknown

# dataElement Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                       |
| :-------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-column-name.md "#/properties/dataElement/name#/definitions/dataElement/properties/name")                      |
| [dataType](#datatype)       | `string`  | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-data-type.md "#/properties/dataElement/dataType#/definitions/dataElement/properties/dataType")                |
| [description](#description) | `string`  | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-column-description.md "#/properties/dataElement/description#/definitions/dataElement/properties/description") |
| [sensitive](#sensitive)     | `boolean` | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-sensitive.md "#/properties/dataElement/sensitive#/definitions/dataElement/properties/sensitive")              |
| Additional Properties       | Any       | Optional | can be null    |                                                                                                                                                                                  |

## name

The name of a column in a table.

> 255 Chars

`name`

*   is required

*   Type: merged type ([Column Name](dataset-definitions-dataelement-properties-column-name.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-column-name.md "#/properties/dataElement/name#/definitions/dataElement/properties/name")

### name Type

merged type ([Column Name](dataset-definitions-dataelement-properties-column-name.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-dataelement-properties-column-name-allof-0.md "check type definition")

## dataType

The data type of values in the column

> In future we could enumerate options for this, rather than just a string. 255 Chars

`dataType`

*   is required

*   Type: `string` ([Data Type](dataset-definitions-dataelement-properties-data-type.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-data-type.md "#/properties/dataElement/dataType#/definitions/dataElement/properties/dataType")

### dataType Type

`string` ([Data Type](dataset-definitions-dataelement-properties-data-type.md))

## description

A description of a column in a table.

`description`

*   is optional

*   Type: `string` ([Column Description](dataset-definitions-dataelement-properties-column-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-column-description.md "#/properties/dataElement/description#/definitions/dataElement/properties/description")

### description Type

`string` ([Column Description](dataset-definitions-dataelement-properties-column-description.md))

### description Constraints

**maximum length**: the maximum number of characters for this string is: `20000`

**minimum length**: the minimum number of characters for this string is: `1`

## sensitive

A True or False value, indicating if the field is sensitive or not

> We could clarify a definition of what is sensitive in the future.

`sensitive`

*   is required

*   Type: `boolean` ([Sensitive](dataset-definitions-dataelement-properties-sensitive.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-dataelement-properties-sensitive.md "#/properties/dataElement/sensitive#/definitions/dataElement/properties/sensitive")

### sensitive Type

`boolean` ([Sensitive](dataset-definitions-dataelement-properties-sensitive.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema