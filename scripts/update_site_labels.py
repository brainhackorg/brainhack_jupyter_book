"""Update the list of issue labels based of the list of brainhack sites"""

import json

import pandas as pd
from utils import load_site_labels, root_dir

label_color = "d4c5f9"


def format_label(string):
    string = string.values[0].replace(" ", "").replace(".", "").lower()
    string = string.replace("unitedkingdomofgreatbritainandnorthernireland", "uk")
    string = string.replace("unitedstatesofamerica", "usa")
    return string


def main():
    sites_file = root_dir().joinpath("data", "brainhack-sites.csv")
    sites = pd.read_csv(sites_file)

    labels = load_site_labels()
    sites_in_labels = [label["name"] for label in labels]

    for site in sites["City"]:
        row = sites[sites["City"] == site]

        this_site = {
            "name": f"{format_label(row['City'])}_{format_label(row['Country'])}",
            "description": f"{row['City'].values[0]} event",
            "color": label_color,
        }

        if this_site["name"] not in sites_in_labels:
            labels.append(this_site)

    labels_file = root_dir().joinpath("template", "labels.json")
    with open(labels_file, "w") as f:
        json.dump(labels, f, indent=4)
