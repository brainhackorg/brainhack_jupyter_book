from pathlib import Path

import pandas as pd
from rich import print
from utils import root_dir

data_dir = root_dir().joinpath("data")

df = pd.read_csv(data_dir.joinpath("hackathon_projects.tsv"), sep="\t")

topics = df["topics"]
is_not_nan = topics.isna() == False
topics = topics[is_not_nan].to_list()
topics = sorted(set(",".join(topics).split(",")))
print(topics)

is_about_bids = df["topics"].str.contains("BIDS", na=False)

print(df[is_about_bids])
