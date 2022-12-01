from typing import Union

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


def histogram_nb_projects_per_x(
    df: pd.DataFrame,
    column: str,
    content: Union[str, list, None] = None,
    replace: Union[str, list, None] = None,
):
    """Make a histogram of the number of projects sorted by column x.

    :param df: input dataframe
    :type df: pd.DataFrame
    :param column: column header to sort projects by
    :type column: str
    :param content: only include projects with this content in targeted column, defaults to None
    :type content: str, optional
    :return: figure object
    :rtype: _type_
    """

    ohbm_filter = df["event"].str.contains("OHBM", na=False)

    x = list_x_in_projects(df, column)
    if isinstance(content, (str)):
        tmp = [x for x in x if content in x]
    if isinstance(content, (list)):
        tmp = []
        for item in x:
            tmp.extend(item for item2 in content if item2 in item)
    if content is None:
        tmp = x
    x = tmp

    data = {column: x, "ohbm_projects": [], "bhg_projects": []}

    for item in data[column]:

        df[column] = df[column].astype("string")
        frame_filter = df[column].str.contains("|".join([item]), na=False)

        is_ohbm_project = frame_filter & ohbm_filter
        data["ohbm_projects"].append(is_ohbm_project.sum())

        is_not_ohbm_project = frame_filter & ~ohbm_filter
        data["bhg_projects"].append(is_not_ohbm_project.sum())

    if replace is not None:
        if isinstance(replace, (str)):
            replace = [replace]
        if isinstance(replace, (list)):
            for item in replace:
                for i, item2 in enumerate(data[column]):
                    data[column][i] = item2.replace(item, "")

    data = pd.DataFrame(data)

    fig = px.bar(data, x=column, y=["ohbm_projects", "bhg_projects"])

    return fig


def main():

    df = load_hackathon_projects()

    sites_fig = histogram_nb_projects_per_x(df, "site")
    save_figure(sites_fig, "site")

    date_fig = histogram_nb_projects_per_x(df, "date")
    save_figure(date_fig, "date")

    programming_fig = histogram_nb_projects_per_x(
        df, "labels", "programming:", "programming:"
    )
    save_figure(programming_fig, "programming")

    tools_fig = histogram_nb_projects_per_x(df, "labels", "tools:", "tools:")
    save_figure(tools_fig, "tools")

    topic_fig = histogram_nb_projects_per_x(df, "labels", "topic:", "topic:")
    save_figure(topic_fig, "topic")

    project_type_fig = histogram_nb_projects_per_x(
        df, "labels", "project_type:", "project_type:"
    )
    save_figure(project_type_fig, "project_type")

    modality_fig = histogram_nb_projects_per_x(df, "labels", "modality:", "modality:")
    save_figure(modality_fig, "modality")

    tmp = histogram_nb_projects_per_x(df, "labels", ["git", "MRI"], "git_skills:")
    tmp.show()

    labels_fig = histogram_nb_projects_per_x(df, "labels")
    save_figure(labels_fig, "labels")

    df = px.data.gapminder()
    fig = px.scatter_geo(
        df,
        locations="iso_alpha",
        color="continent",
        hover_name="country",
        size="pop",
        animation_frame="year",
        projection="natural earth",
    )
    fig.show()
    save_figure(fig, "planet")

    if show:
        sites_fig.show()
        date_fig.show()
        programming_fig.show()
        project_type_fig.show()
        tools_fig.show()
        modality_fig.show()
        labels_fig.show()


if __name__ == "__main__":
    main()
