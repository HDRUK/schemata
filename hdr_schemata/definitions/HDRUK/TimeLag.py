from enum import Enum

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

class TimeLagV2(Enum):
    LESS_THAN_1_WEEK = 'Less than 1 week'
    ONE_TWO_WEEKS = '1-2 weeks'
    TWO_FOUR_WEEKS = '2-4 weeks'
    ONE_TWO_MONTHS = '1-2 months'
    TWO_SIX_MONTHS = '2-6 months'
    SIX_MONTHS_PLUS = '6 months plus'
    VARIABLE = 'Variable'
    NOT_APPLICABLE = 'Not applicable'
    OTHER = 'Other'

