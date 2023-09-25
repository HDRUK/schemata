from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr


class IsPartOfEnum(Enum):
    NOT_APPLICABLE = 'NOT APPLICABLE'


class EndDateEnum(Enum):
    CONTINUOUS = 'CONTINUOUS'
    NoneType_None = None


class MeasuredProperty(BaseModel):
    pass


class Uuidv4(BaseModel):
    root: constr(
        pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',
        min_length=36,
        max_length=36,
    )


class Semver(BaseModel):
    root: constr(pattern=r'^([0-9]+)\.([0-9]+)\.([0-9]+)$')

    
class Url(BaseModel):
    root: Optional[AnyUrl]


class OneHundredFiftyCharacters(BaseModel):
    root: constr(min_length=2, max_length=150)


class AbstractText(BaseModel):
    root: Optional[constr(min_length=5, max_length=500)]


class EmailAddress(BaseModel):
    root: Optional[EmailStr]


class ShortDescription(BaseModel):
    root: Optional[constr(min_length=2, max_length=1000)]


class Description(BaseModel):
    root: Optional[constr(min_length=2, max_length=10000)]


class LongDescription(BaseModel):
    root: Optional[constr(min_length=2, max_length=50000)]


class CommaSeparatedValues(BaseModel):
    root: Optional[constr(pattern=r'([^,]+)')]


class Doi(BaseModel):
    root: Optional[constr(pattern=r'^10.\d{4,9}/[-._;()/:a-zA-Z0-9]+$')]


class AgeRange(BaseModel):
    root: Optional[
        constr(
            pattern=r'Not Known|(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])-(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])'
        )
    ]


class Format(BaseModel):
    root: constr(min_length=1)


class Isocountrycode(BaseModel):
    root: constr(pattern=r'^[A-Z]{2}(-[A-Z]{2,3})?$')


class MemberOf(Enum):
    HUB = 'HUB'
    ALLIANCE = 'ALLIANCE'
    OTHER = 'OTHER'
    NCS = 'NCS'


class PhysicalSampleAvailability(Enum):
    NOT_AVAILABLE = 'NOT AVAILABLE'
    BONE_MARROW = 'BONE MARROW'
    CANCER_CELL_LINES = 'CANCER CELL LINES'
    CORE_BIOPSY = 'CORE BIOPSY'
    CDNA_OR_MRNA = 'CDNA OR MRNA'
    DNA = 'DNA'
    FAECES = 'FAECES'
    IMMORTALIZED_CELL_LINES = 'IMMORTALIZED CELL LINES'
    MICRORNA = 'MICRORNA'
    PERIPHERAL_BLOOD_CELLS = 'PERIPHERAL BLOOD CELLS'
    PLASMA = 'PLASMA'
    PM_TISSUE = 'PM TISSUE'
    PRIMARY_CELLS = 'PRIMARY CELLS'
    RNA = 'RNA'
    SALIVA = 'SALIVA'
    SERUM = 'SERUM'
    SWABS = 'SWABS'
    TISSUE = 'TISSUE'
    URINE = 'URINE'
    WHOLE_BLOOD = 'WHOLE BLOOD'
    AVAILABILITY_TO_BE_CONFIRMED = 'AVAILABILITY TO BE CONFIRMED'
    OTHER = 'OTHER'


class Followup(Enum):
    field_0___6_MONTHS = '0 - 6 MONTHS'
    field_6___12_MONTHS = '6 - 12 MONTHS'
    field_1___10_YEARS = '1 - 10 YEARS'
    field__10_YEARS = '> 10 YEARS'
    UNKNOWN = 'UNKNOWN'
    CONTINUOUS = 'CONTINUOUS'
    OTHER = 'OTHER'
    NoneType_None = None


class Periodicity(Enum):
    STATIC = 'STATIC'
    IRREGULAR = 'IRREGULAR'
    CONTINUOUS = 'CONTINUOUS'
    BIENNIAL = 'BIENNIAL'
    ANNUAL = 'ANNUAL'
    BIANNUAL = 'BIANNUAL'
    QUARTERLY = 'QUARTERLY'
    BIMONTHLY = 'BIMONTHLY'
    MONTHLY = 'MONTHLY'
    BIWEEKLY = 'BIWEEKLY'
    WEEKLY = 'WEEKLY'
    SEMIWEEKLY = 'SEMIWEEKLY'
    DAILY = 'DAILY'
    OTHER = 'OTHER'
    NoneType_None = None


