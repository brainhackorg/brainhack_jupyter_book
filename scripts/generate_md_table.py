from pathlib import Path

import pandas as pd
from rich import print
from utils import root_dir

contributors_file = root_dir().joinpath("data", "contributors", "contributors.tsv")

contributors = pd.read_csv(contributors_file, sep="\t")

md = contributors.to_markdown(
    buf=contributors_file.with_suffix(".md"), mode="wt", index=False
)

print(md)
