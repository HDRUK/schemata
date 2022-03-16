# Enrichment and Linkage Schema

```txt
#/definitions/enrichmentAndLinkage#/properties/enrichmentAndLinkage
```

This section includes information about related datasets that may have previously been linked, as well as indicating if there is the opportunity to link to other datasets in the future. If a dataset has been enriched and/or derivations, scores and existing tools are available this section allows providers to indicate this to researchers.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## enrichmentAndLinkage Type

unknown ([Enrichment and Linkage](dataset-properties-enrichment-and-linkage.md))

# enrichmentAndLinkage Properties

| Property                                | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                           |
| :-------------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [qualifiedRelation](#qualifiedrelation) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md "#/properties/enrichmentAndLinkage/qualifiedRelation#/definitions/enrichmentAndLinkage/properties/qualifiedRelation") |
| [derivation](#derivation)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations.md "#/definitions/enrichmentAndLinkage#/definitions/enrichmentAndLinkage/properties/derivation")                             |
| [tools](#tools)                         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools.md "#/properties/enrichmentAndLinkage/tools#/definitions/enrichmentAndLinkage/properties/tools")                                   |

## qualifiedRelation

If applicable, please provide the DOI of other datasets that have previously been linked to this dataset and their availability. If no DOI is available, please provide the title of the datasets that can be linked, where possible using the same title of a dataset previously onboarded to the HOP. Note: If all the datasets from Gateway organisation can be linked please indicate “ALL” and the onboarding portal will automate linkage across the datasets submitted.

> dcat:qualifiedRelation

`qualifiedRelation`

*   is optional

*   Type: merged type ([Linked Datasets](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md "#/properties/enrichmentAndLinkage/qualifiedRelation#/definitions/enrichmentAndLinkage/properties/qualifiedRelation")

### qualifiedRelation Type

merged type ([Linked Datasets](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets-anyof-1.md "check type definition")

## derivation

Indicate if derived datasets or predefined extracts are available and the type of derivation available. Notes. Single or multiple dimensions can be provided as a derived extract alongside the dataset.

> prov:Derivation

`derivation`

*   is optional

*   Type: merged type ([Derivations](dataset-definitions-enrichmentandlinkage-properties-derivations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations.md "#/definitions/enrichmentAndLinkage#/definitions/enrichmentAndLinkage/properties/derivation")

### derivation Type

merged type ([Derivations](dataset-definitions-enrichmentandlinkage-properties-derivations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations-anyof-1.md "check type definition")

## tools

Please provide the URL of any analysis tools or models that have been created for this dataset and are available for further use. Multiple tools may be provided. Note: We encourage users to adopt a model along the lines of <https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/>

> No standard identified. We encourage users to adopt a model along the lines of <https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/>

`tools`

*   is optional

*   Type: merged type ([Tools](dataset-definitions-enrichmentandlinkage-properties-tools.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools.md "#/properties/enrichmentAndLinkage/tools#/definitions/enrichmentAndLinkage/properties/tools")

### tools Type

merged type ([Tools](dataset-definitions-enrichmentandlinkage-properties-tools.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools-anyof-1.md "check type definition")
