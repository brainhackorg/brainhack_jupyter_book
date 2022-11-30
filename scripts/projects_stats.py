from pathlib import Path

import pandas as pd
from rich import print
from utils import load_hackathon_projects, root_dir

df = load_hackathon_projects()

topics = df["topics"]
is_not_nan = topics.isna() == False
topics = topics[is_not_nan].to_list()
topics = sorted(set(",".join(topics).split(",")))
print(topics)

is_about_bids = df["topics"].str.contains("BIDS", na=False)

print(df[is_about_bids])
