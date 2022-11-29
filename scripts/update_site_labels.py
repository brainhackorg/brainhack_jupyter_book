"""Update the list of issue labels based of the list of brainhack sites"""

import json
from pathlib import Path

import pandas as pd
from rich import print

label_color = "d4c5f9"

labels_file = Path(__file__).parent.parent.joinpath("template", "labels.json")

sites_file = Path(__file__).parent.parent.joinpath("data", "brainhack-sites.csv")

with open(labels_file) as f:
    labels = json.load(f)

sites_in_labels = [label["name"] for label in labels]

sites = pd.read_csv(sites_file)


def format_label(string):
    string = string.values[0].replace(" ", "").replace(".", "").lower()
    string = string.replace("unitedkingdomofgreatbritainandnorthernireland", "uk")
    string = string.replace("unitedstatesofamerica", "usa")
    return string


for site in sites["City"]:

    row = sites[sites["City"] == site]

    this_site = {
        "name": f"{format_label(row['City'])}_{format_label(row['Country'])}",
        "description": f"{row['City'].values[0]} event",
        "color": label_color,
    }

    if this_site["name"] not in sites_in_labels:
        labels.append(this_site)

with open(labels_file, "w") as f:
    json.dump(labels, f, indent=4)
