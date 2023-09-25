from pydantic import BaseModel,Field,constr,AnyUrl
from typing import Optional,List,Union

class Text(constr):
    pass

class Url(AnyUrl):
    pass

class Citation(BaseModel):
    _type: Text = Field(alias="@type", default="Dataset")
    headline: Text
    identifier: List[Text]
    datePublished: Text

class Person(BaseModel):
    _type: Text = Field(alias="@type", default="Person")
    givenName: Text
    familyName: Text
    email: Text
    affiliation: Text
    
class Organization(BaseModel):
    _type: Text = Field(alias="@type", default="Organization")
    name: Text
    _id: Text = Field(alias="@id")

class DataDownload(BaseModel):
    _type: Text = Field(alias="@type", default="DataDownload")
    name: Text
    fileFormat: Text
    contentURL: Text

class DataCatalog(BaseModel):
    _type: Text = Field(alias="@type", default="DataCatalog")
    name: Text
    url: Text

class DefinedTerm(BaseModel):
    name: Text
    id: Text

class Organization(BaseModel):
    name: Text
    id: Optional[Text] = None

class BioschemaDataset(BaseModel):
    alternateName: Optional[List[Text]] = None
    citation: Optional[Citation] = None
    creator: List[Union[Person,Organization]] = []
    datePublished: Text
    description: Text
    distribution: List[DataDownload] = []
    identifier: Text
    includedInDataCatalog: Optional[DataCatalog] = None
    isBasedOn: Optional[Text] = None
    keywords: List[Union[DefinedTerm,Text,Url]] = []
    license: Url
    measurementTechnique: Text
    name: Text
    publisher: Union[Organization,Person]
    url: Url
    variableMeasured: Text
    version: Text

    

if __name__ == "__main__":
    import json
    with open('schema.json','w') as f:
        json.dump(BioschemaDataset.model_json_schema(),f,indent=6)
