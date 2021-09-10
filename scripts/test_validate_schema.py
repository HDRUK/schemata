from os import P_WAIT
from re import A
from typing import ItemsView
import pytest
from validate_schema import *
from unittest import TestCase

REPORTING_ATTRIBUTES = {
    "person attributes": [
        "identifier",
        "firstName",
        "lastName",
        "email",
        "sector",
        "organisation",
        "bio",
        "domain",
        "link",
        "orcid",
    ]
}

REPORTING_LEVELS = ["person attributes"]

expected_dict_for_attribute_completeness = {
    "person attributes": {
        "identifier": 1,
        "firstName": 1,
        "lastName": 1,
        "email": 1,
        "sector": 1,
        "organisation": 1,
        "bio": 1,
        "domain": 1,
        "link": 1,
        "orcid": 1,
        "filled_attributes": 10,
        "total_attributes": 10,
    },
    "filled_attributes": 10,
    "total_attributes": 10,
}


expected_dict_for_item_completeness = {
    "identifier": "https://web.www.healthdatagateway.org/person/8101920551208412",
    "name": None,
    "person attributes": {
        "identifier": 1,
        "firstName": 1,
        "lastName": 1,
        "email": 1,
        "sector": 1,
        "organisation": 1,
        "bio": 1,
        "domain": 1,
        "link": 1,
        "orcid": 1,
        "filled_attributes": 10,
        "total_attributes": 10,
    },
    "filled_attributes": 10,
    "total_attributes": 10,
}

# CASE 1: All fields are present 100% completeness
class Test_CaseOne:
    def test_check_attribute_completeness(self):
        """Test to check if the attribute is complete"""

        item = {
            "identifier": "https://web.www.healthdatagateway.org/person/8101920551208412",
            "firstName": "Gerry",
            "lastName": "Reilly",
            "email": "Gerry.Reilly@hdruk.ac.uk",
            "sector": "Industry",
            "organisation": "HDRUK",
            "bio": "Technologist in Residence, HDR UK",
            "domain": ["Software Engineering", "Data Management"],
            "link": "https://www.linkedin.com/in/gerry-reilly-7290681/",
            "orcid": "https://orcid.org/0000-0003-1427-3598",
        }

        global REPORTING_ATTRIBUTES

        global REPORTING_LEVELS

        output = check_attribute_completeness(
            item, REPORTING_ATTRIBUTES, REPORTING_LEVELS
        )  # Run function
        print(output)
        assert output == expected_dict_for_attribute_completeness  # Compare results

    # def test_check_item_completeness(self):
    #     """Test to check if the item is complete"""

    #     item_type = "person"
    #     items = {
    #         "identifier": "https://web.www.healthdatagateway.org/person/8101920551208412",
    #     "firstName": "Gerry",
    #     "lastName": "Reilly",
    #     "email": "gerry.reilly@hdruk.ac.uk",
    #     "sector": "Industry",
    #     "organisation": "HDRUK",
    #     "bio": "Technologist in Residence, HDR UK",
    #     "domain": ["Software Engineering", "Data Management"],
    #     "link": "https://www.linkedin.com/in/gerry-reilly-7290681/",
    #     "orcid": "https://orcid.org/0000-0003-1427-3598",
    # }
    # global REPORTING_ATTRIBUTES
    # global REPORTING_LEVELS

    # output = check_item_completeness(
    #     item_type, items, REPORTING_ATTRIBUTES, REPORTING_LEVELS
    # )  # Run function

    # assert output == expected_dict_for_item_completeness  # Compare results

    # def test_check_attribute_validation(self):
    #     """Test to check if the item is complete"""

    #     item_type = "person"
    #     items = {
    #         "identifier": "https://web.www.healthdatagateway.org/person/8101920551208412",
    #         "firstName": "Gerry",
    #         "lastName": "Reilly",
    #         "email": "gerry.reilly@hdruk.ac.uk",
    #         "sector": "Industry",
    #         "organisation": "HDRUK",
    #         "bio": "Technologist in Residence, HDR UK",
    #         "domain": ["Software Engineering", "Data Management"],
    #         "link": "https://www.linkedin.com/in/gerry-reilly-7290681/",
    #         "orcid": "https://orcid.org/0000-0003-1427-3598",
    #     }

    #     schema =
    #     global REPORTING_ATTRIBUTES
    #     global REPORTING_LEVELS

    #     output = check_item_completeness(
    #         item_type, items, REPORTING_ATTRIBUTES, REPORTING_LEVELS
    #     )  # Run function

    #     assert output == expected_dict_for_item_completeness  # Compare results
