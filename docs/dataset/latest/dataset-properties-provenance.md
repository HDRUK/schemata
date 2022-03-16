# Provenance Schema

```txt
#/definitions/provenance#/properties/provenance
```

Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## provenance Type

unknown ([Provenance](dataset-properties-provenance.md))

# provenance Properties

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                                                     |
| :-------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [origin](#origin)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin.md "#/definitions/provenance/origin#/definitions/provenance/properties/origin")       |
| [temporal](#temporal) | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal.md "#/definitions/provenance/temporal#/definitions/provenance/properties/temporal") |

## origin



`origin`

*   is optional

*   Type: merged type ([Details](dataset-definitions-provenance-properties-origin.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin.md "#/definitions/provenance/origin#/definitions/provenance/properties/origin")

### origin Type

merged type ([Details](dataset-definitions-provenance-properties-origin.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-provenance-properties-origin-allof-0.md "check type definition")

## temporal



`temporal`

*   is required

*   Type: merged type ([Details](dataset-definitions-provenance-properties-temporal.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal.md "#/definitions/provenance/temporal#/definitions/provenance/properties/temporal")

### temporal Type

merged type ([Details](dataset-definitions-provenance-properties-temporal.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-provenance-properties-temporal-allof-0.md "check type definition")
