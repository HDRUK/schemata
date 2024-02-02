from enum import Enum


class TissueCollectionTypeEnum(Enum):
    CASE_CONTROL = "Case-control"
    COHORT = "Cohort"
    CROSS_SECTIONAL = "Cross-sectional"
    LONGITUDINAL = "Longitudinal"
    TWIN_STUDY = "Twin-study"
    QUALITY_CONTROL = "Quality control"
    POPULATION_BASED = "Population-based"
    DISEASE_SPECIFIC = "Disease specific"
    BIRTH_COHORT = "Birth cohort"
    OTHER = "Other"
