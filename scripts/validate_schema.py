# IMPORTS
import os
import json
import requests
from jsonschema import Draft7Validator, draft7_format_checker
import copy
import argparse
import re

# JSON_PATH = 'examples/tools/test/tools_test.json'


def get_json(json_uri):
    if isinstance(json_uri, dict):
        return json_uri
    elif os.path.isfile(json_uri):
        with open(json_uri, "r") as json_file:
            return json.load(json_file)
    elif json_uri.startswith("http"):
        return requests.get(json_uri).json()
    else:
        raise Exception


def export_json(data, filename, indent=2):
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=indent)


def validate_attribute_schema(schema, item):
    """validate each attribute against JSON schema
    @param schema: JSON validation schema
    @param item: uploaded item in list of items (e.g. each tool in the tools collection)
    @return: dictionary with all schema errors
    """
    schema = get_json(schema)

    v = Draft7Validator(schema, format_checker=draft7_format_checker)

    errors = sorted(v.iter_errors(item), key=lambda e: e.path)

    print(item["identifier"], ": Number of validation errors = ", len(errors))
    err = {}
    for error in errors:

        if len(list(error.path)):
            attribute = list(error.path)[0]
            err.setdefault(attribute, []).append(error.message)
            print(attribute, error.message, sep=": ")
        else:
            print(error.message)
            attribute = re.findall(r"(.*?)'", error.message)[1]
            err.setdefault(attribute, []).append(error.message)
    return err


def generate_attribute_list(
    REPORTING_ATTRIBUTES,
    REPORTING_LEVELS,
    add_id=True,
):
    """
    Collect all attributes from all attribute levels
    @param REPORTING_ATTRIBUTES: reporting levels and attributes
    @param REPORTING_LEVELS: list of reporting levels
    @param add_id: add id field to list
    @return: list of all reporting attributes
    """
    raw_attributes = []

    # collect the attribute names
    if REPORTING_LEVELS:
        for level in REPORTING_LEVELS:
            raw_attributes.extend(REPORTING_ATTRIBUTES.get(level, []))
    else:
        raw_attributes = [
            attribute
            for element in REPORTING_ATTRIBUTES.values()
            for attribute in element
        ]

    if add_id:
        raw_attributes.insert(0, "identifier")

    return raw_attributes


def check_attribute_completeness(item, REPORTING_ATTRIBUTES, REPORTING_LEVELS):
    """
    Count completed (i.e. filled or populated) item attributes
    @param item: uploaded item in list of items (e.g. each tool in the tools collection)
    @param REPORTING_ATTRIBUTES: reporting attributes and levels
    @param REPORTING_LEVELS: reporting levels
    @return: dictionary with completeness for each attribute and level
    """
    reporting_dict = init_reporting_dict(
        REPORTING_ATTRIBUTES,
        REPORTING_LEVELS,
        txt="filled_attributes",
    )
    total_populated = 0
    for level in REPORTING_LEVELS:
        level_total = 0
        for k in reporting_dict[level].keys():
            if "filled_attributes" == k:
                continue
            elif "total_attributes" == k:
                continue
            else:
                reporting_dict[level][k] = 1 if item.get(k, None) is not None else 0
                total_populated += reporting_dict[level][k]
                level_total += reporting_dict[level][k]
        reporting_dict[level]["filled_attributes"] = level_total
    reporting_dict["filled_attributes"] = total_populated
    return reporting_dict


def check_item_completeness(item_type, items, REPORTING_ATTRIBUTES, REPORTING_LEVELS):
    """
    @return:
    """
    # schema = get_json(BASELINE_SAMPLE)
    schema = generate_baseline_from_sections(
        REPORTING_ATTRIBUTES, REPORTING_LEVELS, True
    )
    data = []
    for item in items[item_type]:
        it = copy.deepcopy(item)
        print("Processing:", it["identifier"])
        t = {"identifier": it.get("identifier", None), "name": it.get("name", None)}
        compute_tech_md_completeness(it)
        for attribute in set(it.keys()) - set(schema.keys()):
            it.pop(
                attribute, None
            )  # any attribute not in the schema, drop from the data model
        s = copy.deepcopy(schema)
        s.update(it)
        score = check_attribute_completeness(s, REPORTING_ATTRIBUTES, REPORTING_LEVELS)
        t.update(score)
        data.append(t)
    return data


def check_attribute_validation(
    item_type,
    items,
    schema,
    REPORTING_ATTRIBUTES,
    REPORTING_LEVELS,
):
    """
    Generate dictionary that validates each attribute against the JSON validation schema
    @param items: data-models for validation
    @param REPORTING_ATTRIBUTES: reporting levels and attributes
    @param REPORTING_LEVELS: reporting attributes
    @return: dictionary with validation for each attribute
    """

    validation_attributes = set(
        generate_attribute_list(REPORTING_ATTRIBUTES, REPORTING_LEVELS)
    )
    data = []
    for it in items[item_type]:
        total_errors, level_errors = 0, 0
        it_validate = copy.deepcopy(it)
        for attribute in set(it_validate.keys()) - validation_attributes:
            it_validate.pop(attribute, None)
        errors = validate_attribute_schema(schema, it_validate)
        t = {"identifier": it.get("identifier", None), "name": it.get("name", None)}
        reporting_dict = init_reporting_dict(
            REPORTING_ATTRIBUTES,
            REPORTING_LEVELS,
            txt="attributes_with_errors",
        )
        total_errors = 0
        for level in REPORTING_LEVELS:
            level_errors = 0
            if "F: Technical Metadata" == level:
                for k in reporting_dict[level].keys():
                    if "dataClassesCount" == k:
                        i = it_validate.get(k, 0)
                        reporting_dict[level][k] = int(1 - (i > 1))
                    elif "attributes_with_errors" == k:
                        continue
                    elif "total_attributes" == k:
                        continue
                    else:
                        reporting_dict[level][k] = it_validate.get(k, 0)
                    level_errors += reporting_dict[level][k]
                    total_errors += reporting_dict[level][k]
            else:
                for k in reporting_dict[level].keys():
                    if "attributes_with_errors" == k:
                        continue
                    elif "total_attributes" == k:
                        continue
                    else:
                        if k in errors:
                            zzz_debug = errors[k]
                            reporting_dict[level][k] = 1
                            level_errors += 1
                            total_errors += 1
            reporting_dict[level]["attributes_with_errors"] = level_errors
        t.update(reporting_dict)
        t["attributes_with_errors"] = total_errors
        data.append(t)
    return data


