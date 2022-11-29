import json
from pathlib import Path

import pandas as pd
from rich import print
from utils import load_repositories_info, root_dir

sites = {
    "Marseille": {"label": "bhg:marseille_fra_1"},
    "New York City": {"label": "bhg:nyc_usa_1"},
    "Toronto": {"label": "bhg:toronto_can_1"},
    "ontario": {"label": "bhg:ontario_can_1"},
    "Washington D.C.": {"label": "bhg:washingtondc_usa_1"},
    "Montreal": {"label": "bhg:mtl_can_1"},
    "Ankara": {"label": "bhg:ankara_tur_1"},
    "micro2macro": {"label": "bhg:micro2macro_gbr_1"},
    "Bilbao": {"label": "bhg:donostia_esp_1"},
    "Pittsburgh": {"label": "bhg:pittsburgh_usa_1"},
    "Melbourne": {"label": "bhg:melbourne_aus_1"},
}

LABELS_TO_REMOVE = [
    "project",
    "Hackathon Project",
    "Hackathon project",
    "status:published",
    "status:web_ready",
    "Atlantis",
    "Rising sun",
    "Email ok",
    "EMEA hub",
    "Apac hub",
    "Americas hub",
    "Hacktrack: Good to go",
]


def main():

    repositories_info = load_repositories_info()

    data_dir = root_dir().joinpath("data")

    labels_to_remove = LABELS_TO_REMOVE
    for i in sites:
        labels_to_remove.append(sites[i]["label"])

    name = []
    url = []
    topics = []
    event = []
    site = []
    date = []

    for this_hackathon in repositories_info:

        print(f"{this_hackathon}")

        with open(data_dir.joinpath(f"projects_{this_hackathon}.json"), "r") as f:

            projects = json.load(f)

            for this_project in projects:

                labels = [x["name"] for x in this_project["labels"]]

                this_project["site"] = "n/a"
                tmp = [x for x in labels if "bhg" in x]
                if tmp != []:
                    for key in sites:
                        if tmp[0] == sites[key]["label"]:
                            this_project["site"] = key
                            print(this_project["site"])
                            break

                for i in labels_to_remove:
                    if i in labels:
                        labels.remove(i)
                labels = sorted(labels)

                if labels == []:
                    labels = ["n/a"]

                event.append(repositories_info[this_hackathon]["name"])
                name.append(this_project["title"].lstrip())
                date.append(this_project["created_at"])
                site.append(this_project["site"].lstrip())
                url.append(this_project["url"])
                topics.append(",".join(labels))

    d = {
        "name": name,
        "site": site,
        "event": event,
        "date": date,
        "topics": topics,
        "url": url,
    }
    df = pd.DataFrame(data=d)

    df.to_csv(data_dir.joinpath("hackathon_projects.tsv"), index=False, sep="\t")


if __name__ == "__main__":
    main()
