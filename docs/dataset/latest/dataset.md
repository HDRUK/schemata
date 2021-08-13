# HDR UK Dataset Schema Schema

```txt
https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json
```

HDR UK Dataset Metadata JSONSchema

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## HDR UK Dataset Schema Type

`object` ([HDR UK Dataset Schema](dataset.md))

# HDR UK Dataset Schema Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                  |
| :-------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| [identifier](#identifier)                     | Merged        | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-dataset-identifier.md "#/properties/identifier#/properties/identifier")                          |
| [version](#version)                           | `string`      | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-dataset-version.md "#/properties/version#/properties/version")                                   |
| [revisions](#revisions)                       | `array`       | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-dataset-revisions.md "#/properties/revisions#/properties/revisions")                             |
| [issued](#issued)                             | `string`      | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-creation-date.md "#/properties/issued#/properties/issued")                                       |
| [modified](#modified)                         | `string`      | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-modification-date.md "#/properties/modified#/properties/modified")                               |
| [summary](#summary)                           | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-summary.md "#/definitions/summary#/properties/summary")                                          |
| [documentation](#documentation)               | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-properties-documentation.md "#/definitions/documentation#/properties/documentation")                        |
| [coverage](#coverage)                         | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-properties-coverage.md "#/definitions/coverage#/properties/coverage")                                       |
| [provenance](#provenance)                     | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-properties-provenance.md "#/definitions/provenance#/properties/provenance")                                 |
| [accessibility](#accessibility)               | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-properties-accessibility.md "#/definitions/accessibility#/properties/accessibility")                        |
| [enrichmentAndLinkage](#enrichmentandlinkage) | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-properties-enrichment-and-linkage.md "#/definitions/enrichmentAndLinkage#/properties/enrichmentAndLinkage") |
| [observations](#observations)                 | `array`       | Optional | cannot be null | [HDR UK Dataset Schema](dataset-properties-observations.md "#/properties/observations#/properties/observations")                            |

## identifier

System dataset identifier

> <http://purl.org/dc/terms/identifier>

`identifier`

*   is required

*   Type: merged type ([Dataset identifier](dataset-properties-dataset-identifier.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-dataset-identifier.md "#/properties/identifier#/properties/identifier")

### identifier Type

merged type ([Dataset identifier](dataset-properties-dataset-identifier.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-properties-dataset-identifier-anyof-0.md "check type definition")

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-properties-dataset-identifier-anyof-1.md "check type definition")

### identifier Examples

```json
[
  "226fb3f1-4471-400a-8c39-2b66d46a39b6",
  "https://web.www.healthdatagateway.org/dataset/226fb3f1-4471-400a-8c39-2b66d46a39b6"
]
```

## version

Dataset metadata version

`version`

*   is required

*   Type: `string` ([Dataset Version](dataset-properties-dataset-version.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-dataset-version.md "#/properties/version#/properties/version")

### version Type

`string` ([Dataset Version](dataset-properties-dataset-version.md))

### version Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([0-9]+)\.([0-9]+)\.([0-9]+)$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-9%5D%2B\)%5C.\(%5B0-9%5D%2B\)%5C.\(%5B0-9%5D%2B\)%24 "try regular expression with regexr.com")

### version Examples

```json
"1.1.0"
```

## revisions

Revisions of Dataset metadata

`revisions`

*   is required

*   Type: an array of merged types ([Details](dataset-properties-dataset-revisions-items.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-dataset-revisions.md "#/properties/revisions#/properties/revisions")

### revisions Type

an array of merged types ([Details](dataset-properties-dataset-revisions-items.md))

## issued

Dataset Metadata Creation Date

> dcat:issued

`issued`

*   is required

*   Type: `string` ([Creation Date](dataset-properties-creation-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-creation-date.md "#/properties/issued#/properties/issued")

### issued Type

`string` ([Creation Date](dataset-properties-creation-date.md))

### issued Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## modified

Dataset Metadata Creation Date

> dcat:modified

`modified`

*   is required

*   Type: `string` ([Modification Date](dataset-properties-modification-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-modification-date.md "#/properties/modified#/properties/modified")

### modified Type

`string` ([Modification Date](dataset-properties-modification-date.md))

### modified Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## summary

Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.

`summary`

*   is required

*   Type: unknown ([Summary](dataset-properties-summary.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-summary.md "#/definitions/summary#/properties/summary")

### summary Type

unknown ([Summary](dataset-properties-summary.md))

## documentation

Documentation can include a rich text description of the dataset or links to media such as documents, images, presentations, videos or links to data dictionaries, profiles or dashboards. Organisations are required to confirm that they have permission to distribute any additional media.

`documentation`

*   is optional

*   Type: unknown ([Documentation](dataset-properties-documentation.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-documentation.md "#/definitions/documentation#/properties/documentation")

### documentation Type

unknown ([Documentation](dataset-properties-documentation.md))

## coverage

This information includes attributes for geographical and temporal coverage, cohort details etc. to enable a deeper understanding of the dataset content so that researchers can make decisions about the relevance of the underlying data.

`coverage`

*   is optional

*   Type: unknown ([Coverage](dataset-properties-coverage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-coverage.md "#/definitions/coverage#/properties/coverage")

### coverage Type

unknown ([Coverage](dataset-properties-coverage.md))

## provenance

Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.

`provenance`

*   is optional

*   Type: unknown ([Provenance](dataset-properties-provenance.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-provenance.md "#/definitions/provenance#/properties/provenance")

### provenance Type

unknown ([Provenance](dataset-properties-provenance.md))

## accessibility

Accessibility information allows researchers to understand access, usage, limitations, formats, standards and linkage or interoperability with toolsets.

`accessibility`

*   is required

*   Type: unknown ([Accessibility](dataset-properties-accessibility.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-accessibility.md "#/definitions/accessibility#/properties/accessibility")

### accessibility Type

unknown ([Accessibility](dataset-properties-accessibility.md))

## enrichmentAndLinkage

This section includes information about related datasets that may have previously been linked, as well as indicating if there is the opportunity to link to other datasets in the future. If a dataset has been enriched and/or derivations, scores and existing tools are available this section allows providers to indicate this to researchers.

`enrichmentAndLinkage`

*   is optional

*   Type: unknown ([Enrichment and Linkage](dataset-properties-enrichment-and-linkage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-enrichment-and-linkage.md "#/definitions/enrichmentAndLinkage#/properties/enrichmentAndLinkage")

### enrichmentAndLinkage Type

unknown ([Enrichment and Linkage](dataset-properties-enrichment-and-linkage.md))

## observations

Multiple observations about the dataset may be provided and users are expected to provide at least one observation (1..\*). We will be supporting the schema.org observation model (<https://schema.org/Observation>) with default values. Users will be encouraged to provide their own statistical populations as the project progresses. Example: \<b> Statistical Population 1 \</b> type: StatisticalPopulation populationType: Persons numConstraints: 0 \<b> Statistical Population 2 \</b> type: StatisticalPopulation populationType: Events numConstraints: 0 \<b> Statistical Population 3 \</b> type: StatisticalPopulation populationType: Findings numConstraints: 0 typeOf: Observation observedNode: \<b> Statistical Population 1 \</b> measuredProperty: count measuredValue: 32937 observationDate: “2017”

> <https://schema.org/observation>

`observations`

*   is optional

*   Type: an array of merged types ([Details](dataset-properties-observations-items.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-properties-observations.md "#/properties/observations#/properties/observations")

### observations Type

an array of merged types ([Details](dataset-properties-observations-items.md))

# HDR UK Dataset Schema Definitions

## Definitions group revision

Reference this group by using

```json
{"$ref":"#/definitions/revision#/definitions/revision"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                            |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [version](#version-1) | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-revision-properties-version.md "#/definitions/revision/version#/definitions/revision/properties/version") |
| [url](#url)           | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-revision-properties-url.md "#/definitions/revision/url#/definitions/revision/properties/url")             |

### version

Semantic Version

`version`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-revision-properties-version.md "#/definitions/revision/version#/definitions/revision/properties/version")

#### version Type

unknown

### url

URL endpoint to obtain the version

`url`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-revision-properties-url.md "#/definitions/revision/url#/definitions/revision/properties/url")

#### url Type

unknown

## Definitions group summary

Reference this group by using

```json
{"$ref":"#/definitions/summary#/definitions/summary"}
```

| Property                                      | Type   | Required | Nullable       | Defined by                                                                                                                                                                             |
| :-------------------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [title](#title)                               | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-title.md "#/summary/title#/definitions/summary/properties/title")                                                       |
| [abstract](#abstract)                         | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract.md "#/summary/abstract#/definitions/summary/properties/abstract")                                      |
| [publisher](#publisher)                       | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher.md "#/summary/publisher#/definitions/summary/properties/publisher")                                   |
| [contactPoint](#contactpoint)                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point.md "#/summary/contactPoint#/definitions/summary/properties/contactPoint")                                 |
| [keywords](#keywords)                         | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords.md "#/summary/keywords#/definitions/summary/properties/keywords")                                              |
| [alternateIdentifiers](#alternateidentifiers) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers.md "#/summary/alternateIdentifiers#/definitions/summary/properties/alternateIdentifiers") |
| [doiName](#doiname)                           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier.md "#/summary/doiName#/definitions/summary/properties/doiName")                               |

### title

Title of the dataset limited to 80 characters. It should provide a short description of the dataset and be unique across the gateway. If your title is not unique, please add a prefix with your organisation name or identifier to differentiate it from other datasets within the Gateway. Please avoid acronyms wherever possible. Good titles should summarise the content of the dataset and if relevant, the region the dataset covers.

> dct:title. title is reserved word in json schema

`title`

*   is required

*   Type: merged type ([Title](dataset-definitions-summary-properties-title.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-title.md "#/summary/title#/definitions/summary/properties/title")

#### title Type

merged type ([Title](dataset-definitions-summary-properties-title.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-title-allof-0.md "check type definition")

#### title Examples

```json
[
  "North West London COVID-19 Patient Level Situation Report"
]
```

### abstract

Provide a clear and brief descriptive signpost for researchers who are searching for data that may be relevant to their research. The abstract should allow the reader to determine the scope of the data collection and accurately summarise its content. The optimal length is one paragraph (limited to 255 characters) and effective abstracts should avoid long sentences and abbreviations where possible

> dct:abstract

`abstract`

*   is required

*   Type: merged type ([Dataset Abstract](dataset-definitions-summary-properties-dataset-abstract.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract.md "#/summary/abstract#/definitions/summary/properties/abstract")

#### abstract Type

merged type ([Dataset Abstract](dataset-definitions-summary-properties-dataset-abstract.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract-allof-0.md "check type definition")

#### abstract Examples

```json
"CPRD Aurum contains primary care data contributed by General Practitioner (GP) practices using EMIS Web® including patient registration information and all care events that GPs have chosen to record as part of their usual medical practice."
```

### publisher

This is the organisation responsible for running or supporting the data access request process, as well as publishing and maintaining the metadata. In most this will be the same as the HDR UK Organisation (Hub or Alliance Member). However, in some cases this will be different i.e. Tissue Directory are an HDR UK Gateway organisation but coordinate activities across a number of data publishers i.e. Cambridge Blood and Stem Cell Biobank.

> Conforms to spec, but this MAY be an an object of organisation. <https://schema.org/publisher>

`publisher`

*   is required

*   Type: merged type ([Dataset publisher](dataset-definitions-summary-properties-dataset-publisher.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher.md "#/summary/publisher#/definitions/summary/properties/publisher")

#### publisher Type

merged type ([Dataset publisher](dataset-definitions-summary-properties-dataset-publisher.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher-allof-0.md "check type definition")

### contactPoint

Please provide a valid email address that can be used to coordinate data access requests with the publisher. Organisations are expected to provide a dedicated email address associated with the data access request process. Notes: An employee’s email address can only be provided on a temporary basis and if one is provided an explicit consent must be obtained for this purpose.

> dcat:contactPoint

`contactPoint`

*   is required

*   Type: merged type ([Contact Point](dataset-definitions-summary-properties-contact-point.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point.md "#/summary/contactPoint#/definitions/summary/properties/contactPoint")

#### contactPoint Type

merged type ([Contact Point](dataset-definitions-summary-properties-contact-point.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point-allof-0.md "check type definition")

#### contactPoint Default Value

The default value is:

```json
"Defaulted to the contact point of the primary organisation of the user however, can be overridden for specific datasets"
```

#### contactPoint Examples

```json
"SAILDatabank@swansea.ac.uk"
```

### keywords

Please provide relevant and specific keywords that can improve the SEO of your dataset as a comma separated list. Notes: Onboarding portal will suggest keywords based on title, abstract and description. We are compiling a standardised list of keywords and synonyms across datasets to make filtering easier for users.

> dcat:keyword. May be an array of strings or comma seperated list.

`keywords`

*   is required

*   Type: merged type ([Keywords](dataset-definitions-summary-properties-keywords.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords.md "#/summary/keywords#/definitions/summary/properties/keywords")

#### keywords Type

merged type ([Keywords](dataset-definitions-summary-properties-keywords.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords-anyof-1.md "check type definition")

### alternateIdentifiers

Alternate dataset identifiers or local identifiers

> DATA-CITE alternate-identifiers used. Note, will support comma separated list for backwards compatibility with other systems

`alternateIdentifiers`

*   is optional

*   Type: merged type ([Alternate dataset identifiers](dataset-definitions-summary-properties-alternate-dataset-identifiers.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers.md "#/summary/alternateIdentifiers#/definitions/summary/properties/alternateIdentifiers")

#### alternateIdentifiers Type

merged type ([Alternate dataset identifiers](dataset-definitions-summary-properties-alternate-dataset-identifiers.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers-anyof-1.md "check type definition")

### doiName

All HDR UK registered datasets should either have a Digital Object Identifier (DOI) or be working towards obtaining one. If a DOI is available, please provide the DOI.

> Vocabulary: DOI Data Dictionary

`doiName`

*   is optional

*   Type: merged type ([Digital Object Identifier](dataset-definitions-summary-properties-digital-object-identifier.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier.md "#/summary/doiName#/definitions/summary/properties/doiName")

#### doiName Type

merged type ([Digital Object Identifier](dataset-definitions-summary-properties-digital-object-identifier.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier-allof-0.md "check type definition")

#### doiName Examples

```json
"10.3399/bjgp17X692645"
```

## Definitions group organisation

Reference this group by using

```json
{"$ref":"#/definitions/organisation#/definitions/organisation"}
```

| Property                                    | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------------------ | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [identifier](#identifier-1)                 | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier.md "#/organisation/identifier#/definitions/organisation/properties/identifier")                        |
| [name](#name)                               | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name.md "#/organisation/name#/definitions/organisation/properties/name")                                          |
| [logo](#logo)                               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo.md "#/organisation/logo#/definitions/organisation/properties/logo")                                          |
| [description](#description)                 | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description.md "#/organisation/description#/definitions/organisation/properties/description")                     |
| [contactPoint](#contactpoint-1)             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md "#/organisation/contactPoint#/definitions/organisation/properties/contactPoint")                 |
| [memberOf](#memberof)                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership.md "#/organisation/memberOf#/definitions/organisation/properties/memberOf")                            |
| [accessRights](#accessrights)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md "#/organisation/accessRights#/definitions/organisation/properties/accessRights")         |
| [deliveryLeadTime](#deliveryleadtime)       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration.md "#/organisation/deliveryLeadTime#/definitions/organisation/properties/deliveryLeadTime")            |
| [accessService](#accessservice)             | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service.md "#/organisation/accessService#/definitions/organisation/properties/accessService")              |
| [accessRequestCost](#accessrequestcost)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md "#/organisation/accessRequestCost#/definitions/organisation/properties/accessRequestCost") |
| [dataUseLimitation](#datauselimitation)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation.md "#/organisation/dataUseLimitation#/definitions/organisation/properties/dataUseLimitation")              |
| [dataUseRequirements](#datauserequirements) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements.md "#/organisation/dataUseRequirements#/definitions/organisation/properties/dataUseRequirements")        |

### identifier

Please provide a Grid.ac identifier (see <https://www.grid.ac/institutes>) for your organisation. If your organisation does not have a Grid.ac identifier please use the “suggest and institute” function here: <https://www.grid.ac/institutes#>

> <https://schema.org/identifier>

`identifier`

*   is optional

*   Type: merged type ([Organisation Identifier](dataset-definitions-organisation-metadata-properties-organisation-identifier.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier.md "#/organisation/identifier#/definitions/organisation/properties/identifier")

#### identifier Type

merged type ([Organisation Identifier](dataset-definitions-organisation-metadata-properties-organisation-identifier.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier-allof-0.md "check type definition")

### name

Name of the organisation

> <https://schema.org/name>

`name`

*   is required

*   Type: merged type ([Organisation Name](dataset-definitions-organisation-metadata-properties-organisation-name.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name.md "#/organisation/name#/definitions/organisation/properties/name")

#### name Type

merged type ([Organisation Name](dataset-definitions-organisation-metadata-properties-organisation-name.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name-allof-0.md "check type definition")

### logo

Please provide a logo associated with the Gateway Organisation using a valid URL. The following formats will be accepted .jpg, .png or .svg.

> <https://schema.org/logo>

`logo`

*   is optional

*   Type: merged type ([Organisation Logo](dataset-definitions-organisation-metadata-properties-organisation-logo.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo.md "#/organisation/logo#/definitions/organisation/properties/logo")

#### logo Type

merged type ([Organisation Logo](dataset-definitions-organisation-metadata-properties-organisation-logo.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo-allof-0.md "check type definition")

### description

Please provide a URL that describes the organisation.

> <https://schema.org/description>

`description`

*   is optional

*   Type: merged type ([Organisation Description](dataset-definitions-organisation-metadata-properties-organisation-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description.md "#/organisation/description#/definitions/organisation/properties/description")

#### description Type

merged type ([Organisation Description](dataset-definitions-organisation-metadata-properties-organisation-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description-allof-0.md "check type definition")

### contactPoint

Organisation contact point(s)

> <https://schema.org/contactPoint>

`contactPoint`

*   is required

*   Type: merged type ([Organisation Contact Point](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md "#/organisation/contactPoint#/definitions/organisation/properties/contactPoint")

#### contactPoint Type

merged type ([Organisation Contact Point](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point-anyof-1.md "check type definition")

### memberOf

Please indicate if the organisation is an Alliance Member or a Hub.

> <https://schema.org/memberOf>

`memberOf`

*   is optional

*   Type: merged type ([Organisation Membership](dataset-definitions-organisation-metadata-properties-organisation-membership.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership.md "#/organisation/memberOf#/definitions/organisation/properties/memberOf")

#### memberOf Type

merged type ([Organisation Membership](dataset-definitions-organisation-metadata-properties-organisation-membership.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership-allof-0.md "check type definition")

### accessRights

The URL of a webpage where the data access request process and/or guidance is provided. If there is more than one access process i.e. industry vs academic please provide both.

> dct:access_rights

`accessRights`

*   is optional

*   Type: merged type ([Organisation Default Access Rights](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md "#/organisation/accessRights#/definitions/organisation/properties/accessRights")

#### accessRights Type

merged type ([Organisation Default Access Rights](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights-anyof-1.md "check type definition")

### deliveryLeadTime

Please provide an indication of the typical processing times based on the types of requests typically received. Note: This value will be used as default access request duration for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> <https://schema.org/deliveryLeadTime>

`deliveryLeadTime`

*   is optional

*   Type: merged type ([Access Request Duration](dataset-definitions-organisation-metadata-properties-access-request-duration.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration.md "#/organisation/deliveryLeadTime#/definitions/organisation/properties/deliveryLeadTime")

#### deliveryLeadTime Type

merged type ([Access Request Duration](dataset-definitions-organisation-metadata-properties-access-request-duration.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration-allof-0.md "check type definition")

### accessService

Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> dcat:accessService

`accessService`

*   is optional

*   Type: merged type ([Organisation Access Service](dataset-definitions-organisation-metadata-properties-organisation-access-service.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service.md "#/organisation/accessService#/definitions/organisation/properties/accessService")

#### accessService Type

merged type ([Organisation Access Service](dataset-definitions-organisation-metadata-properties-organisation-access-service.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service-allof-0.md "check type definition")

#### accessService Examples

```json
"https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide"
```

### accessRequestCost

Please provide link(s) to a webpage or a short description detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.

> No standard identified

`accessRequestCost`

*   is optional

*   Type: merged type ([Organisation Access Request Cost](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md "#/organisation/accessRequestCost#/definitions/organisation/properties/accessRequestCost")

#### accessRequestCost Type

merged type ([Organisation Access Request Cost](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost-anyof-1.md "check type definition")

### dataUseLimitation

Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Notes: where there are existing data-sharing arrangements such as the HDR UK HUB data sharing agreement or the NIHR HIC data sharing agreement this should be indicated within access rights. This value will be used as terms for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseLimitation`

*   is optional

*   Type: merged type ([Data Use Limitation](dataset-definitions-organisation-metadata-properties-data-use-limitation.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation.md "#/organisation/dataUseLimitation#/definitions/organisation/properties/dataUseLimitation")

#### dataUseLimitation Type

merged type ([Data Use Limitation](dataset-definitions-organisation-metadata-properties-data-use-limitation.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation-anyof-1.md "check type definition")

### dataUseRequirements

Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseRequirements`

*   is optional

*   Type: merged type ([Data Use Requirements](dataset-definitions-organisation-metadata-properties-data-use-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements.md "#/organisation/dataUseRequirements#/definitions/organisation/properties/dataUseRequirements")

#### dataUseRequirements Type

merged type ([Data Use Requirements](dataset-definitions-organisation-metadata-properties-data-use-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements-anyof-1.md "check type definition")

## Definitions group documentation

Reference this group by using

```json
{"$ref":"#/definitions/documentation#/definitions/documentation"}
```

| Property                            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                   |
| :---------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description-1)       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-description.md "#/properties/documentation/description#/definitions/documentation/properties/description")              |
| [associatedMedia](#associatedmedia) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media.md "#/properties/documentation/associatedMedia#/definitions/documentation/properties/associatedMedia") |
| [isPartOf](#ispartof)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-group.md "#/properties/documentation/isPartOf#/definitions/documentation/properties/isPartOf")                          |

### description

A free-text description of the record.

> dc:description, <https://schema.org/description>

`description`

*   is optional

*   Type: merged type ([Description](dataset-definitions-documentation-properties-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-description.md "#/properties/documentation/description#/definitions/documentation/properties/description")

#### description Type

merged type ([Description](dataset-definitions-documentation-properties-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-description-allof-0.md "check type definition")

### associatedMedia

Please provide any media associated with the Gateway Organisation using a valid URI for the content. This is an opportunity to provide additional context that could be useful for researchers wanting to understand more about the dataset and its relevance to their research question. The following formats will be accepted .jpg, .png or .svg, .pdf, .xslx or .docx. Note: media asset can be hosted by the organisation or uploaded using the onboarding portal.

> <https://schema.org/associatedMedia>

`associatedMedia`

*   is optional

*   Type: merged type ([Associated Media](dataset-definitions-documentation-properties-associated-media.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media.md "#/properties/documentation/associatedMedia#/definitions/documentation/properties/associatedMedia")

#### associatedMedia Type

merged type ([Associated Media](dataset-definitions-documentation-properties-associated-media.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media-anyof-1.md "check type definition")

#### associatedMedia Examples

```json
"PDF Document that describes study protocol"
```

### isPartOf

Please complete only if the dataset is part of a group or family

> <https://schema.org/isPartOf> NOTE: we may make Groups first class citizens so the are navigable

`isPartOf`

*   is optional

*   Type: merged type ([Group](dataset-definitions-documentation-properties-group.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-group.md "#/properties/documentation/isPartOf#/definitions/documentation/properties/isPartOf")

#### isPartOf Type

merged type ([Group](dataset-definitions-documentation-properties-group.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-group-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-documentation-properties-group-anyof-1.md "check type definition")

#### isPartOf Default Value

The default value is:

```json
"NOT APPLICABLE"
```

#### isPartOf Examples

```json
"Hospital Episodes Statistics datasets (A&E, APC, OP, AC MSDS)."
```

## Definitions group coverage

Reference this group by using

```json
{"$ref":"#/definitions/coverage#/definitions/coverage"}
```

| Property                                                  | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                      |
| :-------------------------------------------------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [spatial](#spatial)                                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage.md "#/properties/coverage/spatial#/definitions/coverage/properties/spatial")                                                |
| [typicalAgeRange](#typicalagerange)                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range.md "#/properties/coverage/typicalAgeRange#/definitions/coverage/properties/typicalAgeRange")                                          |
| [physicalSampleAvailability](#physicalsampleavailability) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability.md "#/properties/coverage/physicalSampleAvailability#/definitions/coverage/properties/physicalSampleAvailability") |
| [followup](#followup)                                     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup.md "#/properties/coverage/followup#/definitions/coverage/properties/followup")                                                         |
| [pathway](#pathway)                                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway.md "#/properties/coverage/pathway#/definitions/coverage/properties/pathway")                                                            |

### spatial

The geographical area covered by the dataset. It is recommended that links are to entries in a well-maintained gazetteer such as <https://www.geonames.org/> or <https://what3words.com/daring.lion.race>.

> dct:spatial

`spatial`

*   is optional

*   Type: merged type ([Geographic Coverage](dataset-definitions-coverage-properties-geographic-coverage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage.md "#/properties/coverage/spatial#/definitions/coverage/properties/spatial")

#### spatial Type

merged type ([Geographic Coverage](dataset-definitions-coverage-properties-geographic-coverage.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage-anyof-1.md "check type definition")

#### spatial Examples

```json
"https://www.geonames.org/2635167/united-kingdom-of-great-britain-and-northern-ireland.html"
```

### typicalAgeRange

Please indicate the age range in whole years of participants in the dataset. Please provide range in the following format ‘\[min age] – \[max age]’ where both the minimum and maximum are whole numbers (integers).

> <https://schema.org/typicalAgeRange>

`typicalAgeRange`

*   is optional

*   Type: merged type ([Age Range](dataset-definitions-coverage-properties-age-range.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range.md "#/properties/coverage/typicalAgeRange#/definitions/coverage/properties/typicalAgeRange")

#### typicalAgeRange Type

merged type ([Age Range](dataset-definitions-coverage-properties-age-range.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range-allof-0.md "check type definition")

### physicalSampleAvailability

Availability of physical samples associated with the dataset. If samples are available, please indicate the types of samples that are available. More than one type may be provided. If sample are not yet available, please provide “AVAILABILITY TO BE CONFIRMED”. If samples are not available, then please provide “NOT AVAILABLE”.

> No standard identified. Used enumeration from the UK Tissue Directory.

`physicalSampleAvailability`

*   is optional

*   Type: merged type ([Physical Sample Availability](dataset-definitions-coverage-properties-physical-sample-availability.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability.md "#/properties/coverage/physicalSampleAvailability#/definitions/coverage/properties/physicalSampleAvailability")

#### physicalSampleAvailability Type

merged type ([Physical Sample Availability](dataset-definitions-coverage-properties-physical-sample-availability.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability-anyof-1.md "check type definition")

#### physicalSampleAvailability Examples

```json
"BONE MARROW"
```

### followup

If known, what is the typical time span that a patient appears in the dataset (follow up period)

> No standard identified

`followup`

*   is optional

*   Type: merged type ([Followup](dataset-definitions-coverage-properties-followup.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup.md "#/properties/coverage/followup#/definitions/coverage/properties/followup")

#### followup Type

merged type ([Followup](dataset-definitions-coverage-properties-followup.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup-allof-0.md "check type definition")

#### followup Default Value

The default value is:

```json
"UNKNOWN"
```

### pathway

Please indicate if the dataset is representative of the patient pathway and any limitations the dataset may have with respect to pathway coverage. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tiers (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.

> No standard identified

`pathway`

*   is optional

*   Type: merged type ([Pathway](dataset-definitions-coverage-properties-pathway.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway.md "#/properties/coverage/pathway#/definitions/coverage/properties/pathway")

#### pathway Type

merged type ([Pathway](dataset-definitions-coverage-properties-pathway.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway-allof-0.md "check type definition")

## Definitions group provenance

Reference this group by using

```json
{"$ref":"#/definitions/provenance#/definitions/provenance"}
```

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                                                     |
| :-------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [origin](#origin)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin.md "#/definitions/provenance/origin#/definitions/provenance/properties/origin")       |
| [temporal](#temporal) | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal.md "#/definitions/provenance/temporal#/definitions/provenance/properties/temporal") |

### origin



`origin`

*   is optional

*   Type: merged type ([Details](dataset-definitions-provenance-properties-origin.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin.md "#/definitions/provenance/origin#/definitions/provenance/properties/origin")

#### origin Type

merged type ([Details](dataset-definitions-provenance-properties-origin.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin-allof-0.md "check type definition")

### temporal



`temporal`

*   is required

*   Type: merged type ([Details](dataset-definitions-provenance-properties-temporal.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal.md "#/definitions/provenance/temporal#/definitions/provenance/properties/temporal")

#### temporal Type

merged type ([Details](dataset-definitions-provenance-properties-temporal.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal-allof-0.md "check type definition")

## Definitions group origin

Reference this group by using

```json
{"$ref":"#/definitions/origin#/definitions/origin"}
```

| Property                                    | Type   | Required | Nullable       | Defined by                                                                                                                                                                        |
| :------------------------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [purpose](#purpose)                         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose.md "#/properties/provenance/origin/purpose#/definitions/origin/properties/purpose")                         |
| [source](#source)                           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-source.md "#/properties/provenance/origin/source#/definitions/origin/properties/source")                            |
| [collectionSituation](#collectionsituation) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-origin-properties-setting.md "#/properties/provenance/origin/collectionSituation#/definitions/origin/properties/collectionSituation") |

### purpose

Pleases indicate the purpose(s) that the dataset was collected.

> <https://ddialliance.org/Specification/DDI-Lifecycle/3.3/XMLSchema/FieldLevelDocumentation/>

`purpose`

*   is optional

*   Type: merged type ([Purpose](dataset-definitions-origin-properties-purpose.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose.md "#/properties/provenance/origin/purpose#/definitions/origin/properties/purpose")

#### purpose Type

merged type ([Purpose](dataset-definitions-origin-properties-purpose.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-purpose-anyof-1.md "check type definition")

### source

Pleases indicate the source of the data extraction

> <https://dublincore.org/specifications/dublin-core/dcmi-terms/#source>

`source`

*   is optional

*   Type: merged type ([Source](dataset-definitions-origin-properties-source.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-source.md "#/properties/provenance/origin/source#/definitions/origin/properties/source")

#### source Type

merged type ([Source](dataset-definitions-origin-properties-source.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-source-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-source-anyof-1.md "check type definition")

### collectionSituation

Pleases indicate the setting(s) where data was collected. Multiple settings may be provided

> <https://ddialliance.org/Specification/DDI-Lifecycle/3.2/XMLSchema/FieldLevelDocumentation/>

`collectionSituation`

*   is optional

*   Type: merged type ([Setting](dataset-definitions-origin-properties-setting.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-origin-properties-setting.md "#/properties/provenance/origin/collectionSituation#/definitions/origin/properties/collectionSituation")

#### collectionSituation Type

merged type ([Setting](dataset-definitions-origin-properties-setting.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-origin-properties-setting-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-origin-properties-setting-anyof-1.md "check type definition")

## Definitions group temporal

Reference this group by using

```json
{"$ref":"#/definitions/temporal#/definitions/temporal"}
```

| Property                                            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                           |
| :-------------------------------------------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [accrualPeriodicity](#accrualperiodicity)           | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity.md "#/properties/provenance/temporal/accrualPeriodicity#/definitions/temporal/properties/accrualPeriodicity")            |
| [distributionReleaseDate](#distributionreleasedate) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date.md "#/properties/provenance/temporal/distributionReleaseDate#/definitions/temporal/properties/distributionReleaseDate") |
| [startDate](#startdate)                             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date.md "#/properties/provenance/temporal/startDate#/definitions/temporal/properties/startDate")                               |
| [endDate](#enddate)                                 | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date.md "#/properties/provenance/temporal/endDate#/definitions/temporal/properties/endDate")                                     |
| [timeLag](#timelag)                                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag.md "#/properties/provenance/temporal/timeLag#/definitions/temporal/properties/timeLag")                                     |

### accrualPeriodicity

Please indicate the frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity. If a dataset has been published and will remain static please indicate that it is static and indicated when it was released. If a dataset is released on an irregular basis or “on-demand” please indicate that it is Irregular and leave release date as null. If a dataset can be published in real-time or near-real-time please indicate that it is continuous and leave release date as null. Notes: see <https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/>

> dct:accrualPeriodicity

`accrualPeriodicity`

*   is required

*   Type: merged type ([Periodicity](dataset-definitions-temporal-properties-periodicity.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity.md "#/properties/provenance/temporal/accrualPeriodicity#/definitions/temporal/properties/accrualPeriodicity")

#### accrualPeriodicity Type

merged type ([Periodicity](dataset-definitions-temporal-properties-periodicity.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity-allof-0.md "check type definition")

### distributionReleaseDate

Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity. If this is Irregular or Continuously released please leave this blank. Notes: Periodicity and release date will be used to determine when the next release is expected. E.g. if the release date is documented as 01/01/2020 and it is now 20/04/2020 and there is a quarterly release schedule, the latest release will be calculated as 01/04/2020.

> dcat:distribution_release_date

`distributionReleaseDate`

*   is optional

*   Type: merged type ([Release Date](dataset-definitions-temporal-properties-release-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date.md "#/properties/provenance/temporal/distributionReleaseDate#/definitions/temporal/properties/distributionReleaseDate")

#### distributionReleaseDate Type

merged type ([Release Date](dataset-definitions-temporal-properties-release-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-1.md "check type definition")

### startDate

The start of the time period that the dataset provides coverage for. If there are multiple cohorts in the dataset with varying start dates, please provide the earliest date and use the description or the media attribute to provide more information.

> dcat:startDate

`startDate`

*   is required

*   Type: merged type ([Start Date](dataset-definitions-temporal-properties-start-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date.md "#/properties/provenance/temporal/startDate#/definitions/temporal/properties/startDate")

#### startDate Type

merged type ([Start Date](dataset-definitions-temporal-properties-start-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date-anyof-1.md "check type definition")

### endDate

The end of the time period that the dataset provides coverage for. If the dataset is “Continuous” and has no known end date, please state continuous. If there are multiple cohorts in the dataset with varying end dates, please provide the latest date and use the description or the media attribute to provide more information.

> dcat:endDate

`endDate`

*   is optional

*   Type: merged type ([End Date](dataset-definitions-temporal-properties-end-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date.md "#/properties/provenance/temporal/endDate#/definitions/temporal/properties/endDate")

#### endDate Type

merged type ([End Date](dataset-definitions-temporal-properties-end-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-1.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-2.md "check type definition")

### timeLag

Please indicate the typical time-lag between an event and the data for that event appearing in the dataset

> No standard identified

`timeLag`

*   is required

*   Type: merged type ([Time Lag](dataset-definitions-temporal-properties-time-lag.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag.md "#/properties/provenance/temporal/timeLag#/definitions/temporal/properties/timeLag")

#### timeLag Type

merged type ([Time Lag](dataset-definitions-temporal-properties-time-lag.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag-allof-0.md "check type definition")

## Definitions group accessibility

Reference this group by using

```json
{"$ref":"#/definitions/accessibility#/definitions/accessibility"}
```

| Property                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :---------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [usage](#usage)                           | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-usage.md "#/definitions/accessibility/usage#/definitions/accessibility/properties/usage")                                          |
| [access](#access)                         | Not specified | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-access.md "#/definitions/accessibility/access#/definitions/accessibility/properties/access")                                       |
| [formatAndStandards](#formatandstandards) | Not specified | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-format-and-standards.md "#/definitions/accessibility/formatAndStandards#/definitions/accessibility/properties/formatAndStandards") |

### usage

This section includes information about how the data can be used and how it is currently being used

`usage`

*   is optional

*   Type: unknown ([Usage](dataset-definitions-accessibility-properties-usage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-usage.md "#/definitions/accessibility/usage#/definitions/accessibility/properties/usage")

#### usage Type

unknown ([Usage](dataset-definitions-accessibility-properties-usage.md))

### access

This section includes information about data access

`access`

*   is required

*   Type: unknown ([Access](dataset-definitions-accessibility-properties-access.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-access.md "#/definitions/accessibility/access#/definitions/accessibility/properties/access")

#### access Type

unknown ([Access](dataset-definitions-accessibility-properties-access.md))

### formatAndStandards

Section includes technical attributes for language vocabularies, sizes etc. and gives researchers facts about and processing the underlying data in the dataset.

`formatAndStandards`

*   is optional

*   Type: unknown ([Format and Standards](dataset-definitions-accessibility-properties-format-and-standards.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-accessibility-properties-format-and-standards.md "#/definitions/accessibility/formatAndStandards#/definitions/accessibility/properties/formatAndStandards")

#### formatAndStandards Type

unknown ([Format and Standards](dataset-definitions-accessibility-properties-format-and-standards.md))

## Definitions group usage

Reference this group by using

```json
{"$ref":"#/definitions/usage#/definitions/usage"}
```

| Property                                      | Type   | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :-------------------------------------------- | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [dataUseLimitation](#datauselimitation-1)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation.md "#/properties/accessibility/usage/dataUseLimitation#/definitions/usage/properties/dataUseLimitation")       |
| [dataUseRequirements](#datauserequirements-1) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements.md "#/properties/accessibility/usage/dataUseRequirements#/definitions/usage/properties/dataUseRequirements") |
| [resourceCreator](#resourcecreator)           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements.md "#/properties/accessibility/usage/resourceCreator#/definitions/usage/properties/resourceCreator")         |
| [investigations](#investigations)             | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations.md "#/definitions/usage#/definitions/usage/properties/investigations")                                              |
| [isReferencedBy](#isreferencedby)             | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-usage-properties-citations.md "#/definitions/usage#/definitions/usage/properties/isReferencedBy")                                                   |

### dataUseLimitation

Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. NOTE: we have extended the DUO to include a value for NO LINKAGE

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseLimitation`

*   is optional

*   Type: merged type ([Data Use Limitation](dataset-definitions-usage-properties-data-use-limitation.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation.md "#/properties/accessibility/usage/dataUseLimitation#/definitions/usage/properties/dataUseLimitation")

#### dataUseLimitation Type

merged type ([Data Use Limitation](dataset-definitions-usage-properties-data-use-limitation.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-limitation-anyof-1.md "check type definition")

### dataUseRequirements

Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseRequirements`

*   is optional

*   Type: merged type ([Data Use Requirements](dataset-definitions-usage-properties-data-use-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements.md "#/properties/accessibility/usage/dataUseRequirements#/definitions/usage/properties/dataUseRequirements")

#### dataUseRequirements Type

merged type ([Data Use Requirements](dataset-definitions-usage-properties-data-use-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-data-use-requirements-anyof-1.md "check type definition")

### resourceCreator

Please provide the text that you would like included as part of any citation that credits this dataset. This is typically just the name of the publisher.   No employee details should be provided.

> dct:creator

`resourceCreator`

*   is optional

*   Type: merged type ([Citation Requirements](dataset-definitions-usage-properties-citation-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements.md "#/properties/accessibility/usage/resourceCreator#/definitions/usage/properties/resourceCreator")

#### resourceCreator Type

merged type ([Citation Requirements](dataset-definitions-usage-properties-citation-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-citation-requirements-anyof-1.md "check type definition")

### investigations



> No standard identified

`investigations`

*   is optional

*   Type: merged type ([Investigations](dataset-definitions-usage-properties-investigations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations.md "#/definitions/usage#/definitions/usage/properties/investigations")

#### investigations Type

merged type ([Investigations](dataset-definitions-usage-properties-investigations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-investigations-anyof-1.md "check type definition")

### isReferencedBy

Please provide the keystone paper associated with the dataset. Also include a list of known citations, if available and should be links to existing resources where the dataset has been used or referenced. Please provide multiple entries, or if you are using a csv upload please provide them as a tab separated list.

> dct:isReferencedBy

`isReferencedBy`

*   is optional

*   Type: merged type ([Citations](dataset-definitions-usage-properties-citations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-usage-properties-citations.md "#/definitions/usage#/definitions/usage/properties/isReferencedBy")

#### isReferencedBy Type

merged type ([Citations](dataset-definitions-usage-properties-citations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-usage-properties-citations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-usage-properties-citations-anyof-1.md "check type definition")

## Definitions group access

Reference this group by using

```json
{"$ref":"#/definitions/access#/definitions/access"}
```

| Property                                  | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :---------------------------------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [accessRights](#accessrights-1)           | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights.md "#/properties/accessibility/access/accessRights#/definitions/access/properties/accessRights")                              |
| [accessService](#accessservice-1)         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-service.md "#/properties/accessibility/access/accessService#/definitions/access/properties/accessService")                           |
| [accessRequestCost](#accessrequestcost-1) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost.md "#/properties/accessibility/access/accessRequestCost#/definitions/access/properties/accessRequestCost") |
| [deliveryLeadTime](#deliveryleadtime-1)   | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration.md "#/properties/accessibility/access/deliveryLeadTime#/definitions/access/properties/deliveryLeadTime")            |
| [jurisdiction](#jurisdiction)             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction.md "#/properties/accessibility/access/jurisdiction#/definitions/access/properties/jurisdiction")                               |
| [dataController](#datacontroller)         | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller.md "#/properties/accessibility/access/dataController#/definitions/access/properties/dataController")                        |
| [dataProcessor](#dataprocessor)           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor.md "#/properties/accessibility/access/dataProcessor#/definitions/access/properties/dataProcessor")                           |

### accessRights



> dct:access_rights NOTE: need to ensure that this is consistent across the organisation info and the dataset info

`accessRights`

*   is required

*   Type: merged type ([Access Rights](dataset-definitions-access-properties-access-rights.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights.md "#/properties/accessibility/access/accessRights#/definitions/access/properties/accessRights")

#### accessRights Type

merged type ([Access Rights](dataset-definitions-access-properties-access-rights.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-0.md "check type definition")

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-1.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-2.md "check type definition")

### accessService

Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> dcat:accessService

`accessService`

*   is optional

*   Type: merged type ([Access Service](dataset-definitions-access-properties-access-service.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-service.md "#/properties/accessibility/access/accessService#/definitions/access/properties/accessService")

#### accessService Type

merged type ([Access Service](dataset-definitions-access-properties-access-service.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-service-allof-0.md "check type definition")

#### accessService Examples

```json
"https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide"
```

### accessRequestCost

Please provide link(s) to a webpage detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.

> No standard identified

`accessRequestCost`

*   is optional

*   Type: merged type ([Organisation Access Request Cost](dataset-definitions-access-properties-organisation-access-request-cost.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost.md "#/properties/accessibility/access/accessRequestCost#/definitions/access/properties/accessRequestCost")

#### accessRequestCost Type

merged type ([Organisation Access Request Cost](dataset-definitions-access-properties-organisation-access-request-cost.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost-anyof-1.md "check type definition")

### deliveryLeadTime

Please provide an indication of the typical processing times based on the types of requests typically received.

> <https://schema.org/deliveryLeadTime>

`deliveryLeadTime`

*   is optional

*   Type: merged type ([Access Request Duration](dataset-definitions-access-properties-access-request-duration.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration.md "#/properties/accessibility/access/deliveryLeadTime#/definitions/access/properties/deliveryLeadTime")

#### deliveryLeadTime Type

merged type ([Access Request Duration](dataset-definitions-access-properties-access-request-duration.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration-allof-0.md "check type definition")

### jurisdiction

Please use country code from ISO 3166-1 country codes and the associated ISO 3166-2 for regions, cities, states etc. for the country/state under whose laws the data subjects’ data is collected, processed and stored.

> <http://purl.org/dc/terms/Jurisdiction> FIXME: Add ISO 3166-2 Subdivision code pattern

`jurisdiction`

*   is required

*   Type: merged type ([Jurisdiction](dataset-definitions-access-properties-jurisdiction.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction.md "#/properties/accessibility/access/jurisdiction#/definitions/access/properties/jurisdiction")

#### jurisdiction Type

merged type ([Jurisdiction](dataset-definitions-access-properties-jurisdiction.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction-anyof-1.md "check type definition")

#### jurisdiction Default Value

The default value is:

```json
"GB-ENG"
```

### dataController

Data Controller means a person/entity who (either alone or jointly or in common with other persons/entities) determines the purposes for which and the way any Data Subject data, specifically personal data or are to be processed.

> dpv:DataController

`dataController`

*   is required

*   Type: merged type ([Data Controller](dataset-definitions-access-properties-data-controller.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller.md "#/properties/accessibility/access/dataController#/definitions/access/properties/dataController")

#### dataController Type

merged type ([Data Controller](dataset-definitions-access-properties-data-controller.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller-allof-0.md "check type definition")

### dataProcessor

A Data Processor, in relation to any Data Subject data, specifically personal data, means any person/entity (other than an employee of the data controller) who processes the data on behalf of the data controller.

> dpv:DataProcessor

`dataProcessor`

*   is optional

*   Type: merged type ([Data Processor](dataset-definitions-access-properties-data-processor.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor.md "#/properties/accessibility/access/dataProcessor#/definitions/access/properties/dataProcessor")

#### dataProcessor Type

merged type ([Data Processor](dataset-definitions-access-properties-data-processor.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor-allof-0.md "check type definition")

## Definitions group formatAndStandards

Reference this group by using

```json
{"$ref":"#/definitions/formatAndStandards#/definitions/formatAndStandards"}
```

| Property                                              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :---------------------------------------------------- | :----- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [vocabularyEncodingScheme](#vocabularyencodingscheme) | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md "#/properties/accessibility/formatAndStandards/vocabularyEncodingScheme#/definitions/formatAndStandards/properties/vocabularyEncodingScheme") |
| [conformsTo](#conformsto)                             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to.md "#/properties/accessibility/formatAndStandards/conformsTo#/definitions/formatAndStandards/properties/conformsTo")                                       |
| [language](#language)                                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language.md "#/properties/accessibility/formatAndStandards/language#/definitions/formatAndStandards/properties/language")                                              |
| [format](#format)                                     | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format.md "#/properties/accessibility/formatAndStandards/format#/definitions/formatAndStandards/properties/format")                                                    |

### vocabularyEncodingScheme

List any relevant terminologies / ontologies / controlled vocabularies, such as ICD 10 Codes, NHS Data Dictionary National Codes or SNOMED CT International, that are being used by the dataset. If the controlled vocabularies are local standards, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition. Notes: More than one vocabulary may be provided.

> <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/dcam/VocabularyEncodingScheme>

`vocabularyEncodingScheme`

*   is required

*   Type: merged type ([Controlled Vocabulary](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md "#/properties/accessibility/formatAndStandards/vocabularyEncodingScheme#/definitions/formatAndStandards/properties/vocabularyEncodingScheme")

#### vocabularyEncodingScheme Type

merged type ([Controlled Vocabulary](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary-anyof-1.md "check type definition")

#### vocabularyEncodingScheme Default Value

The default value is:

```json
"LOCAL"
```

### conformsTo

List standardised data models that the dataset has been stored in or transformed to, such as OMOP or FHIR. If the data is only available in a local format, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition.

> dct:conformsTo

`conformsTo`

*   is required

*   Type: merged type ([Conforms To](dataset-definitions-formatandstandards-properties-conforms-to.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to.md "#/properties/accessibility/formatAndStandards/conformsTo#/definitions/formatAndStandards/properties/conformsTo")

#### conformsTo Type

merged type ([Conforms To](dataset-definitions-formatandstandards-properties-conforms-to.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to-anyof-1.md "check type definition")

#### conformsTo Default Value

The default value is:

```json
"LOCAL"
```

### language

This should list all the languages in which the dataset metadata and underlying data is made available.

> dct:language. FIXME: Conforms to spec, but may be a list of strings given cardinality 1:\*. Validate against external list of languages. Resources defined by the Library of Congress (ISO 639-1, ISO 639-2) SHOULD be used.

`language`

*   is required

*   Type: merged type ([Language](dataset-definitions-formatandstandards-properties-language.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language.md "#/properties/accessibility/formatAndStandards/language#/definitions/formatAndStandards/properties/language")

#### language Type

merged type ([Language](dataset-definitions-formatandstandards-properties-language.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-1.md "check type definition")

#### language Default Value

The default value is:

```json
"en"
```

### format

If multiple formats are available please specify. See application, audio, image, message, model, multipart, text, video, <https://www.iana.org/assignments/media-types/media-types.xhtml> Note: If your file format is not included in the current list of formats, please indicate other. If you are using the HOP you will be directed to a service desk page where you can request your additional format. If not please go to: <https://metadata.atlassian.net/servicedesk/customer/portal/4> to request your format.

> <http://purl.org/dc/terms/format>

`format`

*   is required

*   Type: merged type ([Format](dataset-definitions-formatandstandards-properties-format.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format.md "#/properties/accessibility/formatAndStandards/format#/definitions/formatAndStandards/properties/format")

#### format Type

merged type ([Format](dataset-definitions-formatandstandards-properties-format.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format-anyof-1.md "check type definition")

## Definitions group enrichmentAndLinkage

Reference this group by using

```json
{"$ref":"#/definitions/enrichmentAndLinkage#/definitions/enrichmentAndLinkage"}
```

| Property                                | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                           |
| :-------------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [qualifiedRelation](#qualifiedrelation) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md "#/properties/enrichmentAndLinkage/qualifiedRelation#/definitions/enrichmentAndLinkage/properties/qualifiedRelation") |
| [derivation](#derivation)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations.md "#/definitions/enrichmentAndLinkage#/definitions/enrichmentAndLinkage/properties/derivation")                             |
| [tools](#tools)                         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools.md "#/properties/enrichmentAndLinkage/tools#/definitions/enrichmentAndLinkage/properties/tools")                                   |

### qualifiedRelation

If applicable, please provide the DOI of other datasets that have previously been linked to this dataset and their availability. If no DOI is available, please provide the title of the datasets that can be linked, where possible using the same title of a dataset previously onboarded to the HOP. Note: If all the datasets from Gateway organisation can be linked please indicate “ALL” and the onboarding portal will automate linkage across the datasets submitted.

> dcat:qualifiedRelation

`qualifiedRelation`

*   is optional

*   Type: merged type ([Linked Datasets](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md "#/properties/enrichmentAndLinkage/qualifiedRelation#/definitions/enrichmentAndLinkage/properties/qualifiedRelation")

#### qualifiedRelation Type

merged type ([Linked Datasets](dataset-definitions-enrichmentandlinkage-properties-linked-datasets.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-linked-datasets-anyof-1.md "check type definition")

### derivation

Indicate if derived datasets or predefined extracts are available and the type of derivation available. Notes. Single or multiple dimensions can be provided as a derived extract alongside the dataset.

> prov:Derivation

`derivation`

*   is optional

*   Type: merged type ([Derivations](dataset-definitions-enrichmentandlinkage-properties-derivations.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations.md "#/definitions/enrichmentAndLinkage#/definitions/enrichmentAndLinkage/properties/derivation")

#### derivation Type

merged type ([Derivations](dataset-definitions-enrichmentandlinkage-properties-derivations.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-derivations-anyof-1.md "check type definition")

### tools

Please provide the URL of any analysis tools or models that have been created for this dataset and are available for further use. Multiple tools may be provided. Note: We encourage users to adopt a model along the lines of <https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/>

> No standard identified. We encourage users to adopt a model along the lines of <https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/>

`tools`

*   is optional

*   Type: merged type ([Tools](dataset-definitions-enrichmentandlinkage-properties-tools.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools.md "#/properties/enrichmentAndLinkage/tools#/definitions/enrichmentAndLinkage/properties/tools")

#### tools Type

merged type ([Tools](dataset-definitions-enrichmentandlinkage-properties-tools.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-enrichmentandlinkage-properties-tools-anyof-1.md "check type definition")

## Definitions group observation

Reference this group by using

```json
{"$ref":"#/definitions/observation#/definitions/observation"}
```

| Property                                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                           |
| :------------------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [observedNode](#observednode)                           | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population.md "#/properties/observation/observedNode#/definitions/observation/properties/observedNode")                               |
| [measuredValue](#measuredvalue)                         | `integer` | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-value.md "#/properties/observation/measuredValue#/definitions/observation/properties/measuredValue")                                     |
| [disambiguatingDescription](#disambiguatingdescription) | Merged    | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description.md "#/properties/observation/disambiguatingDescription#/definitions/observation/properties/disambiguatingDescription") |
| [observationDate](#observationdate)                     | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date.md "#/properties/observation/observationDate#/definitions/observation/properties/observationDate")                               |
| [measuredProperty](#measuredproperty)                   | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property.md "#/properties/observation/measuredProperty#/definitions/observation/properties/measuredProperty")                            |

### observedNode

Please select one of the following statistical populations for you observation

> <https://schema.org/observedNode>

`observedNode`

*   is required

*   Type: merged type ([Statistical Population](dataset-definitions-observation-properties-statistical-population.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population.md "#/properties/observation/observedNode#/definitions/observation/properties/observedNode")

#### observedNode Type

merged type ([Statistical Population](dataset-definitions-observation-properties-statistical-population.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population-allof-0.md "check type definition")

#### observedNode Examples

```json
"PERSONS"
```

### measuredValue

Please provide the population size associated with the population type the dataset i.e. 1000 people in a study, or 87 images (MRI) of Knee Usage Note: Used with Statistical Population, which specifies the type of the population in the dataset.

> <https://schema.org/measuredValue>

`measuredValue`

*   is required

*   Type: `integer` ([Measured Value](dataset-definitions-observation-properties-measured-value.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-value.md "#/properties/observation/measuredValue#/definitions/observation/properties/measuredValue")

#### measuredValue Type

`integer` ([Measured Value](dataset-definitions-observation-properties-measured-value.md))

### disambiguatingDescription

If SNOMED CT term does not provide sufficient detail, please provide a description that disambiguates the population type.

> <https://schema.org/disambiguatingDescription>

`disambiguatingDescription`

*   is optional

*   Type: merged type ([Disambiguating Description](dataset-definitions-observation-properties-disambiguating-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description.md "#/properties/observation/disambiguatingDescription#/definitions/observation/properties/disambiguatingDescription")

#### disambiguatingDescription Type

merged type ([Disambiguating Description](dataset-definitions-observation-properties-disambiguating-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description-allof-0.md "check type definition")

### observationDate

Please provide the date that the observation was made. Some datasets may be continuously updated and the number of records will change regularly, so the observation date provides users with the date that the analysis or query was run to generate the particular observation. Multiple observations can be made i.e. an observation of cumulative COVID positive cases by specimen on the 1/1/2021 could be 2M. On the 8/1/2021 a new observation could be 2.1M. Users can add multiple observations.

> <https://schema.org/observationDate>

`observationDate`

*   is required

*   Type: merged type ([Observation Date](dataset-definitions-observation-properties-observation-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date.md "#/properties/observation/observationDate#/definitions/observation/properties/observationDate")

#### observationDate Type

merged type ([Observation Date](dataset-definitions-observation-properties-observation-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-1.md "check type definition")

#### observationDate Default Value

The default value is:

```json
"release date"
```

### measuredProperty

Initially this will be defaulted to "COUNT"

> <https://schema.org/measuredProperty>

`measuredProperty`

*   is required

*   Type: merged type ([Measured Property](dataset-definitions-observation-properties-measured-property.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property.md "#/properties/observation/measuredProperty#/definitions/observation/properties/measuredProperty")

#### measuredProperty Type

merged type ([Measured Property](dataset-definitions-observation-properties-measured-property.md))

all of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property-allof-0.md "check type definition")

#### measuredProperty Default Value

The default value is:

```json
"COUNT"
```

## Definitions group uuidv4

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/uuidv4"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group semver

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/semver"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group url

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/url"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group eightyCharacters

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/eightyCharacters"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group abstractText

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/abstractText"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group emailAddress

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/emailAddress"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group shortDescription

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/shortDescription"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group description

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/description"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group longDescription

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/longDescription"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group commaSeparatedValues

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/commaSeparatedValues"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group doi

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/doi"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group ageRange

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/ageRange"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group format

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/format"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group isocountrycode

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/isocountrycode"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group memberOf

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/memberOf"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group physicalSampleAvailability

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/physicalSampleAvailability"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group followup

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/followup"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group periodicity

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/periodicity"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group purpose

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/purpose"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group source

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/source"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group setting

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/setting"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group timeLag

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/timeLag"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group dataUseLimitation

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/dataUseLimitation"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group dataUseRequirements

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/dataUseRequirements"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group deliveryLeadTime

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/deliveryLeadTime"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group standardisedDataModels

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/standardisedDataModels"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group controlledVocabulary

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/controlledVocabulary"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group language

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/language"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group statisticalPopulationConstrained

Reference this group by using

```json
{"$ref":"https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json#/definitions/statisticalPopulationConstrained"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
