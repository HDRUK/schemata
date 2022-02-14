# Coverage Schema

```txt
#/definitions/coverage#/properties/coverage
```

This information includes attributes for geographical and temporal coverage, cohort details etc. to enable a deeper understanding of the dataset content so that researchers can make decisions about the relevance of the underlying data.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## coverage Type

unknown ([Coverage](dataset-properties-coverage.md))

# coverage Properties

| Property                                                  | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                      |
| :-------------------------------------------------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [spatial](#spatial)                                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage.md "#/properties/coverage/spatial#/definitions/coverage/properties/spatial")                                                |
| [typicalAgeRange](#typicalagerange)                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range.md "#/properties/coverage/typicalAgeRange#/definitions/coverage/properties/typicalAgeRange")                                          |
| [physicalSampleAvailability](#physicalsampleavailability) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability.md "#/properties/coverage/physicalSampleAvailability#/definitions/coverage/properties/physicalSampleAvailability") |
| [followup](#followup)                                     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup.md "#/properties/coverage/followup#/definitions/coverage/properties/followup")                                                         |
| [pathway](#pathway)                                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway.md "#/properties/coverage/pathway#/definitions/coverage/properties/pathway")                                                            |

## spatial

The geographical area covered by the dataset. It is recommended that links are to entries in a well-maintained gazetteer such as <https://www.geonames.org/> or <https://what3words.com/daring.lion.race>.

> dct:spatial

`spatial`

*   is optional

*   Type: merged type ([Geographic Coverage](dataset-definitions-coverage-properties-geographic-coverage.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage.md "#/properties/coverage/spatial#/definitions/coverage/properties/spatial")

### spatial Type

merged type ([Geographic Coverage](dataset-definitions-coverage-properties-geographic-coverage.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-coverage-properties-geographic-coverage-anyof-1.md "check type definition")

### spatial Examples

```json
"https://www.geonames.org/2635167/united-kingdom-of-great-britain-and-northern-ireland.html"
```

## typicalAgeRange

Please indicate the age range in whole years of participants in the dataset. Please provide range in the following format '\[min age] – \[max age]' where both the minimum and maximum are whole numbers (integers).

> <https://schema.org/typicalAgeRange>

`typicalAgeRange`

*   is optional

*   Type: merged type ([Age Range](dataset-definitions-coverage-properties-age-range.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range.md "#/properties/coverage/typicalAgeRange#/definitions/coverage/properties/typicalAgeRange")

### typicalAgeRange Type

merged type ([Age Range](dataset-definitions-coverage-properties-age-range.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-age-range-allof-0.md "check type definition")

## physicalSampleAvailability

Availability of physical samples associated with the dataset. If samples are available, please indicate the types of samples that are available. More than one type may be provided. If sample are not yet available, please provide “AVAILABILITY TO BE CONFIRMED”. If samples are not available, then please provide “NOT AVAILABLE”.

> No standard identified. Used enumeration from the UK Tissue Directory.

`physicalSampleAvailability`

*   is optional

*   Type: merged type ([Physical Sample Availability](dataset-definitions-coverage-properties-physical-sample-availability.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability.md "#/properties/coverage/physicalSampleAvailability#/definitions/coverage/properties/physicalSampleAvailability")

### physicalSampleAvailability Type

merged type ([Physical Sample Availability](dataset-definitions-coverage-properties-physical-sample-availability.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-coverage-properties-physical-sample-availability-anyof-1.md "check type definition")

### physicalSampleAvailability Examples

```json
"BONE MARROW"
```

## followup

If known, what is the typical time span that a patient appears in the dataset (follow up period)

> No standard identified

`followup`

*   is optional

*   Type: merged type ([Followup](dataset-definitions-coverage-properties-followup.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup.md "#/properties/coverage/followup#/definitions/coverage/properties/followup")

### followup Type

merged type ([Followup](dataset-definitions-coverage-properties-followup.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-followup-allof-0.md "check type definition")

### followup Default Value

The default value is:

```json
"UNKNOWN"
```

## pathway

Please indicate if the dataset is representative of the patient pathway and any limitations the dataset may have with respect to pathway coverage. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tiers (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.

> No standard identified

`pathway`

*   is optional

*   Type: merged type ([Pathway](dataset-definitions-coverage-properties-pathway.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway.md "#/properties/coverage/pathway#/definitions/coverage/properties/pathway")

### pathway Type

merged type ([Pathway](dataset-definitions-coverage-properties-pathway.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-coverage-properties-pathway-allof-0.md "check type definition")
