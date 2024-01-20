"""Generate figures for the projects and timeline."""
from typing import Union

import pandas as pd
import plotly.express as px
from rich import print
from utils import get_timeline
from utils import list_labels_in_projects
from utils import list_x_in_projects
from utils import load_hackathon_projects
from utils import root_dir

show = True


def save_figure(fig, filename):
    fig_file = root_dir().joinpath("brainhack_book", f"_{filename}.html")
    print(f"[blue]saving figure {fig_file}[/blue]")
    fig.write_html(fig_file)


def get_categories_to_sort_project_by(
    projects: pd.DataFrame, column: str, content: Union[str, list, None] = None
) -> list:
    categories = list_x_in_projects(projects, column)

    if isinstance(content, (str)):
        categories = [x for x in categories if content in x]

    if isinstance(content, (list)):
        tmp = []
        for item in categories:
            tmp.extend(item for item2 in content if item2 in item)
        categories = tmp

    return categories


def histogram_nb_projects_per_x(
    projects: pd.DataFrame,
    column: str,
    content: Union[str, list, None] = None,
    replace: Union[str, list, None] = None,
):
    """Make a histogram of the number of projects sorted by column x.

    :param projects: input dataframe
    :type projects: pd.DataFrame
    :param column: column header to sort projects by
    :type column: str
    :param content: only include projects with this content in targeted column, defaults to None
    :type content: str, optional
    :return: figure object
    :rtype: _type_
    """

    ohbm_filter = projects["event"].str.contains("OHBM", na=False)

    categories = get_categories_to_sort_project_by(projects, column, content)

    data = {column: categories, "ohbm_projects": [], "bhg_projects": []}

    for item in data[column]:
        projects[column] = projects[column].astype("string")
        frame_filter = projects[column].str.contains("|".join([item]), na=False)

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

    title = f"Number of projects by '{column}'"
    if isinstance(content, (str)):
        title = f"Number of projects for '{column}' by {content.replace(':', '').replace('-', '')}"

    print(title)

    fig = px.bar(
        data,
        x=column,
        y=["ohbm_projects", "bhg_projects"],
        labels={
            "value": "Number of projects",
            "variable": "Event type",
            "labels": column.replace(":", ""),
        },
        title=title,
    )

    return fig


def main():
    projects = load_hackathon_projects()

    sites_fig = histogram_nb_projects_per_x(projects, column="site")
    save_figure(sites_fig, "site")

    date_fig = histogram_nb_projects_per_x(projects, column="date")
    save_figure(date_fig, "date")

    labels_with_separate_figure = [
        "programming:",
        "tools:",
        "topic:",
        "project_type:",
        "modality:",
    ]
    figures = []
    for item in labels_with_separate_figure:
        fig = histogram_nb_projects_per_x(
            projects, column="labels", content=item, replace=item
        )
        save_figure(fig, item.replace(":", ""))
        figures.append(fig)

    labels = list_labels_in_projects(projects)
    other_labels = [
        x
        for x in labels
        if not any(x.startswith(y) for y in labels_with_separate_figure)
    ]
    other_labels_fig = histogram_nb_projects_per_x(
        projects, column="labels", content=other_labels
    )
    save_figure(other_labels_fig, "labels")

    # TODO OHBM events do not get displayed in the timeline
    timeline = get_timeline()
    planet_slider_fig = px.scatter_geo(
        timeline,
        lat=timeline.geometry.y,
        lon=timeline.geometry.x,
        hover_name="display_name",
        color="event type",
        projection="natural earth",
        size="Nb_participants",
        # animation_frame="date",
    )
    save_figure(planet_slider_fig, "planet")

    # TODO add dash datatable with list of projects
    # https://dash.plotly.com/datatable

    if show:
        sites_fig.show()
        date_fig.show()
        for fig in figures:
            fig.show()
        other_labels_fig.show()
        planet_slider_fig.show()


if __name__ == "__main__":
    main()
