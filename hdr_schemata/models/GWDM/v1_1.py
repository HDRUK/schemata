from hdr_schemata.models.GWDM import Gwdm10
from hdr_schemata.models.GWDM.base import Coverage as BaseCoverage
from hdr_schemata.definitions.HDRUK import LongDescription,CommaSeparatedValues
import re
from typing import Optional,List
from pydantic import Field, BaseModel, RootModel, constr

#'Anthropometric': ['waist circumference', 'weight', 'blood pressure', 'hip circumference', 'height'], 'Physical': ['respiratory', 'vision', 'hearing ', 'musculoskeletal', 'cardiovascular', 'reproductive'], 'Psychological': ['cognitive function', 'mental health'], 'Lifestyle': ['Smoking', 'dietary habits', 'physical activity', 'alcohol', 'smoking'], 'Socio-economic': ['finances', 'family circumstances', 'housing', 'education', 'marital status', 'occupation', 'ethnic group', 'social support'], 'Biological samples': ['blood', 'other', 'urine', 'saliva']}

def get_pattern(allowed_phrases):
    return r'\b(?:' + '|'.join(allowed_phrases) + r')(?:,(?:' + '|'.join(allowed_phrases) + r'))*\b'
    
class Lifestyles(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Smoking',
            'Dietary Habits',
            'Physical Activity',
            'Alcohol'
        ]))]

class SocioEconomic(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Finances',
            'Family Circumstances',
            'Housing',
            'Education',
            'Marital Status',
            'Occupation',
            'Ethnic Group',
            'Social Support'
        ]))]
    

class Coverage(BaseCoverage):
    lifestyle: Optional[Lifestyles] = Field(
        None,
        title='Lifestyle',
        description='Cohort lifestyle habits: Smoking, Physical activity, Dietary habits, Alcohol'
    )
    

    socioeconomic: Optional[SocioEconomic] = Field(
        None,
        title='Socio-economic',
        description='Description of Occupation, Family circumstances, Housing, Education, Ethnic group, Martial status, Social support'
    )


class Gwdm11(Gwdm10):
    #overload Coverage with an updated version of it.. 
    coverage: Optional[Coverage] = Field(
        None,
        description='Spatial and Temporal coverage',
        title='Coverage',
    )


#data = {'lifestyle':'Smoking, Alcohol ,Dietary Habits'}
#Coverage(**data)


