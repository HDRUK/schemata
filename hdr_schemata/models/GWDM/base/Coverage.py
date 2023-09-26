from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

class Coverage(BaseModel):

    #note: limit these to country codes?
    #      what about regions? surely it's more interesting to know:
    #      scotland:lothian, england:yorkshire, etc. 
    spatial: Optional[CommaSeparatedValues] = Field(
        None,
        description="List of countries where the data was taken from",
        example="United Kingdom,Wales,England",
        title='Spatial'
    )


    #note: limit these instead of arbitrary CommaSeparatedValues
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/PhysicalSampleAvailability.py
    #note: this would also be useful to know in a bit more detail, and not always 'sample'
    #      e.g.: <WHAT SAMPLE>::<WHAT MEASURED>::<HOW> ... SERUM::IgG::Abbott
    #note: What about measurements (e.g. serum anti-IgG to SARs-CoV-2)?
    #      What about drug exposures (e.g. vaccine AZ)?
    #      What about medicine given (e.g. diazepam) ?
    #      What about observations (e.g. smoker)?
    physicalSampleAvailability: Optional[CommaSeparatedValues] = Field(
        None,
        description="A list of what the dataset actually contains in terms of sample measurements",
        example="DNA,PLASMA,SERUM,URINE,WHOLE BLOOD",
        title='Physical Sample Availability'
    )

    #note: missing coverage of the types of people the dataset is covering?
    #      diabetes, cancer, care home residents, smokers, etc. etc.
    #      i.e. not just the 'sample'
    #
    #Could do something OMOP-like:
    # measurements: Optional[CommaSeparatedValues]
    # drugs: Optional[CommaSeparatedValues]
    # observations: Optional[CommaSeparatedValues]
    
    #note: is this appropriate in this coverage section?
    pathway: Optional[LongDescription] = Field(
        None,
        description="Long description of the clinical/diagnostic/treatment pathway if applicable. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tier (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.",
        example= "The lookup contains references to link data held elsewhere on:\n• individuals appearing as defendants in criminal cases dealt with by the magistrates' or Crown Court in England and Wales (including Youth Courts). \n• individuals supervised by the probation service in England and Wales\n• individuals serving custodial sentences in England & Wales who appear within records from the prison data source, p-NOMIS. Young Offenders are included if resident at prisons or Young Offender Institutes (YOIs) that use p-NOMIS, however, this excludes the majority of Secure Schools and Secure Training Centres. \"\n\n\"The linking dataset includes a person ID and link to record in other data first datasets for: \n• Disposals in the magistrates’ court from 1 January 2011 to 31 December 2020\n• Disposals in the Crown Court from 1 January 2013 to 31 December 2020\n• Custodial sentences of offenders in custody from January 2011 to September 2021 (including sentences begun before 2011) \n• Offender probation records from January 2014 to December 2020."
        title='Pathway'
    )

    #note: May need to update/modify:
    #      https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Followup.py
    followup: Optional[Followup] = Field(
        None,
        description="What is the typical time span that a patient appears in the dataset (follow up period)",
        example="CONTINUOUS",
        title='Followup'
    )

    #note: not sure if this is the best way of doing it
    #      ask for age: low, median, high instead?
    #      allowing [0-150] is not useful ...
    typicalAgeRange: Optional[AgeRange] = Field(
        None,
        description="Age range in whole years of participants in the dataset. Please provide range in the following format '[min age] – [max age]' where both the minimum and maximum are whole numbers (integers).",
        example="1-150",
        title='Typical Age Range'
    )

