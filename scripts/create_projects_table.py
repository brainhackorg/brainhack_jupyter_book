import json

import pandas as pd
from rich import print
from utils import list_labels_in_projects
from utils import load_repositories_info
from utils import root_dir

sites = {
    "Marseille": {"labels": ["bhg:marseille_fra_1", "marseille_fra"]},
    "Boston": {"labels": ["bhg:boston_usa_1"]},
    "New York City": {"labels": ["bhg:nyc_usa_1"]},
    "Toronto": {"labels": ["bhg:toronto_can_1", "toronto_canada"]},
    "Ontario": {"labels": ["bhg:ontario_can_1"]},
    "Washington D.C.": {"labels": ["bhg:washingtondc_usa_1"]},
    "Montreal": {"labels": ["bhg:mtl_can_1", "montreal_canada"]},
    "Ankara": {"labels": ["bhg:ankara_tur_1"]},
    "micro2macro": {"labels": ["bhg:micro2macro_gbr_1"]},
    "Donostia": {"labels": ["bhg:donostia_esp_1", "donostia_esp"]},
    "Pittsburgh": {"labels": ["bhg:pittsburgh_usa_1"]},
    "Melbourne": {"labels": ["bhg:melbourne_aus_1"]},
    "Rome": {"labels": ["rome_italy"]},
    "Vancouver": {"labels": ["vancouver_canada"]},
    "Singapore": {"labels": ["singapore_singapore"]},
    "Glasgow": {"labels": ["glasgow_scotland"]},
    "EMEA hub": {"labels": ["EMEA hub"]},
    "Apac hub": {"labels": ["Apac hub"]},
    "Americas hub": {"labels": ["Americas hub"]},
    "Sydney": {"labels": ["australasia_aus"]},
    "PhysioPy": {"labels": ["physiopy_gathertown"]},
    "Bay Area": {"labels": ["bay_area_usa"]},
    "Atlantis": {"labels": ["Atlantis", "atlantis_earth"]},
    "Rising sun": {"labels": ["Rising sun"]},
    "Online": {"labels": ["atlantis_earth"]},
    "Nijmegen": {"labels": ["nijmegen_netherlands"]},
    "Krakow": {"labels": ["krakow_pol"]},
    "Madison": {"labels": ["madison_usa"]},
    "Ghent": {"labels": ["ghent_belgium"]},
    "Magdeburg": {"labels": ["magdeburg_germany"]},
    "Espoo": {"labels": ["espoo_finland"]},
}

