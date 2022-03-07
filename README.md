![generate-markdown](https://github.com/HDRUK/schemata/workflows/generate-markdown/badge.svg)

# HDR UK Schemata - Dataset V2.1

### 1. [HDR UK Dataset Schema](https://hdruk.github.io/schemata/schema/dataset/latest/) - [YAML](https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.yaml) - [JSON](https://hdruk.github.io/schemata/schema/dataset/latest/dataset.schema.json)

The latest version specification required for datasets to be on boarded onto the Gateway are shown in this repository and is comprised of the following:

 - The latest json schema and yaml which can be found here: https://github.com/HDRUK/schemata/blob/master/schema/dataset/latest. They represent the V2 metadata specification for onboarding datasets onto the Gateway presented in the [descriptive metadata documentation](https://github.com/HDRUK/schemata/tree/master/docs/dataset/2.0.0/distribution).
 - Example json files which can be found here: https://github.com/HDRUK/schemata/blob/master/examples. It includes a current mapped dataset, a minimum json example and a full example of the metadata for onboarding to the Gateway.
 - The latest word documentation, change log and mapping file which can be found here: https://github.com/HDRUK/schemata/tree/master/docs/dataset/2.0.0/distribution. The documentation provides details of the descriptive metadata needed for the Gateway including their definitions and user stories to illustrate its purpose.
 - An impact assessment and indicative mapping files which can be found here: https://github.com/HDRUK/schemata/tree/master/docs/dataset/2.0.0/impact-assessment. It contains the following files:
   - *aggregated_errors.xlsx*: aggregated validation errors with an overview on the most common errors per attribute that will need to be resolved during migration.
   - *generated_mapping.py*: the mapping algorithm that generates v2 data-models, (basically a mapping function for all fields in the new v2 specs).
   - *v1_to_v2.json*: for each data-model (key is the UUID) v1: old schema, v2: new schema, which is the mapping result (*generated_mapping.py*) of all data-models in the gateway.
   - *dm_validation.json*: for each data-model (key again is UUID) the data-set in form of the v2 attributes and the JSON schema validation.
   - *aggregated_errors.json*: an aggregation of the validation of all data-models by attribute with a list of unique error messages, a count of unique error messages, and a total count of the errors across all data-models; note that JSON schema validator generates an entry for all hierarchy levels, which means some error messages are repeated along the hierarchy.



### 2. Dataset Properties Breakdown

Below is the breakdown of the HDR UK V2 Dataset Schema by its properties and sub properties as defined in the [JSON Schema](https://github.com/HDRUK/schemata/blob/master/schema/dataset/latest/dataset.schema.json). Each property from 1-7 has its own Schema with a description of its corresponding sub properties, including their data type and whether it is a required field.

<!--ts-->

#### 0. Metadata: Properties generated when dataset is entered into the system.

   * [identifier](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-dataset-identifier.md#dataset-identifier-schema)
   * [version](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-dataset-version.md#dataset-version-schema)
 * [revisions](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-dataset-revisions.md#dataset-revisions-schema)
 * [issued](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-creation-date.md#creation-date-schema)
 * [modified](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-modification-date.md#modification-date-schema)

#### 1. [summary](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-summary.md#summary-schema): Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.

 * [title](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#title)
 * [abstract](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#abstract)
 * [publisher](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#publisher)
 * [contactPoint](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#contactpoint)
 * [keywords](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#keywords)
 * [alternateIdentifiers](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#alternateidentifiers)
 * [doiName](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#doiname)

#### 2. [documentation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-documentation.md#documentation-schema): Documentation can include a rich text description of the dataset or links to media such as documents, images, presentations, videos or links to data dictionaries, profiles or dashboards. Organisations are required to confirm that they have permission to distribute any additional media.

 * [description](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#description-1)
 * [associatedMedia](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#associatedmedia)
 * [isPartOf](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#ispartof)

#### 3. [coverage](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-coverage.md#coverage-schema): This information includes attributes for geographical and temporal coverage, cohort details etc. to enable a deeper understanding of the dataset content so that researchers can make decisions about the relevance of the underlying data.

 * [spatial](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#spatial)
 * [typicalAgeRange](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#typicalagerange)
 * [physicalSampleAvailability](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#physicalsampleavailability)
 * [followup](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#followup)
 * [pathway](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#pathway)

#### 4. [provenance](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-provenance.md#provenance-schema): Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.

 * [origin](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#origin)
    * [purpose](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#purpose)
    * [source](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#source)
    * [collectionSituation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#collectionsituation)
 * [temporal](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#temporal)
    * [accrualPeriodicity](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#accrualperiodicity)
    * [distributionReleaseDate](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#distributionreleasedate)
    * [startDate](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#startdate)
    * [endDate](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#enddate)
    * [timeLag](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#timelag)

#### 5. [accessibility](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-accessibility.md#accessibility-schema): Accessibility information allows researchers to understand access, usage, limitations, formats, standards and linkage or interoperability with toolsets.

 * [usage](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#usage)
    * [dataUseLimitation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#datauselimitation-1)
    * [dataUseRequirements](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#datauserequirements-1)
    * [resourceCreator](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#resourcecreator)
    * [investigations](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#investigations)
    * [isReferencedBy](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#isreferencedby)
 * [access](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#access)
    * [accessRights](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#accessrights-1)
    * [accessService](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#accessservice-1)
    * [accessRequestCost](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#accessrequestcost-1)
    * [deliveryLeadTime](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#deliveryleadtime-1)
    * [jurisdiction](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#jurisdiction)
    * [dataController](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#datacontroller)
    * [dataProcessor](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#dataprocessor)
 * [formatAndStandards](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#formatandstandards)
    * [vocabularyEncodingScheme](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#vocabularyencodingscheme)
    * [conformsTo](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#conformsto)
    * [language](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#language)
    * [format](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#format)

#### 6. [enrichmentAndLinkage](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-enrichment-and-linkage.md#enrichment-and-linkage-schema): This section includes information about related datasets that may have previously been linked, as well as indicating if there is the opportunity to link to other datasets in the future. If a dataset has been enriched and/or derivations, scores and existing tools are available this section allows providers to indicate this to researchers.

 * [qualifiedRelation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#qualifiedrelation)
 * [derivation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#derivation)
 * [tools](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#tools)

#### 7. [observations](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-observations.md#observations-schema): Multiple observations about the dataset may be provided and users are expected to provide at least one observation (1..*). We will be supporting the schema.org observation model (https://schema.org/Observation) with default values. Users will be encouraged to provide their own statistical populations as the project progresses.

- [observation](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#definitions-group-observation)
  - [observedNode](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#observednode)
  - [measuredValue](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#measuredvalue)
  - [disambiguatingDescription](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#disambiguatingdescription)
  - [observationDate](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#observationdate)
  - [measuredProperty](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#measuredproperty)

#### 8. [structuralMetadata](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset-properties-structural-metadata.md#structural-metadata-schema): Descriptions and details about the tables and columns within a dataset.

- [dataClass](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#definitions-group-dataclass)
  - [name](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#name-1)
  - [description](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#description-2)
  - [elements](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#elements)
- [dataElement](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#definitions-group-dataelements)
  - [name](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#name-2)
  - [description](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#description-3)
  - [dataType](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#datatype)
  - [sensitive](https://github.com/HDRUK/schemata/blob/master/docs/dataset/latest/dataset.md#sensitive)

<!--te-->



### 3. [Metadata Quality Scoring](https://github.com/JakeBGitHub/datasets/tree/dataset-v2-scores/reports#hdr-uk-data-documentation-scores)

Once a dataset is onboarded onto the Gateway, a quality check is run on its corresponding json schema to produce a weighted quality score based on weighted field completeness and weighted field error percentage. Weights of each field can be found here (https://github.com/HDRUK/datasets/tree/master/config/weights) and details of the quality score calculation can be found here (https://github.com/HDRUK/datasets/tree/master/reports#how-scores-are-calculated).

Based on the weighted quality score, a dataset is given a medallion rating as follows:

- <img src="https://render.githubusercontent.com/render/math?math=\leq 60"> is "Not rated",
- <img src="https://render.githubusercontent.com/render/math?math=> 60"> & <img src="https://render.githubusercontent.com/render/math?math=\leq 70"> is "Bronze",
- <img src="https://render.githubusercontent.com/render/math?math=> 70"> & <img src="https://render.githubusercontent.com/render/math?math=\leq 80"> is "Silver",
- <img src="https://render.githubusercontent.com/render/math?math=> 80"> & <img src="https://render.githubusercontent.com/render/math?math=\leq 90"> is "Gold",
- <img src="https://render.githubusercontent.com/render/math?math=> 90"> is "Platinum".

