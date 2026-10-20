from enum import Enum

class RecruitmentStatus(Enum):
    NOT_YET_RECRUITING = 'Not yet recruiting'
    RECRUITING = 'Recruiting'
    CLOSED = 'Closed'
    UNKNOWN = 'Unknown'