LABELS_TO_REMOVE = [
    "",
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

LABELS_TO_RENAME = {
    "git_skills:0_none": [
        "git - 0",
        "git-0",
    ],
    "git_skills:1_commit_push": [
        "git - 1",
        "git-1",
    ],
    "git_skills:2_branches_PRs": [
        "git - 2",
    ],
    "git_skills:3_continuous_integration": [
        "git-3",
    ],
    "modality:DWI": ["DWI"],
    "modality:ECG": ["ECG"],
    "modality:ECOG": ["ECOG"],
    "modality:dMRI": ["dMRI"],
    "modality:EEG": ["EEG"],
    "modality:MEG": ["MEG"],
    "modality:MRI": ["MRI"],
    "modality:PET": ["PET"],
    "modality:TDCS": ["TDCS"],
    "modality:TMS": ["TMS"],
    "modality:behavioral": ["behavioral"],
    "modality:eye_tracking": ["eye_tracking", "eye tracking"],
    "modality:fMRI": ["fMRI"],
    "modality:fNIRS": ["fNIRS"],
    "programming:C": [
        "C / C++",
        "C / C++ / Cython",
        "C++",
        "programming:C++",
    ],
    "programming:containerization": [
        "containerization",
        "docker / singularity",
    ],
    "programming:documentation": ["documentation", "markdown", "reStructuredText"],
    "programming:Java": [
        "Java",
    ],
    "programming:R": [
        "R",
    ],
    "programming:Javascript": [
        "javascript",
    ],
    "programming:html_css": ["html / css"],
    "programming:none": ["no code"],
    "programming:Matlab": ["Matlab", "matlab"],
    "programming:Python": ["Python", "python"],
    "programming:Unix_command_line": ["Unix command line", "unix command line"],
    "programming:workflows": ["workflows", "Workflow"],
    "tools:AFNI": ["AFNI"],
    "tools:ANTs": ["ANTs"],
    "tools:BIDS": ["BIDS"],
    "tools:Brainstorm": ["Brainstorm"],
    "tools:CPAC": ["CPAC"],
    "tools:Datalad": [
        "DataLad",
        "Datalad",
    ],
    "tools:DIPY": ["DIPY", "dipy"],
    "tools:FSL": ["FSL"],
    "tools:FieldTrip": ["FieldTrip"],
    "tools:Freesurfer": ["Freesurfer", "freesurfer"],
    "tools:Jupyter": ["Jupyter", "Jupyter notebooks"],
    "tools:MNE": ["MNE"],
    "tools:MRtrix": ["MRtrix", "Mrtrix"],
    "tools:NWB": ["NWB"],
    "tools:Nipype": ["Nipype", "nipype"],
    "tools:SPM": ["SPM"],
    "tools:fMRIPrep": ["fMRIPrep"],
    "topic:tractography": ["tractography"],
    "topic:machine_learning": [
        "machine learning",
        "Machine Learning",
        "machine_learning",
    ],
}


def rename_labels(labels, LABELS_TO_RENAME):
    for i, label in enumerate(labels):
        for key in LABELS_TO_RENAME:
            if label in LABELS_TO_RENAME[key]:
                labels[i] = key
    return labels


def get_project_labels(this_project):
    return [x["name"] for x in this_project["labels"]]


def find_this_site_name(site, sites):
    return next((key for key in sites if site in sites[key]["labels"]), None)


def find_site_in_labels(sites, labels):
    for key in sites:
        if set(sites[key]["labels"]) & set(labels):
            return key


def get_project_site(this_hackathon, sites, labels):

    site = this_hackathon.get("site", None)
    if site is not None:
        site = find_this_site_name(site, sites)

    if site is None:
        site = find_site_in_labels(sites, labels)

    if site is None:
        print(f"Could not find site for {this_hackathon['name']}")
        print(labels)
        print(this_hackathon)
        site = "n/a"

    return site


def main():

    repositories_info = load_repositories_info()

    data_dir = root_dir().joinpath("data")

    labels_to_remove = LABELS_TO_REMOVE
    for i in sites:
        labels_to_remove.extend(sites[i]["labels"])

    data = {
        "name": [],
        "site": [],
        "event": [],
        "date": [],
        "labels": [],
        "url": [],
    }

    for this_hackathon in repositories_info:

        print(f"{this_hackathon}")

        with open(data_dir.joinpath(f"projects_{this_hackathon}.json"), "r") as f:

            projects = json.load(f)

            for this_project in projects:

                labels = get_project_labels(this_project)
                this_project["site"] = get_project_site(
                    repositories_info[this_hackathon], sites, labels
                )

                for i in labels_to_remove:
                    if i in labels:
                        labels.remove(i)
                labels = sorted(labels)

                labels = rename_labels(labels, LABELS_TO_RENAME)

                if labels == []:
                    labels = ["n/a"]

                labels = sorted(labels)

                data["event"].append(repositories_info[this_hackathon]["name"])
                data["name"].append(this_project["title"].lstrip())
                data["date"].append(this_project["created_at"])
                data["site"].append(this_project["site"].lstrip())
                data["url"].append(this_project["url"])
                data["labels"].append(",".join(labels))

    df = pd.DataFrame(data=data)

    df.to_csv(data_dir.joinpath("hackathon_projects.tsv"), index=False, sep="\t")

    print(list_labels_in_projects(df))


if __name__ == "__main__":
    main()
