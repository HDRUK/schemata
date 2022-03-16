# Accessibility Schema

```txt
#/definitions/accessibility#/properties/accessibility
```

Accessibility information allows researchers to understand access, usage, limitations, formats, standards and linkage or interoperability with toolsets.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## accessibility Type

unknown ([Accessibility](dataset-properties-accessibility.md))

# accessibility Properties

| Property                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :---------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [usage](#usage)                           | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-usage.md "#/definitions/accessibility/usage#/definitions/accessibility/properties/usage")                                          |
| [access](#access)                         | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-access.md "#/definitions/accessibility/access#/definitions/accessibility/properties/access")                                       |
| [formatAndStandards](#formatandstandards) | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-format-and-standards.md "#/definitions/accessibility/formatAndStandards#/definitions/accessibility/properties/formatAndStandards") |

## usage

This section includes information about how the data can be used and how it is currently being used

`usage`

*   is optional

*   Type: unknown ([Usage](dataset-definitions-accessibility-properties-usage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-usage.md "#/definitions/accessibility/usage#/definitions/accessibility/properties/usage")

### usage Type

unknown ([Usage](dataset-definitions-accessibility-properties-usage.md))

## access

This section includes information about data access

`access`

*   is required

*   Type: unknown ([Access](dataset-definitions-accessibility-properties-access.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-access.md "#/definitions/accessibility/access#/definitions/accessibility/properties/access")

### access Type

unknown ([Access](dataset-definitions-accessibility-properties-access.md))

## formatAndStandards

Section includes technical attributes for language vocabularies, sizes etc. and gives researchers facts about and processing the underlying data in the dataset.

`formatAndStandards`

*   is optional

*   Type: unknown ([Format and Standards](dataset-definitions-accessibility-properties-format-and-standards.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-format-and-standards.md "#/definitions/accessibility/formatAndStandards#/definitions/accessibility/properties/formatAndStandards")

### formatAndStandards Type

unknown ([Format and Standards](dataset-definitions-accessibility-properties-format-and-standards.md))
