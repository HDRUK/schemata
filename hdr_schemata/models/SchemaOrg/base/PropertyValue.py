from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text, Number


class PropertyValue(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="PropertyValue"
    )


    maxValue: Optional[Number] = Field(
        None,
        description=r'''The upper value of some characteristic or property.'''
    )
    
    #measurementMethod: Optional[Union[DefinedTerm, MeasurementMethodEnum, Text, AnyUrl]] = Field(
    measurementMethod: Optional[Union[Text, AnyUrl]] = Field(
        None,
        description=r'''A subproperty of measurementTechnique that can be used for specifying specific methods, in particular via MeasurementMethodEnum.'''
    )
    
    #measurementTechnique: Optional[Union[DefinedTerm, MeasurementMethodEnum, Text, AnyUrl]] = Field(
    measurementTechnique: Optional[Union[Text, AnyUrl]] = Field(
        None,
        description=r'''A technique, method or technology used in an Observation, StatisticalVariable or Dataset (or DataDownload, DataCatalog), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using variableMeasured; for Observation, a StatisticalVariable). Often but not necessarily each variableMeasured will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of variableMeasured called measuredProperty is applicable.
        
        The measurementTechnique property helps when extra clarification is needed about how a measuredProperty was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. 
        
        For example, if variableMeasured is: molecule concentration, measurementTechnique could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the variableMeasured is "depression rating", the measurementTechnique could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". 
        
        If there are several variableMeasured properties recorded for some given data object, use a PropertyValue for each variableMeasured and attach the corresponding measurementTechnique. The value can also be from an enumeration, organized as a MeasurementMetholdEnumeration.'''
    )
    
    minValue: Optional[Number] = Field(
        None,
        description=r'''The lower value of some characteristic or property.'''
    )
    
    propertyID: Optional[Union[Text, AnyUrl]] = Field(
        None,
        description=r'''A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be
        (1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific ID of the property), or (3)
        a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).
        Standards bodies should promote a standard prefix for the identifiers of properties from their standards.'''
    )
    
    unitCode: Optional[Union[Text, AnyUrl]] = Field(
        None,
        description=r'''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.'''
    )
    
    unitText: Optional[Text] = Field(
        None,
        description=r'''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
        unitCode.'''
    )
    
    value: Optional[Text] = Field(
        # value: Optional[Union[Boolean, Number, StructuredValue, Text]] = Field(
        None,
        description=r'''The value of a QuantitativeValue (including Observation) or property value node.
        
        For QuantitativeValue and MonetaryAmount, the recommended type for values is 'Number'.
        For PropertyValue, it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.
        Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
    Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.'''
    )

    #valueReference: Optional[Union[DefinedTerm, Enumeration, MeasurementTypeEnumeration, PropertyValue, QualitativeValue, QuantitativeValue, StructuredValue, Text]] = Field(
    valueReference: Optional[Text] = Field(
        None,
        description=r'''A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.'''
)