class Purpose(Enum):
    STUDY = 'STUDY'
    DISEASE_REGISTRY = 'DISEASE REGISTRY'
    TRIAL = 'TRIAL'
    CARE = 'CARE'
    AUDIT = 'AUDIT'
    ADMINISTRATIVE = 'ADMINISTRATIVE'
    FINANCIAL = 'FINANCIAL'
    STATUTORY = 'STATUTORY'
    OTHER = 'OTHER'
    NoneType_None = None


class Source(Enum):
    EPR = 'EPR'
    ELECTRONIC_SURVEY = 'ELECTRONIC SURVEY'
    LIMS = 'LIMS'
    OTHER_INFORMATION_SYSTEM = 'OTHER INFORMATION SYSTEM'
    PAPER_BASED = 'PAPER BASED'
    FREETEXT_NLP = 'FREETEXT NLP'
    MACHINE_GENERATED = 'MACHINE GENERATED'
    OTHER = 'OTHER'


class Setting(Enum):
    CLINIC = 'CLINIC'
    PRIMARY_CARE = 'PRIMARY CARE'
    ACCIDENT_AND_EMERGENCY = 'ACCIDENT AND EMERGENCY'
    OUTPATIENTS = 'OUTPATIENTS'
    IN_PATIENTS = 'IN-PATIENTS'
    SERVICES = 'SERVICES'
    COMMUNITY = 'COMMUNITY'
    HOME = 'HOME'
    PRIVATE = 'PRIVATE'
    PHARMACY = 'PHARMACY'
    SOCIAL_CARE = 'SOCIAL CARE'
    LOCAL_AUTHORITY = 'LOCAL AUTHORITY'
    NATIONAL_GOVERNMENT = 'NATIONAL GOVERNMENT'
    OTHER = 'OTHER'


class TimeLag(Enum):
    LESS_1_WEEK = 'LESS 1 WEEK'
    field_1_2_WEEKS = '1-2 WEEKS'
    field_2_4_WEEKS = '2-4 WEEKS'
    field_1_2_MONTHS = '1-2 MONTHS'
    field_2_6_MONTHS = '2-6 MONTHS'
    MORE_6_MONTHS = 'MORE 6 MONTHS'
    VARIABLE = 'VARIABLE'
    NO_TIMELAG = 'NO TIMELAG'
    NOT_APPLICABLE = 'NOT APPLICABLE'
    OTHER = 'OTHER'
    NoneType_None = None


class DataUseLimitation(Enum):
    GENERAL_RESEARCH_USE = 'GENERAL RESEARCH USE'
    COMMERCIAL_RESEARCH_USE = 'COMMERCIAL RESEARCH USE'
    GENETIC_STUDIES_ONLY = 'GENETIC STUDIES ONLY'
    NO_GENERAL_METHODS_RESEARCH = 'NO GENERAL METHODS RESEARCH'
    NO_RESTRICTION = 'NO RESTRICTION'
    GEOGRAPHICAL_RESTRICTIONS = 'GEOGRAPHICAL RESTRICTIONS'
    INSTITUTION_SPECIFIC_RESTRICTIONS = 'INSTITUTION SPECIFIC RESTRICTIONS'
    NOT_FOR_PROFIT_USE = 'NOT FOR PROFIT USE'
    PROJECT_SPECIFIC_RESTRICTIONS = 'PROJECT SPECIFIC RESTRICTIONS'
    RESEARCH_SPECIFIC_RESTRICTIONS = 'RESEARCH SPECIFIC RESTRICTIONS'
    USER_SPECIFIC_RESTRICTION = 'USER SPECIFIC RESTRICTION'
    RESEARCH_USE_ONLY = 'RESEARCH USE ONLY'
    NO_LINKAGE = 'NO LINKAGE'


