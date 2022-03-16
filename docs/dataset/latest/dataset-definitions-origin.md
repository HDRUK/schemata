# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/origin#/definitions/origin
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## origin Type

unknown

# origin Properties

| Property                                    | Type   | Required | Nullable       | Defined by                                                                                                                                                                        |
| :------------------------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [purpose](#purpose)                         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose.md "#/properties/provenance/origin/purpose#/definitions/origin/properties/purpose")                         |
| [source](#source)                           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-source.md "#/properties/provenance/origin/source#/definitions/origin/properties/source")                            |
| [collectionSituation](#collectionsituation) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-setting.md "#/properties/provenance/origin/collectionSituation#/definitions/origin/properties/collectionSituation") |

## purpose

Pleases indicate the purpose(s) that the dataset was collected.

> <https://ddialliance.org/Specification/DDI-Lifecycle/3.3/XMLSchema/FieldLevelDocumentation/>

`purpose`

*   is optional

*   Type: merged type ([Purpose](dataset-definitions-origin-properties-purpose.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose.md "#/properties/provenance/origin/purpose#/definitions/origin/properties/purpose")

### purpose Type

merged type ([Purpose](dataset-definitions-origin-properties-purpose.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose-anyof-1.md "check type definition")

## source

Pleases indicate the source of the data extraction

> <https://dublincore.org/specifications/dublin-core/dcmi-terms/#source>

`source`

*   is optional

*   Type: merged type ([Source](dataset-definitions-origin-properties-source.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-source.md "#/properties/provenance/origin/source#/definitions/origin/properties/source")

### source Type

merged type ([Source](dataset-definitions-origin-properties-source.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-source-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-source-anyof-1.md "check type definition")

## collectionSituation

Pleases indicate the setting(s) where data was collected. Multiple settings may be provided

> <https://ddialliance.org/Specification/DDI-Lifecycle/3.2/XMLSchema/FieldLevelDocumentation/>

`collectionSituation`

*   is optional

*   Type: merged type ([Setting](dataset-definitions-origin-properties-setting.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-setting.md "#/properties/provenance/origin/collectionSituation#/definitions/origin/properties/collectionSituation")

### collectionSituation Type

merged type ([Setting](dataset-definitions-origin-properties-setting.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-setting-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-setting-anyof-1.md "check type definition")
