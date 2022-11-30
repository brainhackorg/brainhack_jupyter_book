import json
from pathlib import Path

import pandas as pd
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def root_dir():
    return Path(__file__).parent.parent


def load_hackathon_projects():
    hackathon_projects_file = root_dir().joinpath("data", "hackathon_projects.tsv")
    return pd.read_csv(hackathon_projects_file, sep="\t")


def load_citation(citation_file):
    with open(citation_file, "r", encoding="utf8") as input_file:
        return yaml.load(input_file)


def write_citation(citation_file, citation):
    with open(citation_file, "w", encoding="utf8") as output_file:
        return yaml.dump(citation, output_file)


def load_repositories_info():
    repositories_file = root_dir().joinpath("data", "repositories.json")
    with open(repositories_file, "r", encoding="utf8") as input_file:
        return json.load(input_file)


def load_site_labels():
    sites_file = root_dir().joinpath("template", "labels.json")
    with open(sites_file, "r", encoding="utf8") as input_file:
        return json.load(input_file)