def generate_baseline_from_sections(
    REPORTING_ATTRIBUTES,
    REPORTING_LEVELS,
    add_id=True,
):
    """
    generate the baseline schema from REPORTING_ATTRIBUTES, a dictionary of dictionaries
    @param REPORTING_ATTRIBUTES: reporting levels and attributes
    @param REPORTING_LEVELS: reporting attributes
    @param add_id: add ID field to levels
    @return: dictionary including all attributes

    """
    baseline_dict = {}
    raw_attributes = generate_attribute_list(
        REPORTING_ATTRIBUTES, REPORTING_LEVELS, add_id
    )

    baseline_dict = {attribute: None for attribute in raw_attributes}

    return baseline_dict


def compute_tech_md_completeness(data_model):
    """
    check if technical metadata is complete
    @param data_model: uploaded data-model
    """
    if data_model.get("dataClassesCount", 0) < 1:
        return
    tm = data_model.get("technicalMetaDataValidation", {})
    data_model["tableName"] = 1 if tm.get("tableNames", 0) > 0 else 0
    data_model["tableDescription"] = 1 if tm.get("tableDescriptions", 0) > 0 else 0
    data_model["columnName"] = 1 if tm.get("columnNames", 0) > 0 else 0
    data_model["columnDescription"] = 1 if tm.get("columnDescriptions", 0) > 0 else 0
    data_model["dataType"] = 1 if tm.get("dataTypes", 0) > 0 else 0
    data_model["sensitive"] = None


def init_reporting_dict(
    REPORTING_ATTRIBUTES,
    REPORTING_LEVELS,
    txt="attribute_reporting",
):
    """
    Initialise dictionary that mirrors reporting levels and attributes
    @param REPORTING_ATTRIBUTES: reporting levels and attributes
    @param REPORTING_LEVELS: reporting attributes
    @param txt: name for aggregation field
    @return: reporting attribute dictionary
    """
    reporting_dict = {}
    attribute_count = 0
    for level in REPORTING_LEVELS:
        level_dict = {attr: 0 for attr in REPORTING_ATTRIBUTES[level]}
        level_dict[txt] = 0
        level_dict["total_attributes"] = len(REPORTING_ATTRIBUTES[level])
        attribute_count += len(REPORTING_ATTRIBUTES[level])
        reporting_dict[level] = level_dict

    reporting_dict[txt] = 0
    reporting_dict["total_attributes"] = attribute_count

    return reporting_dict


def flatten_reporting_dict(items):
    """
    flatten nested reporting dictionary for export to .csv
    @param items: nested dictionary
    @return: flat dictionary
    """
    headers = []
    data = []

    for it in items:
        flat_it = {}
        for k, v in it.items():
            if isinstance(v, dict):
                i = 0
                for nk, nv in v.items():  # nested key, value
                    if i == 0:
                        fk = f"{k}, {nk}"  # flat key
                        # i += 1
                    else:
                        fk = f"{k[:2]} {nk}"
                    flat_it[fk] = nv
                    if not fk in headers:
                        headers.append(fk)
            else:
                flat_it[k] = v
                if not k in headers:
                    headers.append(k)
        data.append(flat_it)

    return data, headers


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--schema",
        choices=["tools", "project", "person", "paper"],
        help="Please enter the schema name (tools, project, person, paper).",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--json",
        help="Please enter the path to the JSON file you would like to validate.",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    SCHEMA_PATH = "schema/{}/draft/{}.schema.json".format(args.schema, args.schema)
    JSON_PATH = args.json

    COMPLETENESS_EXPORT_PATH = "reports/{}/test/attribute_completeness.json".format(
        args.schema
    )
    ERRORS_EXPORT_PATH = "reports/{}/test/attribute_errors.json".format(args.schema)

    REPORTING_LEVELS = ["{} attributes".format(args.schema)]
    REPORTING_ATTRIBUTES = {
        "{} attributes".format(args.schema): list(
            get_json(SCHEMA_PATH)["properties"].keys()
        )
    }

    # STEP 1: READ IN THE SCHEMA AND JSON FOR VALIDATION
    items = get_json(JSON_PATH)
    schema = get_json(SCHEMA_PATH)

    # STEP 2: RUN THE VALIDATION TO OBTAIN ERRORS AND COMPLETENESS
    attribute_completeness_score = check_item_completeness(
        args.schema, items, REPORTING_ATTRIBUTES, REPORTING_LEVELS
    )
    export_json(attribute_completeness_score, COMPLETENESS_EXPORT_PATH)
    data, headers = flatten_reporting_dict(attribute_completeness_score)

    schema_errors = check_attribute_validation(
        args.schema, items, schema, REPORTING_ATTRIBUTES, REPORTING_LEVELS
    )
    export_json(schema_errors, ERRORS_EXPORT_PATH)

    # TODO: STEP 3: CREATE WEIGHTS CONFIG FILE AND CALCULATED WEIGHTED ERRORS


if __name__ == "__main__":
    main()