class DataUseRequirements(Enum):
    COLLABORATION_REQUIRED = 'COLLABORATION REQUIRED'
    PROJECT_SPECIFIC_RESTRICTIONS = 'PROJECT SPECIFIC RESTRICTIONS'
    ETHICS_APPROVAL_REQUIRED = 'ETHICS APPROVAL REQUIRED'
    INSTITUTION_SPECIFIC_RESTRICTIONS = 'INSTITUTION SPECIFIC RESTRICTIONS'
    GEOGRAPHICAL_RESTRICTIONS = 'GEOGRAPHICAL RESTRICTIONS'
    PUBLICATION_MORATORIUM = 'PUBLICATION MORATORIUM'
    PUBLICATION_REQUIRED = 'PUBLICATION REQUIRED'
    RETURN_TO_DATABASE_OR_RESOURCE = 'RETURN TO DATABASE OR RESOURCE'
    TIME_LIMIT_ON_USE = 'TIME LIMIT ON USE'
    DISCLOSURE_CONTROL = 'DISCLOSURE CONTROL'
    NOT_FOR_PROFIT_USE = 'NOT FOR PROFIT USE'
    USER_SPECIFIC_RESTRICTION = 'USER SPECIFIC RESTRICTION'
    NoneType_None = None


class DeliveryLeadTime(Enum):
    LESS_1_WEEK = 'LESS 1 WEEK'
    field_1_2_WEEKS = '1-2 WEEKS'
    field_2_4_WEEKS = '2-4 WEEKS'
    field_1_2_MONTHS = '1-2 MONTHS'
    field_2_6_MONTHS = '2-6 MONTHS'
    MORE_6_MONTHS = 'MORE 6 MONTHS'
    VARIABLE = 'VARIABLE'
    NOT_APPLICABLE = 'NOT APPLICABLE'
    OTHER = 'OTHER'
    NoneType_None = None


class StandardisedDataModelsEnum(Enum):
    HL7_FHIR = 'HL7 FHIR'
    HL7_V2 = 'HL7 V2'
    HL7_CDA = 'HL7 CDA'
    HL7_CCOW = 'HL7 CCOW'
    LOINC = 'LOINC'
    DICOM = 'DICOM'
    I2B2 = 'I2B2'
    IHE = 'IHE'
    OMOP = 'OMOP'
    OPENEHR = 'OPENEHR'
    SENTINEL = 'SENTINEL'
    PCORNET = 'PCORNET'
    CDISC = 'CDISC'
    NHS_DATA_DICTIONARY = 'NHS DATA DICTIONARY'
    NHS_SCOTLAND_DATA_DICTIONARY = 'NHS SCOTLAND DATA DICTIONARY'
    NHS_WALES_DATA_DICTIONARY = 'NHS WALES DATA DICTIONARY'
    LOCAL = 'LOCAL'
    OTHER = 'OTHER'


class StandardisedDataModels(BaseModel):
    root: Optional[StandardisedDataModelsEnum] = None


class ControlledVocabularyEnum(Enum):
    LOCAL = 'LOCAL'
    OPCS4 = 'OPCS4'
    READ = 'READ'
    SNOMED_CT = 'SNOMED CT'
    SNOMED_RT = 'SNOMED RT'
    DM_PLUS_D = 'DM PLUS D'
    DM_D = 'DM+D'
    NHS_NATIONAL_CODES = 'NHS NATIONAL CODES'
    NHS_SCOTLAND_NATIONAL_CODES = 'NHS SCOTLAND NATIONAL CODES'
    NHS_WALES_NATIONAL_CODES = 'NHS WALES NATIONAL CODES'
    ODS = 'ODS'
    LOINC = 'LOINC'
    ICD10 = 'ICD10'
    ICD10CM = 'ICD10CM'
    ICD10PCS = 'ICD10PCS'
    ICD9CM = 'ICD9CM'
    ICD9 = 'ICD9'
    ICDO3 = 'ICDO3'
    AMT = 'AMT'
    APC = 'APC'
    ATC = 'ATC'
    CIEL = 'CIEL'
    HPO = 'HPO'
    CPT4 = 'CPT4'
    DPD = 'DPD'
    DRG = 'DRG'
    HEMONC = 'HEMONC'
    JMDC = 'JMDC'
    KCD7 = 'KCD7'
    MULTUM = 'MULTUM'
    NAACCR = 'NAACCR'
    NDC = 'NDC'
    NDFRT = 'NDFRT'
    OXMIS = 'OXMIS'
    RXNORM = 'RXNORM'
    RXNORM_EXTENSION = 'RXNORM EXTENSION'
    SPL = 'SPL'
    OTHER = 'OTHER'


