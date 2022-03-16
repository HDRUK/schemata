# Summary Schema

```txt
#/definitions/summary#/properties/summary
```

Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## summary Type

unknown ([Summary](dataset-properties-summary.md))

# summary Properties

| Property                                      | Type   | Required | Nullable       | Defined by                                                                                                                                                                             |
| :-------------------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [title](#title)                               | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-title.md "#/summary/title#/definitions/summary/properties/title")                                                       |
| [abstract](#abstract)                         | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract.md "#/summary/abstract#/definitions/summary/properties/abstract")                                      |
| [publisher](#publisher)                       | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher.md "#/summary/publisher#/definitions/summary/properties/publisher")                                   |
| [contactPoint](#contactpoint)                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point.md "#/summary/contactPoint#/definitions/summary/properties/contactPoint")                                 |
| [keywords](#keywords)                         | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords.md "#/summary/keywords#/definitions/summary/properties/keywords")                                              |
| [alternateIdentifiers](#alternateidentifiers) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers.md "#/summary/alternateIdentifiers#/definitions/summary/properties/alternateIdentifiers") |
| [doiName](#doiname)                           | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier.md "#/summary/doiName#/definitions/summary/properties/doiName")                               |

## title

Title of the dataset limited to 80 characters. It should provide a short description of the dataset and be unique across the gateway. If your title is not unique, please add a prefix with your organisation name or identifier to differentiate it from other datasets within the Gateway. Please avoid acronyms wherever possible. Good titles should summarise the content of the dataset and if relevant, the region the dataset covers.

> dct:title. title is reserved word in json schema

`title`

*   is required

*   Type: merged type ([Title](dataset-definitions-summary-properties-title.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-title.md "#/summary/title#/definitions/summary/properties/title")

### title Type

merged type ([Title](dataset-definitions-summary-properties-title.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-title-allof-0.md "check type definition")

### title Examples

```json
[
  "North West London COVID-19 Patient Level Situation Report"
]
```

## abstract

Provide a clear and brief descriptive signpost for researchers who are searching for data that may be relevant to their research. The abstract should allow the reader to determine the scope of the data collection and accurately summarise its content. The optimal length is one paragraph (limited to 255 characters) and effective abstracts should avoid long sentences and abbreviations where possible

> dct:abstract

`abstract`

*   is required

*   Type: merged type ([Dataset Abstract](dataset-definitions-summary-properties-dataset-abstract.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract.md "#/summary/abstract#/definitions/summary/properties/abstract")

### abstract Type

merged type ([Dataset Abstract](dataset-definitions-summary-properties-dataset-abstract.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-abstract-allof-0.md "check type definition")

### abstract Examples

```json
"CPRD Aurum contains primary care data contributed by General Practitioner (GP) practices using EMIS Web® including patient registration information and all care events that GPs have chosen to record as part of their usual medical practice."
```

## publisher

This is the organisation responsible for running or supporting the data access request process, as well as publishing and maintaining the metadata. In most this will be the same as the HDR UK Organisation (Hub or Alliance Member). However, in some cases this will be different i.e. Tissue Directory are an HDR UK Gateway organisation but coordinate activities across a number of data publishers i.e. Cambridge Blood and Stem Cell Biobank.

> Conforms to spec, but this MAY be an an object of organisation. <https://schema.org/publisher>

`publisher`

*   is required

*   Type: merged type ([Dataset publisher](dataset-definitions-summary-properties-dataset-publisher.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher.md "#/summary/publisher#/definitions/summary/properties/publisher")

### publisher Type

merged type ([Dataset publisher](dataset-definitions-summary-properties-dataset-publisher.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-dataset-publisher-allof-0.md "check type definition")

## contactPoint

Please provide a valid email address that can be used to coordinate data access requests with the publisher. Organisations are expected to provide a dedicated email address associated with the data access request process. Notes- An employee's email address can only be provided on a temporary basis and if one is provided an explicit consent must be obtained for this purpose.

> dcat:contactPoint

`contactPoint`

*   is required

*   Type: merged type ([Contact Point](dataset-definitions-summary-properties-contact-point.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point.md "#/summary/contactPoint#/definitions/summary/properties/contactPoint")

### contactPoint Type

merged type ([Contact Point](dataset-definitions-summary-properties-contact-point.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-contact-point-allof-0.md "check type definition")

### contactPoint Default Value

The default value is:

```json
"Defaulted to the contact point of the primary organisation of the user however, can be overridden for specific datasets"
```

### contactPoint Examples

```json
"SAILDatabank@swansea.ac.uk"
```

## keywords

Please provide relevant and specific keywords that can improve the SEO of your dataset as a comma separated list. Notes: Onboarding portal will suggest keywords based on title, abstract and description. We are compiling a standardised list of keywords and synonyms across datasets to make filtering easier for users.

> dcat:keyword. May be an array of strings or comma seperated list.

`keywords`

*   is required

*   Type: merged type ([Keywords](dataset-definitions-summary-properties-keywords.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords.md "#/summary/keywords#/definitions/summary/properties/keywords")

### keywords Type

merged type ([Keywords](dataset-definitions-summary-properties-keywords.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-summary-properties-keywords-anyof-1.md "check type definition")

## alternateIdentifiers

Alternate dataset identifiers or local identifiers

> DATA-CITE alternate-identifiers used. Note, will support comma separated list for backwards compatibility with other systems

`alternateIdentifiers`

*   is optional

*   Type: merged type ([Alternate dataset identifiers](dataset-definitions-summary-properties-alternate-dataset-identifiers.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers.md "#/summary/alternateIdentifiers#/definitions/summary/properties/alternateIdentifiers")

### alternateIdentifiers Type

merged type ([Alternate dataset identifiers](dataset-definitions-summary-properties-alternate-dataset-identifiers.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-summary-properties-alternate-dataset-identifiers-anyof-1.md "check type definition")

## doiName

All HDR UK registered datasets should either have a Digital Object Identifier (DOI) or be working towards obtaining one. If a DOI is available, please provide the DOI.

> Vocabulary: DOI Data Dictionary

`doiName`

*   is optional

*   Type: merged type ([Digital Object Identifier](dataset-definitions-summary-properties-digital-object-identifier.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier.md "#/summary/doiName#/definitions/summary/properties/doiName")

### doiName Type

merged type ([Digital Object Identifier](dataset-definitions-summary-properties-digital-object-identifier.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-summary-properties-digital-object-identifier-allof-0.md "check type definition")

### doiName Examples

```json
"10.3399/bjgp17X692645"
```
