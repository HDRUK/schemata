# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/usage#/definitions/usage
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json\*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## usage Type

unknown

# usage Properties

| Property                                    | Type   | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :------------------------------------------ | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [dataUseLimitation](#datauselimitation)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation.md "#/properties/accessibility/usage/dataUseLimitation#/definitions/usage/properties/dataUseLimitation")       |
| [dataUseRequirements](#datauserequirements) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements.md "#/properties/accessibility/usage/dataUseRequirements#/definitions/usage/properties/dataUseRequirements") |
| [resourceCreator](#resourcecreator)         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements.md "#/properties/accessibility/usage/resourceCreator#/definitions/usage/properties/resourceCreator")         |
| [investigations](#investigations)           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations.md "#/definitions/usage#/definitions/usage/properties/investigations")                                              |
| [isReferencedBy](#isreferencedby)           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-citations.md "#/definitions/usage#/definitions/usage/properties/isReferencedBy")                                                   |

## dataUseLimitation

Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. NOTE: we have extended the DUO to include a value for NO LINKAGE

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseLimitation`

*   is optional

*   Type: merged type ([Data Use Limitation](dataset-definitions-usage-properties-data-use-limitation.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation.md "#/properties/accessibility/usage/dataUseLimitation#/definitions/usage/properties/dataUseLimitation")

### dataUseLimitation Type

merged type ([Data Use Limitation](dataset-definitions-usage-properties-data-use-limitation.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation-anyof-1.md "check type definition")

## dataUseRequirements

Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseRequirements`

*   is optional

*   Type: merged type ([Data Use Requirements](dataset-definitions-usage-properties-data-use-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements.md "#/properties/accessibility/usage/dataUseRequirements#/definitions/usage/properties/dataUseRequirements")

### dataUseRequirements Type

merged type ([Data Use Requirements](dataset-definitions-usage-properties-data-use-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements-anyof-1.md "check type definition")

## resourceCreator

Please provide the text that you would like included as part of any citation that credits this dataset. This is typically just the name of the publisher.   No employee details should be provided.

> dct:creator

`resourceCreator`

*   is optional

*   Type: merged type ([Citation Requirements](dataset-definitions-usage-properties-citation-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements.md "#/properties/accessibility/usage/resourceCreator#/definitions/usage/properties/resourceCreator")

### resourceCreator Type

merged type ([Citation Requirements](dataset-definitions-usage-properties-citation-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements-anyof-1.md "check type definition")

## investigations



> No standard identified

`investigations`

*   is optional

*   Type: merged type ([Investigations](dataset-definitions-usage-properties-investigations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations.md "#/definitions/usage#/definitions/usage/properties/investigations")

### investigations Type

merged type ([Investigations](dataset-definitions-usage-properties-investigations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations-anyof-1.md "check type definition")

## isReferencedBy

Please provide the keystone paper associated with the dataset. Also include a list of known citations, if available and should be links to existing resources where the dataset has been used or referenced. Please provide multiple entries, or if you are using a csv upload please provide them as a tab separated list.

> dct:isReferencedBy

`isReferencedBy`

*   is optional

*   Type: merged type ([Citations](dataset-definitions-usage-properties-citations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-citations.md "#/definitions/usage#/definitions/usage/properties/isReferencedBy")

### isReferencedBy Type

merged type ([Citations](dataset-definitions-usage-properties-citations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-citations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-citations-anyof-1.md "check type definition")