class ControlledVocabulary(BaseModel):
    root: Optional[ControlledVocabularyEnum] = None


class LanguageEnum(Enum):
    aa = 'aa'
    ab = 'ab'
    ae = 'ae'
    af = 'af'
    ak = 'ak'
    am = 'am'
    an = 'an'
    ar = 'ar'
    as_ = 'as'
    av = 'av'
    ay = 'ay'
    az = 'az'
    ba = 'ba'
    be = 'be'
    bg = 'bg'
    bh = 'bh'
    bi = 'bi'
    bm = 'bm'
    bn = 'bn'
    bo = 'bo'
    br = 'br'
    bs = 'bs'
    ca = 'ca'
    ce = 'ce'
    ch = 'ch'
    co = 'co'
    cr = 'cr'
    cs = 'cs'
    cu = 'cu'
    cv = 'cv'
    cy = 'cy'
    da = 'da'
    de = 'de'
    dv = 'dv'
    dz = 'dz'
    ee = 'ee'
    el = 'el'
    en = 'en'
    eo = 'eo'
    es = 'es'
    et = 'et'
    eu = 'eu'
    fa = 'fa'
    ff = 'ff'
    fi = 'fi'
    fj = 'fj'
    fo = 'fo'
    fr = 'fr'
    fy = 'fy'
    ga = 'ga'
    gd = 'gd'
    gl = 'gl'
    gn = 'gn'
    gu = 'gu'
    gv = 'gv'
    ha = 'ha'
    he = 'he'
    hi = 'hi'
    ho = 'ho'
    hr = 'hr'
    ht = 'ht'
    hu = 'hu'
    hy = 'hy'
    hz = 'hz'
    ia = 'ia'
    id = 'id'
    ie = 'ie'
    ig = 'ig'
    ii = 'ii'
    ik = 'ik'
    io = 'io'
    is_ = 'is'
    it = 'it'
    iu = 'iu'
    ja = 'ja'
    jv = 'jv'
    ka = 'ka'
    kg = 'kg'
    ki = 'ki'
    kj = 'kj'
    kk = 'kk'
    kl = 'kl'
    km = 'km'
    kn = 'kn'
    ko = 'ko'
    kr = 'kr'
    ks = 'ks'
    ku = 'ku'
    kv = 'kv'
    kw = 'kw'
    ky = 'ky'
    la = 'la'
    lb = 'lb'
    lg = 'lg'
    li = 'li'
    ln = 'ln'
    lo = 'lo'
    lt = 'lt'
    lu = 'lu'
    lv = 'lv'
    mg = 'mg'
    mh = 'mh'
    mi = 'mi'
    mk = 'mk'
    ml = 'ml'
    mn = 'mn'
    mr = 'mr'
    ms = 'ms'
    mt = 'mt'
    my = 'my'
    na = 'na'
    nb = 'nb'
    nd = 'nd'
    ne = 'ne'
    ng = 'ng'
    nl = 'nl'
    nn = 'nn'
    no = 'no'
    nr = 'nr'
    nv = 'nv'
    ny = 'ny'
    oc = 'oc'
    oj = 'oj'
    om = 'om'
    or_ = 'or'
    os = 'os'
    pa = 'pa'
    pi = 'pi'
    pl = 'pl'
    ps = 'ps'
    pt = 'pt'
    qu = 'qu'
    rm = 'rm'
    rn = 'rn'
    ro = 'ro'
    ru = 'ru'
    rw = 'rw'
    sa = 'sa'
    sc = 'sc'
    sd = 'sd'
    se = 'se'
    sg = 'sg'
    si = 'si'
    sk = 'sk'
    sl = 'sl'
    sm = 'sm'
    sn = 'sn'
    so = 'so'
    sq = 'sq'
    sr = 'sr'
    ss = 'ss'
    st = 'st'
    su = 'su'
    sv = 'sv'
    sw = 'sw'
    ta = 'ta'
    te = 'te'
    tg = 'tg'
    th = 'th'
    ti = 'ti'
    tk = 'tk'
    tl = 'tl'
    tn = 'tn'
    to = 'to'
    tr = 'tr'
    ts = 'ts'
    tt = 'tt'
    tw = 'tw'
    ty = 'ty'
    ug = 'ug'
    uk = 'uk'
    ur = 'ur'
    uz = 'uz'
    ve = 've'
    vi = 'vi'
    vo = 'vo'
    wa = 'wa'
    wo = 'wo'
    xh = 'xh'
    yi = 'yi'
    yo = 'yo'
    za = 'za'
    zh = 'zh'
    zu = 'zu'


