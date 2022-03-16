# Untitled undefined type in HDR UK Dataset Schema Schema

```txt
#/definitions/formatAndStandards#/definitions/formatAndStandards
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## formatAndStandards Type

unknown

# formatAndStandards Properties

| Property                                              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :---------------------------------------------------- | :----- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [vocabularyEncodingScheme](#vocabularyencodingscheme) | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md "#/properties/accessibility/formatAndStandards/vocabularyEncodingScheme#/definitions/formatAndStandards/properties/vocabularyEncodingScheme") |
| [conformsTo](#conformsto)                             | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to.md "#/properties/accessibility/formatAndStandards/conformsTo#/definitions/formatAndStandards/properties/conformsTo")                                       |
| [language](#language)                                 | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language.md "#/properties/accessibility/formatAndStandards/language#/definitions/formatAndStandards/properties/language")                                              |
| [format](#format)                                     | Merged | Required | cannot be null | [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format.md "#/properties/accessibility/formatAndStandards/format#/definitions/formatAndStandards/properties/format")                                                    |

## vocabularyEncodingScheme

List any relevant terminologies / ontologies / controlled vocabularies, such as ICD 10 Codes, NHS Data Dictionary National Codes or SNOMED CT International, that are being used by the dataset. If the controlled vocabularies are local standards, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition. Notes: More than one vocabulary may be provided.

> <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/dcam/VocabularyEncodingScheme>

`vocabularyEncodingScheme`

*   is required

*   Type: merged type ([Controlled Vocabulary](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md "#/properties/accessibility/formatAndStandards/vocabularyEncodingScheme#/definitions/formatAndStandards/properties/vocabularyEncodingScheme")

### vocabularyEncodingScheme Type

merged type ([Controlled Vocabulary](dataset-definitions-formatandstandards-properties-controlled-vocabulary.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-controlled-vocabulary-anyof-1.md "check type definition")

### vocabularyEncodingScheme Default Value

The default value is:

```json
"LOCAL"
```

## conformsTo

List standardised data models that the dataset has been stored in or transformed to, such as OMOP or FHIR. If the data is only available in a local format, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition.

> dct:conformsTo

`conformsTo`

*   is required

*   Type: merged type ([Conforms To](dataset-definitions-formatandstandards-properties-conforms-to.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to.md "#/properties/accessibility/formatAndStandards/conformsTo#/definitions/formatAndStandards/properties/conformsTo")

### conformsTo Type

merged type ([Conforms To](dataset-definitions-formatandstandards-properties-conforms-to.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-conforms-to-anyof-1.md "check type definition")

### conformsTo Default Value

The default value is:

```json
"LOCAL"
```

## language

This should list all the languages in which the dataset metadata and underlying data is made available.

> dct:language. FIXME: Conforms to spec, but may be a list of strings given cardinality 1:\*. Validate against external list of languages. Resources defined by the Library of Congress (ISO 639-1, ISO 639-2) SHOULD be used.

`language`

*   is required

*   Type: merged type ([Language](dataset-definitions-formatandstandards-properties-language.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language.md "#/properties/accessibility/formatAndStandards/language#/definitions/formatAndStandards/properties/language")

### language Type

merged type ([Language](dataset-definitions-formatandstandards-properties-language.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-language-anyof-1.md "check type definition")

### language Default Value

The default value is:

```json
"en"
```

## format

If multiple formats are available please specify. See application, audio, image, message, model, multipart, text, video, <https://www.iana.org/assignments/media-types/media-types.xhtml> Note: If your file format is not included in the current list of formats, please indicate other. If you are using the HOP you will be directed to a service desk page where you can request your additional format. If not please go to: <https://metadata.atlassian.net/servicedesk/customer/portal/4> to request your format.

> <http://purl.org/dc/terms/format>

`format`

*   is required

*   Type: merged type ([Format](dataset-definitions-formatandstandards-properties-format.md))

*   cannot be null

*   defined in: [HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format.md "#/properties/accessibility/formatAndStandards/format#/definitions/formatAndStandards/properties/format")

### format Type

merged type ([Format](dataset-definitions-formatandstandards-properties-format.md))

any of

*   [Untitled undefined type in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format-anyof-0.md "check type definition")

*   [Untitled array in HDR UK Dataset Schema](dataset-definitions-formatandstandards-properties-format-anyof-1.md "check type definition")
