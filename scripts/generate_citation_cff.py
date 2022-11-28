from pathlib import Path

import pandas as pd
from utils import load_citation, root_dir, write_citation


def main():

    contributors = pd.read_csv(
        root_dir().joinpath("data", "contributors", "contributors.tsv")
    )

    citation_file = root_dir().joinpath("CITATION.cff")

    citation = load_citation(citation_file)
    write_citation(citation_file, citation)