class Language(BaseModel):
    root: Optional[LanguageEnum] = None


class StatisticalPopulationConstrained(Enum):
    PERSONS = 'PERSONS'
    EVENTS = 'EVENTS'
    FINDINGS = 'FINDINGS'


class Name(BaseModel):
    pass


class DataElement(BaseModel):
    class Config:
        extra = 'allow'

    name: Name = Field(
        ..., description='The name of a column in a table.', title='Column Name'
    )
    dataType: str = Field(
        ..., description='The data type of values in the column', title='Data Type'
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a column in a table.',
        title='Column Description',
    )
    sensitive: bool = Field(
        ...,
        description='A True or False value, indicating if the field is sensitive or not',
        title='Sensitive',
    )


class Revision(BaseModel):
    class Config:
        extra = 'forbid'

    version: Semver = Field(..., description='Semantic Version')
    url: Optional[Url] = Field(..., description='URL endpoint to obtain the version')


class Organisation(BaseModel):
    identifier: Optional[Url] = Field(
        None,
        description='Please provide a Grid.ac identifier (see https://www.grid.ac/institutes) for your organisation. If your organisation does not have a Grid.ac identifier please use the “suggest and institute” function here: https://www.grid.ac/institutes#',
        title='Organisation Identifier',
    )
    name: OneHundredFiftyCharacters = Field(
        ..., description='Name of the organisation', title='Organisation Name'
    )
    logo: Optional[Url] = Field(
        None,
        description='Please provide a logo associated with the Gateway Organisation using a valid URL. The following formats will be accepted .jpg, .png or .svg.',
        title='Organisation Logo',
    )
    description: Optional[Description] = Field(
        None,
        description='Please provide a URL that describes the organisation.',
        title='Organisation Description',
    )
    contactPoint: Union[Optional[EmailAddress], List[Optional[EmailAddress]]] = Field(
        ...,
        description='Organisation contact point(s)',
        title='Organisation Contact Point',
    )
    memberOf: Optional[MemberOf] = Field(
        None,
        description='Please indicate if the organisation is an Alliance Member or a Hub.',
        title='Organisation Membership',
    )
    accessRights: Optional[Union[Optional[Url], List[Optional[Url]]]] = Field(
        None,
        description='The URL of a webpage where the data access request process and/or guidance is provided. If there is more than one access process i.e. industry vs academic please provide both.',
        title='Organisation Default Access Rights',
    )
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None,
        description='Please provide an indication of the typical processing times based on the types of requests typically received. Note: This value will be used as default access request duration for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        title='Access Request Duration',
    )
    accessService: Optional[LongDescription] = Field(
        None,
        description='Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        examples=[
            'https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide'
        ],
        title='Organisation Access Service',
    )
    accessRequestCost: Optional[
        Union[Optional[ShortDescription], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide link(s) to a webpage or a short description detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.',
        title='Organisation Access Request Cost',
    )
    dataUseLimitation: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseLimitation]]
    ] = Field(
        None,
        description='Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Notes: where there are existing data-sharing arrangements such as the HDR UK HUB data sharing agreement or the NIHR HIC data sharing agreement this should be indicated within access rights. This value will be used as terms for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        title='Data Use Limitation',
    )
    dataUseRequirements: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseRequirements]]
    ] = Field(
        None,
        description='Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.',
        title='Data Use Requirements',
    )


