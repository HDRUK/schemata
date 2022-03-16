# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/observation#/definitions/observation
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## observation Type

unknown

# observation Properties

| Property                                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                           |
| :------------------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [observedNode](#observednode)                           | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population.md "#/properties/observation/observedNode#/definitions/observation/properties/observedNode")                               |
| [measuredValue](#measuredvalue)                         | `integer` | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-value.md "#/properties/observation/measuredValue#/definitions/observation/properties/measuredValue")                                     |
| [disambiguatingDescription](#disambiguatingdescription) | Merged    | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description.md "#/properties/observation/disambiguatingDescription#/definitions/observation/properties/disambiguatingDescription") |
| [observationDate](#observationdate)                     | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date.md "#/properties/observation/observationDate#/definitions/observation/properties/observationDate")                               |
| [measuredProperty](#measuredproperty)                   | Merged    | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property.md "#/properties/observation/measuredProperty#/definitions/observation/properties/measuredProperty")                            |

## observedNode

Please select one of the following statistical populations for you observation

> <https://schema.org/observedNode>

`observedNode`

*   is required

*   Type: merged type ([Statistical Population](dataset-definitions-observation-properties-statistical-population.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population.md "#/properties/observation/observedNode#/definitions/observation/properties/observedNode")

### observedNode Type

merged type ([Statistical Population](dataset-definitions-observation-properties-statistical-population.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-observation-properties-statistical-population-allof-0.md "check type definition")

### observedNode Examples

```json
"PERSONS"
```

## measuredValue

Please provide the population size associated with the population type the dataset i.e. 1000 people in a study, or 87 images (MRI) of Knee Usage Note: Used with Statistical Population, which specifies the type of the population in the dataset.

> <https://schema.org/measuredValue>

`measuredValue`

*   is required

*   Type: `integer` ([Measured Value](dataset-definitions-observation-properties-measured-value.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-value.md "#/properties/observation/measuredValue#/definitions/observation/properties/measuredValue")

### measuredValue Type

`integer` ([Measured Value](dataset-definitions-observation-properties-measured-value.md))

## disambiguatingDescription

If SNOMED CT term does not provide sufficient detail, please provide a description that disambiguates the population type.

> <https://schema.org/disambiguatingDescription>

`disambiguatingDescription`

*   is optional

*   Type: merged type ([Disambiguating Description](dataset-definitions-observation-properties-disambiguating-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description.md "#/properties/observation/disambiguatingDescription#/definitions/observation/properties/disambiguatingDescription")

### disambiguatingDescription Type

merged type ([Disambiguating Description](dataset-definitions-observation-properties-disambiguating-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-observation-properties-disambiguating-description-allof-0.md "check type definition")

## observationDate

Please provide the date that the observation was made. Some datasets may be continuously updated and the number of records will change regularly, so the observation date provides users with the date that the analysis or query was run to generate the particular observation. Multiple observations can be made i.e. an observation of cumulative COVID positive cases by specimen on the 1/1/2021 could be 2M. On the 8/1/2021 a new observation could be 2.1M. Users can add multiple observations.

> <https://schema.org/observationDate>

`observationDate`

*   is required

*   Type: merged type ([Observation Date](dataset-definitions-observation-properties-observation-date.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date.md "#/properties/observation/observationDate#/definitions/observation/properties/observationDate")

### observationDate Type

merged type ([Observation Date](dataset-definitions-observation-properties-observation-date.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-0.md "check type definition")

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-observation-date-anyof-1.md "check type definition")

### observationDate Default Value

The default value is:

```json
"release date"
```

## measuredProperty

Initially this will be defaulted to "COUNT"

> <https://schema.org/measuredProperty>

`measuredProperty`

*   is required

*   Type: merged type ([Measured Property](dataset-definitions-observation-properties-measured-property.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property.md "#/properties/observation/measuredProperty#/definitions/observation/properties/measuredProperty")

### measuredProperty Type

merged type ([Measured Property](dataset-definitions-observation-properties-measured-property.md))

all of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-observation-properties-measured-property-allof-0.md "check type definition")

### measuredProperty Default Value

The default value is:

```json
"COUNT"
```
