# Release Date Schema

```txt
#/properties/provenance/temporal/distributionReleaseDate#/definitions/temporal/properties/distributionReleaseDate
```

Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity. If this is Irregular or Continuously released please leave this blank. Notes: Periodicity and release date will be used to determine when the next release is expected. E.g. if the release date is documented as 01/01/2020 and it is now 20/04/2020 and there is a quarterly release schedule, the latest release will be calculated as 01/04/2020.

> dcat:distribution_release_date

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## distributionReleaseDate Type

merged type ([Release Date](dataset-definitions-temporal-properties-release-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-temporal-properties-release-date-anyof-1.md "check type definition")