class Documentation(BaseModel):
    class Config:
        extra = 'forbid'

    description: Optional[Description] = Field(
        None, description='A free-text description of the record.', title='Description'
    )
    associatedMedia: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide any media associated with the Gateway Organisation using a valid URI for the content. This is an opportunity to provide additional context that could be useful for researchers wanting to understand more about the dataset and its relevance to their research question. The following formats will be accepted .jpg, .png or .svg, .pdf, .xslx or .docx. Note: media asset can be hosted by the organisation or uploaded using the onboarding portal.',
        examples=['PDF Document that describes study protocol'],
        title='Associated Media',
    )
    isPartOf: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters, IsPartOfEnum]],
        ]
    ] = Field(
        'NOT APPLICABLE',
        description='Please complete only if the dataset is part of a group or family',
        examples=['Hospital Episodes Statistics datasets (A&E, APC, OP, AC MSDS).'],
        title='Group',
    )


class Coverage(BaseModel):
    class Config:
        extra = 'forbid'

    spatial: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(
        None,
        description='The geographical area covered by the dataset. It is recommended that links are to entries in a well-maintained gazetteer such as https://www.geonames.org/ or https://what3words.com/daring.lion.race.',
        examples=[
            'https://www.geonames.org/2635167/united-kingdom-of-great-britain-and-northern-ireland.html'
        ],
        title='Geographic Coverage',
    )
    typicalAgeRange: Optional[AgeRange] = Field(
        None,
        description="Please indicate the age range in whole years of participants in the dataset. Please provide range in the following format '[min age] – [max age]' where both the minimum and maximum are whole numbers (integers).",
        title='Age Range',
    )
    physicalSampleAvailability: Optional[
        Union[Optional[CommaSeparatedValues], List]
    ] = Field(
        None,
        description='Availability of physical samples associated with the dataset. If samples are available, please indicate the types of samples that are available. More than one type may be provided. If sample are not yet available, please provide “AVAILABILITY TO BE CONFIRMED”. If samples are not available, then please provide “NOT AVAILABLE”.',
        examples=['BONE MARROW'],
        title='Physical Sample Availability',
    )
    followup: Optional[Followup] = Field(
        'UNKNOWN',
        description='If known, what is the typical time span that a patient appears in the dataset (follow up period)',
        title='Followup',
    )
    pathway: Optional[Description] = Field(
        None,
        description='Please indicate if the dataset is representative of the patient pathway and any limitations the dataset may have with respect to pathway coverage. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tiers (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.',
        title='Pathway',
    )


class Origin(BaseModel):
    class Config:
        extra = 'forbid'

    purpose: Optional[Union[Optional[CommaSeparatedValues], List[Purpose]]] = Field(
        None,
        description='Pleases indicate the purpose(s) that the dataset was collected.',
        title='Purpose',
    )
    source: Optional[Union[Optional[CommaSeparatedValues], List[Source]]] = Field(
        None,
        description='Pleases indicate the source of the data extraction',
        title='Source',
    )
    collectionSituation: Optional[
        Union[Optional[CommaSeparatedValues], List[Setting]]
    ] = Field(
        None,
        description='Pleases indicate the setting(s) where data was collected. Multiple settings may be provided',
        title='Setting',
    )


class Temporal(BaseModel):
    class Config:
        extra = 'forbid'

    accrualPeriodicity: Periodicity = Field(
        ...,
        description='Please indicate the frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity. If a dataset has been published and will remain static please indicate that it is static and indicated when it was released. If a dataset is released on an irregular basis or “on-demand” please indicate that it is Irregular and leave release date as null. If a dataset can be published in real-time or near-real-time please indicate that it is continuous and leave release date as null. Notes: see https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/',
        title='Periodicity',
    )
    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None,
        description='Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity. If this is Irregular or Continuously released please leave this blank. Notes: Periodicity and release date will be used to determine when the next release is expected. E.g. if the release date is documented as 01/01/2020 and it is now 20/04/2020 and there is a quarterly release schedule, the latest release will be calculated as 01/04/2020.',
        title='Release Date',
    )
    startDate: Optional[Union[date, datetime]] = Field(
        ...,
        description='The start of the time period that the dataset provides coverage for. If there are multiple cohorts in the dataset with varying start dates, please provide the earliest date and use the description or the media attribute to provide more information.',
        title='Start Date',
    )
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None,
        description='The end of the time period that the dataset provides coverage for. If the dataset is “Continuous” and has no known end date, please state continuous. If there are multiple cohorts in the dataset with varying end dates, please provide the latest date and use the description or the media attribute to provide more information.',
        title='End Date',
    )
    timeLag: TimeLag = Field(
        ...,
        description='Please indicate the typical time-lag between an event and the data for that event appearing in the dataset',
        title='Time Lag',
    )


