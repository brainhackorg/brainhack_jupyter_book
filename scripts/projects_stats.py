import pandas as pd
import plotly.express as px
from rich import print
from utils import list_labels_in_projects
from utils import list_sites_in_projects
from utils import load_hackathon_projects
from utils import root_dir

df = load_hackathon_projects()

sites = list_sites_in_projects(df)

data = {"sites": [], "nb_projects": []}
for key in sites:
    data["sites"].append(key)
    filter_site = df["site"].str.contains("|".join([key]), na=False)
    data["nb_projects"].append(filter_site.sum())

data = pd.DataFrame(data)

sites_fig = px.bar(data, x="sites", y="nb_projects")
sites_fig_file = root_dir().joinpath("brainhack_book", "_sites.html")
print(f"[blue]saving figure {sites_fig_file}[/blue]")
sites_fig.write_html(sites_fig_file)

labels = list_labels_in_projects(df)

data = {"labels": [], "nb_projects": []}
for key in labels:
    data["labels"].append(key)
    filter_site = df["labels"].str.contains("|".join([key]), na=False)
    data["nb_projects"].append(filter_site.sum())

data = pd.DataFrame(data)

labels_fig = px.bar(data, x="labels", y="nb_projects")
labels_fig_file = root_dir().joinpath("brainhack_book", "_labels.html")
print(f"[blue]saving figure {labels_fig_file}[/blue]")
labels_fig.write_html(labels_fig_file)
