from statistics import mean
import csv
import argparse
from validate_schema import (
    get_json,
    export_json,
)

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

DATASET_SCHEMA = "schema/{}/draft/{}.schema.json".format(args.schema, args.schema)
DATASETS_JSON = args.json
WEIGHTS = "weights/{}.weights.json".format(args.schema)

REPORTING_LEVELS = ["{} attributes".format(args.schema)]
REPORTING_ATTRIBUTES = {
    "{} attributes".format(args.schema): list(
        get_json(DATASET_SCHEMA)["properties"].keys()
    )
}


def export_csv(data, filename, header):
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def generate_quality_score():
    """Reads the completeness and error json reports, and calculates the metadata quality scores.
    return summary_data, list(set(headers))
    """

    # Generate completeness percent & weighted completeness percent
    scores = get_json("reports/{}/test/attribute_completeness.json".format(args.schema))
    completion_weightings = get_json(WEIGHTS)
    data = {}
    for s in scores:
        data[s["identifier"]] = {
            "identifier": s["identifier"],
            "name": s["name"],
        }
        c_score = round(
            (s["filled_attributes"] / s["total_attributes"]) * 100, 2
        )  # completion score
        wc_score = round(
            attribute_weighted_score(s, completion_weightings) * 100, 2
        )  # weighted completion score
        data[s["identifier"]]["completeness_percent"] = c_score
        data[s["identifier"]]["weighted_completeness_percent"] = wc_score

    # Generate error percent and weighted error percent
    schema = get_json(DATASET_SCHEMA)
    total_attributes = len(list(schema["properties"].keys()))
    errors = get_json("reports/{}/test/attribute_errors.json".format(args.schema))
    error_weightings = get_json(WEIGHTS)
    for e in errors:
        e_score = round((e["attributes_with_errors"] / total_attributes) * 100, 2)
        we_score = round(attribute_weighted_score(e, error_weightings) * 100, 2)
        data[e["identifier"]]["error_percent"] = e_score
        data[e["identifier"]]["weighted_error_percent"] = we_score

    # Generate quality score, weighted quality score, quality score rating, and weighted quality score rating
    summary_data = []
    headers = []
    for id, d in data.items():
        avg_score = round(
            mean([data[id]["completeness_percent"], 100 - data[id]["error_percent"]]), 2
        )
        d["quality_score"] = avg_score
        d["quality_rating"] = quality_ratings(d["quality_score"])

        weighted_avg_score = round(
            mean(
                [
                    data[id]["weighted_completeness_percent"],
                    100 - data[id]["weighted_error_percent"],
                ]
            ),
            2,
        )
        d["weighted_quality_score"] = weighted_avg_score
        d["weighted_quality_rating"] = quality_ratings(d["weighted_quality_score"])

        headers.extend(d.keys())
        summary_data.append(d)

    return summary_data, list(set(headers))


def quality_ratings(s):
    """Takes in a score and returns the resulting quality rating
    Keyword arguments:
    s -- score: a single score from the dictionary of metadata scores
    """
    if s <= 66:
        return "Not Rated"
    elif s > 66 and s <= 76:
        return "Bronze"
    elif s > 76 and s <= 86:
        return "Silver"
    elif s > 86:
        return "Gold"


def attribute_weighted_score(s, w):
    """Applies the provided attribute weightings to the completeness and error score.
    Keyword arguments:
    s -- score: a dictionary of metadata scores
    w -- weights: a dictionary of metadata attributes and weights
    """
    score = 0
    for section in REPORTING_LEVELS:
        section_score = s[section]
        for att_name, att_weights in w[section].items():
            score = score + (section_score[att_name] * att_weights)
    return score


def main():

    # Summarise Average Quality Score
    summary_score, headers = generate_quality_score()
    export_json(summary_score, "reports/{}/metadata_quality.json".format(args.schema))
    export_csv(
        summary_score, "reports/{}/metadata_quality.csv".format(args.schema), headers
    )


if __name__ == "__main__":
    main()
