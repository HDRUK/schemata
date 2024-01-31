from enum import Enum


class AnthropometricType(Enum):
    BLOOD_PRESSURE = "Blood Pressure"
    HIP_CIRCUMFERENCE = "Hip Circumference"
    HEIGHT = "Height"
    WAIST_CIRCUMFERENCE = "Waist Circumference"
    WEIGHT = "Weight"


class BiologicalSampleType(Enum):
    BLOOD = "Blood"
    OTHER = "Other"
    URINE = "Urine"
    SALIVA = "Saliva"


class PhysicalType(Enum):
    RESPIRATORY = "Respiratory"
    VISION = "Vision"
    HEARING = "Hearing"
    MUSCULOSKELETAL = "Musculoskeletal"
    CARDIOVASCULAR = "Cardiovascular"
    REPRODUCTIVE = "Reproductive"


class PsychologicalType(Enum):
    COGNITIVE_FUNCTION = "Cognitive Function"
    MENTAL_HEALTH = "Mental Health"


class LifestylesType(Enum):
    SMOKING = "Smoking"
    DIETARY_HABITS = "Dietary Habits"
    PHYSICAL_ACTIVITY = "Physical Activity"
    ALCOHOL = "Alcohol"


class GenderType(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class SocioEconomicType(Enum):
    FINANCES = "Finances"
    FAMILY_CIRCUMSTANCES = "Family Circumstances"
    HOUSING = "Housing"
    EDUCATION = "Education"
    MARITAL_STATUS = "Marital Status"
    OCCUPATION = "Occupation"
    ETHNIC_GROUP = "Ethnic Group"
    SOCIAL_SUPPORT = "Social Support"
