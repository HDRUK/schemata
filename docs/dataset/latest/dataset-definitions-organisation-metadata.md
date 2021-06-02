# Organisation Metadata Schema

```txt
#/definitions/organisation#/definitions/organisation
```

Describes an organisation for purposes of discovery and identification.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## organisation Type

`object` ([Organisation Metadata](dataset-definitions-organisation-metadata.md))

# organisation Properties

| Property                                    | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------------------ | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [identifier](#identifier)                   | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier.md "#/organisation/identifier#/definitions/organisation/properties/identifier")                        |
| [name](#name)                               | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name.md "#/organisation/name#/definitions/organisation/properties/name")                                          |
| [logo](#logo)                               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo.md "#/organisation/logo#/definitions/organisation/properties/logo")                                          |
| [description](#description)                 | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description.md "#/organisation/description#/definitions/organisation/properties/description")                     |
| [contactPoint](#contactpoint)               | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md "#/organisation/contactPoint#/definitions/organisation/properties/contactPoint")                 |
| [memberOf](#memberof)                       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership.md "#/organisation/memberOf#/definitions/organisation/properties/memberOf")                            |
| [accessRights](#accessrights)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md "#/organisation/accessRights#/definitions/organisation/properties/accessRights")         |
| [deliveryLeadTime](#deliveryleadtime)       | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration.md "#/organisation/deliveryLeadTime#/definitions/organisation/properties/deliveryLeadTime")            |
| [accessService](#accessservice)             | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service.md "#/organisation/accessService#/definitions/organisation/properties/accessService")              |
| [accessRequestCost](#accessrequestcost)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md "#/organisation/accessRequestCost#/definitions/organisation/properties/accessRequestCost") |
| [dataUseLimitation](#datauselimitation)     | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation.md "#/organisation/dataUseLimitation#/definitions/organisation/properties/dataUseLimitation")              |
| [dataUseRequirements](#datauserequirements) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements.md "#/organisation/dataUseRequirements#/definitions/organisation/properties/dataUseRequirements")        |

## identifier

Please provide a Grid.ac identifier (see <https://www.grid.ac/institutes>) for your organisation. If your organisation does not have a Grid.ac identifier please use the “suggest and institute” function here: <https://www.grid.ac/institutes#>

> <https://schema.org/identifier>

`identifier`

*   is optional

*   Type: merged type ([Organisation Identifier](dataset-definitions-organisation-metadata-properties-organisation-identifier.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier.md "#/organisation/identifier#/definitions/organisation/properties/identifier")

### identifier Type

merged type ([Organisation Identifier](dataset-definitions-organisation-metadata-properties-organisation-identifier.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-identifier-allof-0.md "check type definition")

## name

Name of the organisation

> <https://schema.org/name>

`name`

*   is required

*   Type: merged type ([Organisation Name](dataset-definitions-organisation-metadata-properties-organisation-name.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name.md "#/organisation/name#/definitions/organisation/properties/name")

### name Type

merged type ([Organisation Name](dataset-definitions-organisation-metadata-properties-organisation-name.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-name-allof-0.md "check type definition")

## logo

Please provide a logo associated with the Gateway Organisation using a valid URL. The following formats will be accepted .jpg, .png or .svg.

> <https://schema.org/logo>

`logo`

*   is optional

*   Type: merged type ([Organisation Logo](dataset-definitions-organisation-metadata-properties-organisation-logo.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo.md "#/organisation/logo#/definitions/organisation/properties/logo")

### logo Type

merged type ([Organisation Logo](dataset-definitions-organisation-metadata-properties-organisation-logo.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-logo-allof-0.md "check type definition")

## description

Please provide a URL that describes the organisation.

> <https://schema.org/description>

`description`

*   is optional

*   Type: merged type ([Organisation Description](dataset-definitions-organisation-metadata-properties-organisation-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description.md "#/organisation/description#/definitions/organisation/properties/description")

### description Type

merged type ([Organisation Description](dataset-definitions-organisation-metadata-properties-organisation-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-description-allof-0.md "check type definition")

## contactPoint

Organisation contact point(s)

> <https://schema.org/contactPoint>

`contactPoint`

*   is required

*   Type: merged type ([Organisation Contact Point](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md "#/organisation/contactPoint#/definitions/organisation/properties/contactPoint")

### contactPoint Type

merged type ([Organisation Contact Point](dataset-definitions-organisation-metadata-properties-organisation-contact-point.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-contact-point-anyof-1.md "check type definition")

## memberOf

Please indicate if the organisation is an Alliance Member or a Hub.

> <https://schema.org/memberOf>

`memberOf`

*   is optional

*   Type: merged type ([Organisation Membership](dataset-definitions-organisation-metadata-properties-organisation-membership.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership.md "#/organisation/memberOf#/definitions/organisation/properties/memberOf")

### memberOf Type

merged type ([Organisation Membership](dataset-definitions-organisation-metadata-properties-organisation-membership.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-membership-allof-0.md "check type definition")

## accessRights

The URL of a webpage where the data access request process and/or guidance is provided. If there is more than one access process i.e. industry vs academic please provide both.

> dct:access_rights

`accessRights`

*   is optional

*   Type: merged type ([Organisation Default Access Rights](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md "#/organisation/accessRights#/definitions/organisation/properties/accessRights")

### accessRights Type

merged type ([Organisation Default Access Rights](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-default-access-rights-anyof-1.md "check type definition")

## deliveryLeadTime

Please provide an indication of the typical processing times based on the types of requests typically received. Note: This value will be used as default access request duration for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> <https://schema.org/deliveryLeadTime>

`deliveryLeadTime`

*   is optional

*   Type: merged type ([Access Request Duration](dataset-definitions-organisation-metadata-properties-access-request-duration.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration.md "#/organisation/deliveryLeadTime#/definitions/organisation/properties/deliveryLeadTime")

### deliveryLeadTime Type

merged type ([Access Request Duration](dataset-definitions-organisation-metadata-properties-access-request-duration.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-access-request-duration-allof-0.md "check type definition")

## accessService

Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> dcat:accessService

`accessService`

*   is optional

*   Type: merged type ([Organisation Access Service](dataset-definitions-organisation-metadata-properties-organisation-access-service.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service.md "#/organisation/accessService#/definitions/organisation/properties/accessService")

### accessService Type

merged type ([Organisation Access Service](dataset-definitions-organisation-metadata-properties-organisation-access-service.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-service-allof-0.md "check type definition")

### accessService Examples

```json
"https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide"
```

## accessRequestCost

Please provide link(s) to a webpage or a short description detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.

> No standard identified

`accessRequestCost`

*   is optional

*   Type: merged type ([Organisation Access Request Cost](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md "#/organisation/accessRequestCost#/definitions/organisation/properties/accessRequestCost")

### accessRequestCost Type

merged type ([Organisation Access Request Cost](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-organisation-access-request-cost-anyof-1.md "check type definition")

## dataUseLimitation

Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Notes: where there are existing data-sharing arrangements such as the HDR UK HUB data sharing agreement or the NIHR HIC data sharing agreement this should be indicated within access rights. This value will be used as terms for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseLimitation`

*   is optional

*   Type: merged type ([Data Use Limitation](dataset-definitions-organisation-metadata-properties-data-use-limitation.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation.md "#/organisation/dataUseLimitation#/definitions/organisation/properties/dataUseLimitation")

### dataUseLimitation Type

merged type ([Data Use Limitation](dataset-definitions-organisation-metadata-properties-data-use-limitation.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-limitation-anyof-1.md "check type definition")

## dataUseRequirements

Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.

> <https://www.ebi.ac.uk/ols/ontologies/duo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDUO_0000001>

`dataUseRequirements`

*   is optional

*   Type: merged type ([Data Use Requirements](dataset-definitions-organisation-metadata-properties-data-use-requirements.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements.md "#/organisation/dataUseRequirements#/definitions/organisation/properties/dataUseRequirements")

### dataUseRequirements Type

merged type ([Data Use Requirements](dataset-definitions-organisation-metadata-properties-data-use-requirements.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-organisation-metadata-properties-data-use-requirements-anyof-1.md "check type definition")
