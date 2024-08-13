from pydantic import BaseModel
from enum import Enum

class EthnicityBin(Enum):
    WHITE___BRITISH = 'White - British'
    WHITE___IRISH = 'White - Irish'
    WHITE___ANY_OTHER_WHITE_BACKGROUND = 'White - Any other White background'
    MIXED___WHITE_AND_BLACK_CARIBBEAN = 'Mixed - White and Black Caribbean'
    MIXED___WHITE_AND_BLACK_AFRICAN = 'Mixed - White and Black African'
    MIXED___WHITE_AND_ASIAN = 'Mixed - White and Asian'
    MIXED___ANY_OTHER_MIXED_BACKGROUND = 'Mixed - Any other mixed background'
    ASIAN_OR_ASIAN_BRITISH___INDIAN = 'Asian or Asian British - Indian'
    ASIAN_OR_ASIAN_BRITISH___PAKISTANI = 'Asian or Asian British - Pakistani'
    ASIAN_OR_ASIAN_BRITISH___BANGLADESHI = 'Asian or Asian British - Bangladeshi'
    ASIAN_OR_ASIAN_BRITISH___ANY_OTHER_ASIAN_BACKGROUND = 'Asian or Asian British - Any other Asian background'
    BLACK_OR_BLACK_BRITISH___CARIBBEAN = 'Black or Black British - Caribbean'
    BLACK_OR_BLACK_BRITISH___AFRICAN = 'Black or Black British - African'
    BLACK_OR_BLACK_BRITISH___ANY_OTHER_BLACK_BACKGROUND = 'Black or Black British - Any other Black background'
    OTHER_ETHNIC_GROUPS___CHINESE = 'Other Ethnic Groups - Chinese'
    OTHER_ETHNIC_GROUPS___ANY_OTHER_ETHNIC_GROUP = 'Other Ethnic Groups - Any other ethnic group'
    NOT_STATED = 'Not stated'
    NOT_KNOWN = 'Not known'

class Ethnicity(BaseModel):
    bin: EthnicityBin
    count: int
