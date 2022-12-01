import json
import logging
from pathlib import Path
from typing import List

import pandas as pd
import ruamel.yaml
from rich import print
from rich.logging import RichHandler

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


log = logging.getLogger("bhg_jupyterbook")


def bhg_log(name: str = "bhg_jupyterbook") -> logging.Logger:
    """Create log."""
    FORMAT = "bhg_jupyterbook - %(asctime)s - %(levelname)s - %(message)s"

    if not name:
        name = "rich"

    logging.basicConfig(
        level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )

    return logging.getLogger(name)


def root_dir() -> Path:
    return Path(__file__).parent.parent


def get_timeline_df() -> pd.DataFrame:

    timeline_df = load_file("brainhack-timeline_new.csv")

    brainhack_sites_df = load_file("brainhack-sites.csv")

    lat = []
    lon = []
    for row in timeline_df.itertuples():
        print(row.City)
        this_city = brainhack_sites_df["City"] == row.City.strip()
        if this_city.sum() == 0:
            log.warning(f"Could not find {row.City} in brainhack-sites.csv")
            continue

        lat.append(brainhack_sites_df[this_city]["lat"].values)
        lon.append(brainhack_sites_df[this_city]["lon"].values)

    return timeline_df


def load_file(file):
    file = root_dir().joinpath("data", file)
    print(f"[blue]Loading {file}[/blue]")
    result = pd.read_csv(file)

    return result


def load_hackathon_projects() -> pd.DataFrame:
    hackathon_projects_file = root_dir().joinpath("data", "hackathon_projects.tsv")
    print(f"[blue]Loading hackathon projects from {hackathon_projects_file}[/blue]")
    df = pd.read_csv(hackathon_projects_file, sep="\t")
    return df


def list_x_in_projects(project_df: pd.DataFrame, x: str) -> List[str]:
    project_df.fillna("", inplace=True)
    x = project_df[x]
    x = [str(x) for x in x]
    x = ",".join(x).split(",")
    x = sorted(set(x))
    if x[0] == "":
        x.pop(0)
    return x


def list_labels_in_projects(project_df: pd.DataFrame) -> List[str]:
    labels = list_x_in_projects(project_df, "labels")
    return labels


def list_sites_in_projects(project_df: pd.DataFrame) -> List[str]:
    sites = list_x_in_projects(project_df, "site")
    return sites


def load_citation(citation_file) -> dict:
    with open(citation_file, encoding="utf8") as input_file:
        return yaml.load(input_file)


def write_citation(citation_file: Path, citation: dict) -> None:
    with open(citation_file, "w", encoding="utf8") as output_file:
        return yaml.dump(citation, output_file)


def load_repositories_info() -> dict:
    repositories_file = root_dir().joinpath("data", "repositories.json")
    with open(repositories_file, encoding="utf8") as input_file:
        return json.load(input_file)


def load_site_labels() -> dict:
    sites_file = root_dir().joinpath("template", "labels.json")
    with open(sites_file, encoding="utf8") as input_file:
        return json.load(input_file)
