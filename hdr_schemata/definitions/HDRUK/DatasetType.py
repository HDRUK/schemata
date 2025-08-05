from typing import Optional, List, Union
from pydantic import BaseModel, Field, RootModel, constr
from enum import Enum

#note: contructed as a string of max_length=100
#      in the future we may want to limit this with Enums
class DatasetType(RootModel):
    root: Optional[constr(min_length=2, max_length=100)]

class DatasetTypeV2(Enum):
    HEALTH_AND_DISEASE = 'Health and disease'
    TREATMENTS_INTERVENTIONS = 'Treatments/Interventions'
    MEASUREMENTS_TESTS = 'Measurements/Tests'
    IMAGING_TYPES = 'Imaging types'
    IMAGING_AREA_OF_THE_BODY = 'Imaging area of the body'
    OMICS = 'Omics'
    SOCIOECONOMIC = 'Socioeconomic'
    LIFESTYLE = 'Lifestyle'
    REGISTRY = 'Registry'
    ENVIRONMENT_AND_ENERGY = 'Environment and energy'
    INFORMATION_AND_COMMUNICATION = 'Information and communication'
    POLITICS = 'Politics'

class DatasetSubType(Enum):
    MENTAL_HEALTH = 'Mental health'
    CARDIOVASCULAR = 'Cardiovascular'
    CANCER = 'Cancer'
    RARE_DISEASES = 'Rare diseases'
    METABOLIC_AND_ENDOCRINE = 'Metabolic and endocrine'
    NEUROLOGICAL = 'Neurological'
    REPRODUCTIVE = 'Reproductive'
    MATERNITY_AND_NEONATOLOGY = 'Maternity and neonatology'
    RESPIRATORY = 'Respiratory'
    IMMUNITY = 'Immunity'
    MUSCULOSKELETAL = 'Musculoskeletal'
    VISION = 'Vision'
    RENAL_AND_UROGENITAL = 'Renal and urogenital'
    ORAL_AND_GASTROINTESTINAL = 'Oral and gastrointestinal'
    COGNITIVE_FUNCTION = 'Cognitive function'
    HEARING = 'Hearing'
    OTHERS = 'Others'
    # OTHERS = 'Others'
    VACCINES = 'Vaccines'
    PREVENTIVE = 'Preventive'
    THERAPEUTIC = 'Therapeutic'
    # OTHERS = 'Others'
    LABORATORY = 'Laboratory'
    OTHER_DIAGNOSTICS = 'Other diagnostics'
    # OTHERS = 'Others'
    CT = 'CT'
    MRI = 'MRI'
    PET = 'PET'
    X_RAY = 'X-ray'
    ULTRASOUND = 'Ultrasound'
    PATHOLOGY = 'Pathology'
    # OTHERS = 'Others'
    HEAD = 'Head'
    CHEST = 'Chest'
    ARM = 'Arm'
    ABDOMEN = 'Abdomen'
    LEG = 'Leg'
    # OTHERS = 'Others'
    PROTEOMICS = 'Proteomics'
    TRANSCRIPTOMICS = 'Transcriptomics'
    EPIGENOMICS = 'Epigenomics'
    METABOLOMICS = 'Metabolomics'
    METAGENOMICS = 'Metagenomics'
    GENOMICS = 'Genomics'
    LIPIDOMICS = 'Lipidomics'
    # OTHERS = 'Others'
    EDUCATION = 'Education'
    CRIME_AND_JUSTICE = 'Crime and justice'
    ETHNICITY = 'Ethnicity'
    HOUSING_ = 'Housing'
    LABOUR = 'Labour'
    AGEING = 'Ageing'
    ECONOMICS = 'Economics'
    MARITAL_STATUS = 'Marital status'
    SOCIAL_SUPPORT = 'Social support'
    DEPRIVATION = 'Deprivation'
    RELIGION = 'Religion'
    OCCUPATION = 'Occupation'
    FINANCES = 'Finances'
    FAMILY_CIRCUMSTANCE = 'Family circumstance'
    # OTHERS = 'Others'
    SMOKING = 'Smoking'
    PHYSICAL_ACTIVITY = 'Physical activity'
    DIETARY_HABITS = 'Dietary habits'
    ALCOHOL = 'Alcohol'
    # OTHERS = 'Others'
    DISEASE_REGISTRY_RESEARCH = 'Disease registry (research)'
    NATIONAL_DISEASE_REGISTRIES_AND_AUDITS = 'National disease registries and audits'
    BIRTHS_AND_DEATHS = 'Births and deaths'
    # OTHERS = 'Others'
    NOT_APPLICABLE = 'Not applicable'


class HealthAndDiseaseSubTypes(Enum):
    MENTAL_HEALTH = 'Mental health'
    CARDIOVASCULAR = 'Cardiovascular'
    CANCER = 'Cancer'
    RARE_DISEASES = 'Rare diseases'
    METABOLIC_AND_ENDOCRINE = 'Metabolic and endocrine'
    NEUROLOGICAL = 'Neurological'
    REPRODUCTIVE = 'Reproductive'
    MATERNITY_AND_NEONATOLOGY = 'Maternity and neonatology'
    RESPIRATORY = 'Respiratory'
    IMMUNITY = 'Immunity'
    MUSCULOSKELETAL = 'Musculoskeletal'
    VISION = 'Vision'
    RENAL_AND_UROGENITAL = 'Renal and urogenital'
    ORAL_AND_GASTROINTESTINAL = 'Oral and gastrointestinal'
    COGNITIVE_FUNCTION = 'Cognitive function'
    HEARING = 'Hearing'
    OTHERS = 'Others'

