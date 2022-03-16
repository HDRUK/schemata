# Documentation Schema

```txt
#/definitions/documentation#/properties/documentation
```

Documentation can include a rich text description of the dataset or links to media such as documents, images, presentations, videos or links to data dictionaries, profiles or dashboards. Organisations are required to confirm that they have permission to distribute any additional media.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json\*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## documentation Type

unknown ([Documentation](dataset-properties-documentation.md))

# documentation Properties

| Property                            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                   |
| :---------------------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description)         | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-description.md "#/properties/documentation/description#/definitions/documentation/properties/description")              |
| [associatedMedia](#associatedmedia) | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media.md "#/properties/documentation/associatedMedia#/definitions/documentation/properties/associatedMedia") |
| [isPartOf](#ispartof)               | Merged | Optional | cannot be null | [HDR UK Dataset Schema](dataset-definitions-documentation-properties-group.md "#/properties/documentation/isPartOf#/definitions/documentation/properties/isPartOf")                          |

## description

A free-text description of the record.

> dc:description, <https://schema.org/description>

`description`

*   is optional

*   Type: merged type ([Description](dataset-definitions-documentation-properties-description.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-description.md "#/properties/documentation/description#/definitions/documentation/properties/description")

### description Type

merged type ([Description](dataset-definitions-documentation-properties-description.md))

all of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-description-allof-0.md "check type definition")

## associatedMedia

Please provide any media associated with the Gateway Organisation using a valid URI for the content. This is an opportunity to provide additional context that could be useful for researchers wanting to understand more about the dataset and its relevance to their research question. The following formats will be accepted .jpg, .png or .svg, .pdf, .xslx or .docx. Note: media asset can be hosted by the organisation or uploaded using the onboarding portal.

> <https://schema.org/associatedMedia>

`associatedMedia`

*   is optional

*   Type: merged type ([Associated Media](dataset-definitions-documentation-properties-associated-media.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media.md "#/properties/documentation/associatedMedia#/definitions/documentation/properties/associatedMedia")

### associatedMedia Type

merged type ([Associated Media](dataset-definitions-documentation-properties-associated-media.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-documentation-properties-associated-media-anyof-1.md "check type definition")

### associatedMedia Examples

```json
"PDF Document that describes study protocol"
```

## isPartOf

Please complete only if the dataset is part of a group or family

> <https://schema.org/isPartOf> NOTE: we may make Groups first class citizens so the are navigable

`isPartOf`

*   is optional

*   Type: merged type ([Group](dataset-definitions-documentation-properties-group.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-documentation-properties-group.md "#/properties/documentation/isPartOf#/definitions/documentation/properties/isPartOf")

### isPartOf Type

merged type ([Group](dataset-definitions-documentation-properties-group.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-documentation-properties-group-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-documentation-properties-group-anyof-1.md "check type definition")

### isPartOf Default Value

The default value is:

```json
"NOT APPLICABLE"
```

### isPartOf Examples

```json
"Hospital Episodes Statistics datasets (A&E, APC, OP, AC MSDS)."
```