class Usage(BaseModel):
    class Config:
        extra = 'forbid'

    dataUseLimitation: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseLimitation]]
    ] = Field(
        None,
        description='Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. NOTE: we have extended the DUO to include a value for NO LINKAGE',
        title='Data Use Limitation',
    )
    dataUseRequirements: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseRequirements]]
    ] = Field(
        None,
        description='Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.',
        title='Data Use Requirements',
    )
    resourceCreator: Optional[
        Union[Optional[ShortDescription], List[Optional[ShortDescription]]]
    ] = Field(
        None,
        description='Please provide the text that you would like included as part of any citation that credits this dataset. This is typically just the name of the publisher.   No employee details should be provided.',
        title='Citation Requirements',
    )
    investigations: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(None, title='Investigations')
    isReferencedBy: Optional[Union[Optional[Doi], str, List[Optional[Doi]]]] = Field(
        None,
        description='Please provide the keystone paper associated with the dataset. Also include a list of known citations, if available and should be links to existing resources where the dataset has been used or referenced. Please provide multiple entries, or if you are using a csv upload please provide them as a tab separated list.',
        title='Citations',
    )


class Access(BaseModel):
    class Config:
        extra = 'forbid'

    accessRights: Union[
        constr(pattern=r'^In Progress$'), Optional[Url], List[Optional[Url]]
    ] = Field(..., title='Access Rights')
    accessService: Optional[LongDescription] = Field(
        None,
        description='Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        examples=[
            'https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide'
        ],
        title='Access Service',
    )
    accessRequestCost: Optional[
        Union[Optional[LongDescription], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide link(s) to a webpage detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.',
        title='Organisation Access Request Cost',
    )
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None,
        description='Please provide an indication of the typical processing times based on the types of requests typically received.',
        title='Access Request Duration',
    )
    jurisdiction: Union[Optional[CommaSeparatedValues], List[Isocountrycode]] = Field(
        ...,
        description="Please use country code from ISO 3166-1 country codes and the associated ISO 3166-2 for regions, cities, states etc. for the country/state under whose laws the data subjects' data is collected, processed and stored.",
        title='Jurisdiction',
    )
    dataController: Optional[LongDescription] = Field(
        ...,
        description='Data Controller means a person/entity who (either alone or jointly or in common with other persons/entities) determines the purposes for which and the way any Data Subject data, specifically personal data or are to be processed.',
        title='Data Controller',
    )
    dataProcessor: Optional[LongDescription] = Field(
        None,
        description='A Data Processor, in relation to any Data Subject data, specifically personal data, means any person/entity (other than an employee of the data controller) who processes the data on behalf of the data controller.',
        title='Data Processor',
    )


class FormatAndStandards(BaseModel):
    class Config:
        extra = 'forbid'

    vocabularyEncodingScheme: Union[
        Optional[CommaSeparatedValues], List[ControlledVocabulary]
    ] = Field(
        ...,
        description='List any relevant terminologies / ontologies / controlled vocabularies, such as ICD 10 Codes, NHS Data Dictionary National Codes or SNOMED CT International, that are being used by the dataset. If the controlled vocabularies are local standards, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition. Notes: More than one vocabulary may be provided.',
        title='Controlled Vocabulary',
    )
    conformsTo: Union[
        Optional[CommaSeparatedValues], List[StandardisedDataModels]
    ] = Field(
        ...,
        description='List standardised data models that the dataset has been stored in or transformed to, such as OMOP or FHIR. If the data is only available in a local format, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition.',
        title='Conforms To',
    )
    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ...,
        description='This should list all the languages in which the dataset metadata and underlying data is made available.',
        title='Language',
    )
    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ...,
        description='If multiple formats are available please specify. See application, audio, image, message, model, multipart, text, video, https://www.iana.org/assignments/media-types/media-types.xhtml Note: If your file format is not included in the current list of formats, please indicate other. If you are using the HOP you will be directed to a service desk page where you can request your additional format. If not please go to: https://metadata.atlassian.net/servicedesk/customer/portal/4 to request your format.',
        title='Format',
    )


