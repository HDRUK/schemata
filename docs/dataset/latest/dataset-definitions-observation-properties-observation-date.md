# Observation Date Schema

```txt
#/properties/observation/observationDate#/definitions/observation/properties/observationDate
```

Please provide the date that the observation was made. Some datasets may be continuously updated and the number of records will change regularly, so the observation date provides users with the date that the analysis or query was run to generate the particular observation. Multiple observations can be made i.e. an observation of cumulative COVID positive cases by specimen on the 1/1/2021 could be 2M. On the 8/1/2021 a new observation could be 2.1M. Users can add multiple observations.

> <https://schema.org/observationDate>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## observationDate Type

merged type ([Observation Date](dataset-definitions-observation-properties-observation-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-1.md "check type definition")

## observationDate Default Value

The default value is:

```json
"release date"
```
