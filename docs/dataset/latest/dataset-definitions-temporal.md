# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/temporal#/definitions/temporal
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## temporal Type

unknown

# temporal Properties

| Property                                            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                           |
| :-------------------------------------------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [accrualPeriodicity](#accrualperiodicity)           | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity.md "#/properties/provenance/temporal/accrualPeriodicity#/definitions/temporal/properties/accrualPeriodicity")            |
| [distributionReleaseDate](#distributionreleasedate) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date.md "#/properties/provenance/temporal/distributionReleaseDate#/definitions/temporal/properties/distributionReleaseDate") |
| [startDate](#startdate)                             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date.md "#/properties/provenance/temporal/startDate#/definitions/temporal/properties/startDate")                               |
| [endDate](#enddate)                                 | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date.md "#/properties/provenance/temporal/endDate#/definitions/temporal/properties/endDate")                                     |
| [timeLag](#timelag)                                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag.md "#/properties/provenance/temporal/timeLag#/definitions/temporal/properties/timeLag")                                     |

## accrualPeriodicity

Please indicate the frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity. If a dataset has been published and will remain static please indicate that it is static and indicated when it was released. If a dataset is released on an irregular basis or “on-demand” please indicate that it is Irregular and leave release date as null. If a dataset can be published in real-time or near-real-time please indicate that it is continuous and leave release date as null. Notes: see <https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/>

> dct:accrualPeriodicity

`accrualPeriodicity`

*   is required

*   Type: merged type ([Periodicity](dataset-definitions-temporal-properties-periodicity.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity.md "#/properties/provenance/temporal/accrualPeriodicity#/definitions/temporal/properties/accrualPeriodicity")

### accrualPeriodicity Type

merged type ([Periodicity](dataset-definitions-temporal-properties-periodicity.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-temporal-properties-periodicity-allof-0.md "check type definition")

## distributionReleaseDate

Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity. If this is Irregular or Continuously released please leave this blank. Notes: Periodicity and release date will be used to determine when the next release is expected. E.g. if the release date is documented as 01/01/2020 and it is now 20/04/2020 and there is a quarterly release schedule, the latest release will be calculated as 01/04/2020.

> dcat:distribution_release_date

`distributionReleaseDate`

*   is optional

*   Type: merged type ([Release Date](dataset-definitions-temporal-properties-release-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date.md "#/properties/provenance/temporal/distributionReleaseDate#/definitions/temporal/properties/distributionReleaseDate")

### distributionReleaseDate Type

merged type ([Release Date](dataset-definitions-temporal-properties-release-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-1.md "check type definition")

## startDate

The start of the time period that the dataset provides coverage for. If there are multiple cohorts in the dataset with varying start dates, please provide the earliest date and use the description or the media attribute to provide more information.

> dcat:startDate

`startDate`

*   is required

*   Type: merged type ([Start Date](dataset-definitions-temporal-properties-start-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date.md "#/properties/provenance/temporal/startDate#/definitions/temporal/properties/startDate")

### startDate Type

merged type ([Start Date](dataset-definitions-temporal-properties-start-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-start-date-anyof-1.md "check type definition")

## endDate

The end of the time period that the dataset provides coverage for. If the dataset is “Continuous” and has no known end date, please state continuous. If there are multiple cohorts in the dataset with varying end dates, please provide the latest date and use the description or the media attribute to provide more information.

> dcat:endDate

`endDate`

*   is optional

*   Type: merged type ([End Date](dataset-definitions-temporal-properties-end-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date.md "#/properties/provenance/temporal/endDate#/definitions/temporal/properties/endDate")

### endDate Type

merged type ([End Date](dataset-definitions-temporal-properties-end-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-1.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-end-date-anyof-2.md "check type definition")

## timeLag

Please indicate the typical time-lag between an event and the data for that event appearing in the dataset

> No standard identified

`timeLag`

*   is required

*   Type: merged type ([Time Lag](dataset-definitions-temporal-properties-time-lag.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag.md "#/properties/provenance/temporal/timeLag#/definitions/temporal/properties/timeLag")

### timeLag Type

merged type ([Time Lag](dataset-definitions-temporal-properties-time-lag.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-temporal-properties-time-lag-allof-0.md "check type definition")