class EnrichmentAndLinkage(BaseModel):
    class Config:
        extra = 'forbid'

    qualifiedRelation: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters]],
        ]
    ] = Field(
        None,
        description='If applicable, please provide the DOI of other datasets that have previously been linked to this dataset and their availability. If no DOI is available, please provide the title of the datasets that can be linked, where possible using the same title of a dataset previously onboarded to the HOP. Note: If all the datasets from Gateway organisation can be linked please indicate “ALL” and the onboarding portal will automate linkage across the datasets submitted.',
        title='Linked Datasets',
    )
    derivation: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[AbstractText]]]
    ] = Field(
        None,
        description='Indicate if derived datasets or predefined extracts are available and the type of derivation available. Notes. Single or multiple dimensions can be provided as a derived extract alongside the dataset.',
        title='Derivations',
    )
    tools: Optional[Union[Optional[CommaSeparatedValues], List[Optional[Url]]]] = Field(
        None,
        description='Please provide the URL of any analysis tools or models that have been created for this dataset and are available for further use. Multiple tools may be provided. Note: We encourage users to adopt a model along the lines of https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/',
        title='Tools',
    )


class Observation(BaseModel):
    class Config:
        extra = 'forbid'

    observedNode: StatisticalPopulationConstrained = Field(
        ...,
        description='Please select one of the following statistical populations for you observation',
        examples=['PERSONS'],
        title='Statistical Population',
    )
    measuredValue: int = Field(
        ...,
        description='Please provide the population size associated with the population type the dataset i.e. 1000 people in a study, or 87 images (MRI) of Knee Usage Note: Used with Statistical Population, which specifies the type of the population in the dataset.',
        title='Measured Value',
    )
    disambiguatingDescription: Optional[AbstractText] = Field(
        None,
        description='If SNOMED CT term does not provide sufficient detail, please provide a description that disambiguates the population type.',
        title='Disambiguating Description',
    )
    observationDate: Union[date, datetime] = Field(
        ...,
        description='Please provide the date that the observation was made. Some datasets may be continuously updated and the number of records will change regularly, so the observation date provides users with the date that the analysis or query was run to generate the particular observation. Multiple observations can be made i.e. an observation of cumulative COVID positive cases by specimen on the 1/1/2021 could be 2M. On the 8/1/2021 a new observation could be 2.1M. Users can add multiple observations.',
        title='Observation Date',
    )
    measuredProperty: MeasuredProperty = Field(
        ...,
        description='Initially this will be defaulted to "COUNT"',
        title='Measured Property',
    )


class DataClass(BaseModel):
    class Config:
        extra = 'forbid'

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        ..., description='The name of a table in a dataset.', title='Table Name'
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a table in a dataset.',
        title='Table Description',
    )
    elements: List[DataElement] = Field(
        ...,
        description='A list of data elements contained within a table in a dataset.',
        title='Data Elements',
    )




class Provenance(BaseModel):
    class Config:
        extra = 'forbid'

    origin: Optional[Origin] = None
    temporal: Temporal


class Accessibility(BaseModel):
    class Config:
        extra = 'forbid'

    usage: Optional[Usage] = Field(
        None,
        description='This section includes information about how the data can be used and how it is currently being used',
        title='Usage',
    )
    access: Access = Field(
        ...,
        description='This section includes information about data access',
        title='Access',
    )
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        description='Section includes technical attributes for language vocabularies, sizes etc. and gives researchers facts about and processing the underlying data in the dataset.',
        title='Format and Standards',
    )



if __name__ == '__main__':
    import json
    with open('schema.json','w') as f:
        json.dump(HdrUkDatasetSchema.model_json_schema(),f,indent=6)
