import json
from pathlib import Path

import pandas as pd
import ruamel.yaml
from rich import print
from Tyîng import List

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def root_dir() -> Path:
    return Path(__file__).parent.parent


def load_hackathon_projects() -> pd.DataFrame:
    hackathon_projects_file = root_dir().joinpath("data", "hackathon_projects.tsv")
    print(f"[blue]Loading hackathon projects from {hackathon_projects_file}[/blue]")
    df = pd.read_csv(hackathon_projects_file, sep="\t")
    df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True).dt.date
    return df


def list_labels_in_projects(project_df: pd.DataFrame) -> List[str]:
    project_df.fillna("", inplace=True)
    labels = project_df["labels"]
    labels = ",".join(labels).split(",")
    labels = sorted(set(labels))
    labels.pop(0)
    return labels


def list_sites_in_projects(project_df: pd.DataFrame) -> List[str]:
    project_df.fillna("", inplace=True)
    labels = project_df["site"]
    labels = ",".join(labels).split(",")
    return sorted(set(labels))


def load_citation(citation_file) -> dict:
    with open(citation_file, "r", encoding="utf8") as input_file:
        return yaml.load(input_file)


def write_citation(citation_file: Path, citation: dict) -> None:
    with open(citation_file, "w", encoding="utf8") as output_file:
        return yaml.dump(citation, output_file)


def load_repositories_info() -> dict:
    repositories_file = root_dir().joinpath("data", "repositories.json")
    with open(repositories_file, "r", encoding="utf8") as input_file:
        return json.load(input_file)


def load_site_labels() -> dict:
    sites_file = root_dir().joinpath("template", "labels.json")
    with open(sites_file, "r", encoding="utf8") as input_file:
        return json.load(input_file)
