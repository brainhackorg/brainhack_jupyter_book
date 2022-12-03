import json
import logging
from pathlib import Path
from typing import List

import geopandas as gpd
import pandas as pd
import ruamel.yaml
from rich import print
from rich.logging import RichHandler

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


log = logging.getLogger("bhg_jupyterbook")


def bhg_log(name: str = "bhg_jupyterbook") -> logging.Logger:
    """Create log."""
    FORMAT = "bhg_jupyterbook - %(asctime)s - \n%(message)s"

    if not name:
        name = "rich"

    logging.basicConfig(
        level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )

    return logging.getLogger(name)


def root_dir() -> Path:
    return Path(__file__).parent.parent


def find_coordinates_event(event_city: str, brainhack_sites: pd.DataFrame) -> tuple:
    """Return latitute and longitude of an event."""
    this_city = brainhack_sites["City"] == event_city.strip()

    lat = []
    lon = []

    if this_city.sum() == 0:
        log.warning(f"Could not find {event_city} in brainhack-sites.csv")
    if this_city.sum() > 1:
        log.warning(
            f"""Found several cities for {event_city} in brainhack-sites.csv:
Evidence: {brainhack_sites[this_city]}"""
        )
    else:
        lat = brainhack_sites[this_city]["lat"].values
        lon = brainhack_sites[this_city]["lon"].values

    assert len(lat) == len(lon)
    return lat, lon


def get_timeline() -> pd.DataFrame:
    """Return timeline dataframe after cleaning and updating it."""
    timeline = load_file("brainhack-timeline.csv")

    timeline["display_name"] = timeline["Title"] + " - " + timeline["City"]

    ohbm_filter = timeline["Title"].str.contains("OHBM", na=False)
    timeline["event type"] = ohbm_filter
    timeline["event type"].replace({True: "OHBM", False: "Brainhack"}, inplace=True)

    brainhack_sites = load_file("brainhack-sites.csv")

    # Find coordinates for each event and drop it if not found
    coordinates = {"lat": [], "lon": []}
    for row in timeline.itertuples():
        (lat, lon) = find_coordinates_event(row.City, brainhack_sites)
        if len(lat) > 0 and len(lon) > 0:
            coordinates["lat"].append(lat[0])
            coordinates["lon"].append(lon[0])
        else:
            timeline.drop(inplace=True, axis=0, index=row.Index)
    geometry = gpd.points_from_xy(x=coordinates["lon"], y=coordinates["lat"])
    timeline = gpd.GeoDataFrame(timeline, geometry=geometry)

    # fill in missing values with mean number of participants for non-OHBM events
    mean = timeline[~ohbm_filter]["Nb_participants"].mean()
    timeline["Nb_participants"] = timeline["Nb_participants"].fillna(mean).astype(int)

    timeline["date"] = pd.to_datetime(
        timeline["YYYY-MM-DD"], infer_datetime_format=True
    ).dt.strftime("%Y")

    return timeline


def load_file(file: str):
    filepath = root_dir().joinpath("data", file)
    print(f"[blue]Loading {filepath}[/blue]")
    result = pd.read_csv(filepath)

    return result


def load_hackathon_projects() -> pd.DataFrame:
    hackathon_projects_file = root_dir().joinpath("data", "hackathon_projects.tsv")
    print(f"[blue]Loading hackathon projects from {hackathon_projects_file}[/blue]")
    df = pd.read_csv(hackathon_projects_file, sep="\t")
    return df


def list_x_in_projects(projects: pd.DataFrame, column: str) -> List[str]:
    projects.fillna("", inplace=True)
    x = projects[column]
    x = [str(x) for x in x]
    x = ",".join(x).split(",")
    x = sorted(set(x))
    if x[0] == "":
        x.pop(0)
    return x


def list_labels_in_projects(projects: pd.DataFrame) -> List[str]:
    labels = list_x_in_projects(projects, "labels")
    return labels


def list_sites_in_projects(projects: pd.DataFrame) -> List[str]:
    sites = list_x_in_projects(projects, "site")
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
