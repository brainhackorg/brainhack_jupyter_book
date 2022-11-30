import pandas as pd
import plotly.express as px
from rich import print
from utils import list_x_in_projects
from utils import load_hackathon_projects
from utils import root_dir

show = True


def save_figure(fig, filename):
    fig_file = root_dir().joinpath("brainhack_book", f"_{filename}.html")
    print(f"[blue]saving figure {fig_file}[/blue]")
    fig.write_html(fig_file)


def make_histogram(df: pd.DataFrame, column: str):

    x = list_x_in_projects(df, column)

    data = {column: [], "nb_projects": []}
    for key in x:
        data[column].append(key)
        frame_filter = df[column].str.contains("|".join([key]), na=False)
        data["nb_projects"].append(frame_filter.sum())

    data = pd.DataFrame(data)

    fig = px.bar(data, x=column, y="nb_projects")

    return fig


def main():

    df = load_hackathon_projects()

    sites_fig = make_histogram(df, "site")
    save_figure(sites_fig, "site")

    labels_fig = make_histogram(df, "labels")
    save_figure(labels_fig, "labels")

    if show:
        sites_fig.show()
        labels_fig.show()


if __name__ == "__main__":
    main()