class HealthAndDisease(BaseModel):
    name: str = Field("Health and disease", Literal=True)
    subTypes: Optional[List[HealthAndDiseaseSubTypes]]


class TreatmentsInterventionsSubTypes(Enum):
    VACCINES = 'Vaccines'
    PREVENTIVE = 'Preventive'
    THERAPEUTIC = 'Therapeutic'
    OTHERS = 'Others'

class TreatmentsInterventions(BaseModel):
    name: str = Field("Treatments/Interventions", Literal=True)
    subTypes: Optional[List[TreatmentsInterventionsSubTypes]]

class MeasurementsTestsSubTypes(Enum):
    LABORATORY = 'Laboratory'
    OTHER_DIAGNOSTICS = 'Other diagnostics'

class MeasurementsTests(BaseModel):
    name: str = Field("Measurements Tests", Literal=True)
    subTypes: Optional[List[MeasurementsTestsSubTypes]]

class ImagingTypesSubTypes(Enum):
    CT = 'CT'
    MRI = 'MRI'
    PET = 'PET'
    X_RAY = 'X-ray'
    ULTRASOUND = 'Ultrasound'
    PATHOLOGY = 'Pathology'
    OTHERS = 'Others'

class ImagingTypes(BaseModel):
    name: str = Field("Imaging Types", Literal=True)
    subTypes: Optional[List[ImagingTypesSubTypes]]

class ImagingAreaOfTheBodySubTypes(Enum):
    HEAD = 'Head'
    CHEST = 'Chest'
    ARM = 'Arm'
    ABDOMEN = 'Abdomen'
    LEG = 'Leg'
    OTHERS = 'Others'

class ImagingAreaOfTheBody(BaseModel):
    name: str = Field("Imaging Area Of The Body", Literal=True)
    subTypes: Optional[List[ImagingAreaOfTheBodySubTypes]]

class OmicsDataTypeSubTypes(Enum):
    PROTEOMICS = 'Proteomics'
    TRANSCRIPTOMICS = 'Transcriptomics'
    EPIGENOMICS = 'Epigenomics'
    METABOLOMICS = 'Metabolomics'
    METAGENOMICS = 'Metagenomics'
    GENOMICS = 'Genomics'
    LIPIDOMICS = 'Lipidomics'
    OTHERS = 'Others'

class OmicsDataType(BaseModel):
    name: str = Field("Omics DataType", Literal=True)
    subTypes: Optional[List[OmicsDataTypeSubTypes]]

class SocioeconomicSubTypes(Enum):
    EDUCATION = 'Education'
    CRIME_AND_JUSTICE = 'Crime and justice'
    ETHNICITY = 'Ethnicity'
    HOUSING_ = 'Housing'
    LABOUR = 'Labour'
    AGEING = 'Ageing'
    ECONOMICS = 'Economics'
    MARITAL_STATUS = 'Marital status'
    SOCIAL_SUPPORT = 'Social support'
    DEPRIVATION = 'Deprivation'
    RELIGION = 'Religion'
    OCCUPATION = 'Occupation'
    FINANCES = 'Finances'
    FAMILY_CIRCUMSTANCE = 'Family circumstance'
    OTHERS = 'Others'

class Socioeconomic(BaseModel):
    name: str = Field("Socioeconomic", Literal=True)
    subTypes: Optional[List[SocioeconomicSubTypes]]

class LifestyleSubTypes(Enum):
    SMOKING = 'Smoking'
    PHYSICAL_ACTIVITY = 'Physical activity'
    DIETARY_HABITS = 'Dietary habits'
    ALCOHOL = 'Alcohol'
    OTHERS = 'Others'

class Lifestyle(BaseModel):
    name: str = Field("Lifestyle", Literal=True)
    subTypes: Optional[List[LifestyleSubTypes]]

class RegistrySubTypes(Enum):
    DISEASE_REGISTRY_RESEARCH = 'Disease registry (research)'
    NATIONAL_DISEASE_REGISTRIES_AND_AUDITS = 'National disease registries and audits'
    BIRTHS_AND_DEATHS = 'Births and deaths'
    OTHERS = 'Others'

class Registry(BaseModel):
    name: str = Field("Registry", Literal=True)
    subTypes: Optional[List[RegistrySubTypes]]

class NotApplicableSubTypes(Enum):
    NOT_APPLICABLE = 'Not applicable'

class EnvironmentAndEnergy(BaseModel):
    name: str = Field("Environment and energy", Literal=True)
    subTypes: Optional[List[NotApplicableSubTypes]]

class InformationAndCommunication(BaseModel):
    name: str = Field("Information and communication", Literal=True)
    subTypes: Optional[List[NotApplicableSubTypes]]

class Politics(BaseModel):
    name: str = Field("Politics", Literal=True)
    subTypes: Optional[List[NotApplicableSubTypes]]

class DatasetTypeV3(BaseModel):
    dataType: Union[
        HealthAndDisease, 
        TreatmentsInterventions, 
        MeasurementsTests, 
        ImagingTypes,
        ImagingAreaOfTheBody,
        OmicsDataType,
        Socioeconomic,
        Lifestyle,
        Registry,
        EnvironmentAndEnergy,
        InformationAndCommunication,
        Politics
    ]