from enum import Enum

class FollowUpFrequency(Enum):
    NONE = 'No scheduled follow-up'
    IRREGULAR = 'Irregular'
    ANNUAL = 'Annual'
    BIENNIAL = 'Biennial'
    THREE_TO_FIVE_YEARS = 'Every 3-5 years'
    MORE_THAN_FIVE_YEARS = 'Every 5+ years'
    CONTINUOUS = 'Continuous'
    OTHER = 'Other'
