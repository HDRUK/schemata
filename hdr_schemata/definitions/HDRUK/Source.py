from enum import Enum

class Source(Enum):
    EPR = 'EPR'
    ELECTRONIC_SURVEY = 'ELECTRONIC SURVEY'
    LIMS = 'LIMS'
    OTHER_INFORMATION_SYSTEM = 'OTHER INFORMATION SYSTEM'
    PAPER_BASED = 'PAPER BASED'
    FREETEXT_NLP = 'FREETEXT NLP'
    MACHINE_GENERATED = 'MACHINE GENERATED'
    OTHER = 'OTHER'

class SourceV2(Enum):
    EPR = 'EPR'
    ELECTRONIC_SURVEY = 'Electronic survey'
    LIMS = 'LIMS'
    PAPER_BASED = 'Paper-based'
    FREE_TEXT_NLP = 'Free text NLP'
    MACHINE_GENERATED = 'Machine generated'
    OTHER = 'Other'
