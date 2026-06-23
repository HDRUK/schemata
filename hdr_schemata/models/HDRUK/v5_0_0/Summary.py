from typing import List, Optional

from pydantic import AnyUrl, Field

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues, OneHundredFiftyCharacters, ShortTitle, Url
from hdr_schemata.models.HDRUK.v4_0_0.Summary import Summary as Summary400

from .Creator import Creator


class Summary(Summary400):

    shortTitle: Optional[ShortTitle] = Field(
        None,
        title="Short Title",
        description="Abbreviated or acronym title for the dataset, used in list/card views.",
    )

    licenseUrl: Optional[Url] = Field(
        None,
        title="Licence URL",
        description="URI of the dataset-level licence (dct:license). Use a recognised licence URI such as https://creativecommons.org/licenses/by/4.0/.",
    )

    landingPage: Optional[Url] = Field(
        None,
        title="Landing Page",
        description="URL of a human-readable landing page for the dataset (dcat:landingPage).",
    )

    creator: Optional[Creator] = Field(
        None,
        title="Creator",
        description="Entity responsible for originally creating the dataset (dct:creator). May differ from the data custodian.",
    )

    theme: Optional[List[AnyUrl]] = Field(
        None,
        title="Theme",
        description="Array of controlled vocabulary concept URIs categorising the dataset by subject area (dcat:theme). Use EuroVoc or NHS Data Dictionary URIs where available.",
    )

    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        None,
        title="Controlled Keywords",
        description="Curated subset of keywords drawn from a controlled vocabulary. Complements free-text keywords.",
    )
