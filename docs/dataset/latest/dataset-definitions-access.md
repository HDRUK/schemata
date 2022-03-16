# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/access#/definitions/access
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## access Type

unknown

# access Properties

| Property                                | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :-------------------------------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [accessRights](#accessrights)           | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights.md "#/properties/accessibility/access/accessRights#/definitions/access/properties/accessRights")                              |
| [accessService](#accessservice)         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-service.md "#/properties/accessibility/access/accessService#/definitions/access/properties/accessService")                           |
| [accessRequestCost](#accessrequestcost) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost.md "#/properties/accessibility/access/accessRequestCost#/definitions/access/properties/accessRequestCost") |
| [deliveryLeadTime](#deliveryleadtime)   | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration.md "#/properties/accessibility/access/deliveryLeadTime#/definitions/access/properties/deliveryLeadTime")            |
| [jurisdiction](#jurisdiction)           | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction.md "#/properties/accessibility/access/jurisdiction#/definitions/access/properties/jurisdiction")                               |
| [dataController](#datacontroller)       | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller.md "#/properties/accessibility/access/dataController#/definitions/access/properties/dataController")                        |
| [dataProcessor](#dataprocessor)         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor.md "#/properties/accessibility/access/dataProcessor#/definitions/access/properties/dataProcessor")                           |

## accessRights



> dct:access_rights NOTE: need to ensure that this is consistent across the organisation info and the dataset info

`accessRights`

*   is required

*   Type: merged type ([Access Rights](dataset-definitions-access-properties-access-rights.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights.md "#/properties/accessibility/access/accessRights#/definitions/access/properties/accessRights")

### accessRights Type

merged type ([Access Rights](dataset-definitions-access-properties-access-rights.md))

any of

*   [Untitled string in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-0.md "check type definition")

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-1.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-access-rights-anyof-2.md "check type definition")

## accessService

Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> dcat:accessService

`accessService`

*   is optional

*   Type: merged type ([Access Service](dataset-definitions-access-properties-access-service.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-service.md "#/properties/accessibility/access/accessService#/definitions/access/properties/accessService")

### accessService Type

merged type ([Access Service](dataset-definitions-access-properties-access-service.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-service-allof-0.md "check type definition")

### accessService Examples

```json
"https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide"
```

## accessRequestCost

Please provide link(s) to a webpage detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.

> No standard identified

`accessRequestCost`

*   is optional

*   Type: merged type ([Organisation Access Request Cost](dataset-definitions-access-properties-organisation-access-request-cost.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost.md "#/properties/accessibility/access/accessRequestCost#/definitions/access/properties/accessRequestCost")

### accessRequestCost Type

merged type ([Organisation Access Request Cost](dataset-definitions-access-properties-organisation-access-request-cost.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-organisation-access-request-cost-anyof-1.md "check type definition")

## deliveryLeadTime

Please provide an indication of the typical processing times based on the types of requests typically received.

> <https://schema.org/deliveryLeadTime>

`deliveryLeadTime`

*   is optional

*   Type: merged type ([Access Request Duration](dataset-definitions-access-properties-access-request-duration.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration.md "#/properties/accessibility/access/deliveryLeadTime#/definitions/access/properties/deliveryLeadTime")

### deliveryLeadTime Type

merged type ([Access Request Duration](dataset-definitions-access-properties-access-request-duration.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-access-request-duration-allof-0.md "check type definition")

## jurisdiction

Please use country code from ISO 3166-1 country codes and the associated ISO 3166-2 for regions, cities, states etc. for the country/state under whose laws the data subjects' data is collected, processed and stored.

> <http://purl.org/dc/terms/Jurisdiction> FIXME: Add ISO 3166-2 Subdivision code pattern

`jurisdiction`

*   is required

*   Type: merged type ([Jurisdiction](dataset-definitions-access-properties-jurisdiction.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction.md "#/properties/accessibility/access/jurisdiction#/definitions/access/properties/jurisdiction")

### jurisdiction Type

merged type ([Jurisdiction](dataset-definitions-access-properties-jurisdiction.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-access-properties-jurisdiction-anyof-1.md "check type definition")

### jurisdiction Default Value

The default value is:

```json
"GB-ENG"
```

## dataController

Data Controller means a person/entity who (either alone or jointly or in common with other persons/entities) determines the purposes for which and the way any Data Subject data, specifically personal data or are to be processed.

> dpv:DataController

`dataController`

*   is required

*   Type: merged type ([Data Controller](dataset-definitions-access-properties-data-controller.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller.md "#/properties/accessibility/access/dataController#/definitions/access/properties/dataController")

### dataController Type

merged type ([Data Controller](dataset-definitions-access-properties-data-controller.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-data-controller-allof-0.md "check type definition")

## dataProcessor

A Data Processor, in relation to any Data Subject data, specifically personal data, means any person/entity (other than an employee of the data controller) who processes the data on behalf of the data controller.

> dpv:DataProcessor

`dataProcessor`

*   is optional

*   Type: merged type ([Data Processor](dataset-definitions-access-properties-data-processor.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor.md "#/properties/accessibility/access/dataProcessor#/definitions/access/properties/dataProcessor")

### dataProcessor Type

merged type ([Data Processor](dataset-definitions-access-properties-data-processor.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-access-properties-data-processor-allof-0.md "check type definition")
