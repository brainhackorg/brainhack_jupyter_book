from pathlib import Path

import pandas as pd
from rich import print
from utils import root_dir


def clean_file(filename: Path):

    contributors = pd.read_csv(filename, sep="\t")
    contributors = rename_colums(contributors)

    contributors = clean_orcid(contributors)
    contributors = clean_twitter(contributors)
    contributors = clean_mattermost(contributors)
    contributors = clean_osf(contributors)

    output_file = filename.parent.joinpath(filename.stem + "_clean.tsv")
    contributors.to_csv(output_file, sep="\t", index=False)


def rename_colums(df):

    renaming_map = {
        "Affiliation (please use the format: Department / Institution / City / Country)": "affiliation",
        "Your 2nd affiliation (optional) - please use same format as above ": "2nd affiliation",
        "Your 3rd affiliation (optional) - please use same format as above": "3rd affiliation",
        "ORCID id (optional)": "orcid",
        "OSF id (optional)": "osf_id",
        "Twitter handle (optional)": "twitter",
        "Brainhack mattermost (optional)": "mattermost",
    }

    df = df.rename(columns=renaming_map)
    return df


def clean_column(df, column, string_to_replace, replacement):
    to_clean = df[column].str.startswith(string_to_replace, na=False)
    index = to_clean[to_clean == True].index
    for i in index:
        df[column][i] = df[column][i].replace(string_to_replace, replacement)
    return df


def clean_osf(df):
    df = clean_column(df, "osf_id", " ", "")
    df = clean_column(df, "osf_id", "osf.io/", "")
    df = clean_column(df, "osf_id", "https://osf.io/", "")
    df = clean_column(df, "osf_id", "http://osf.io/", "")
    df = clean_column(df, "osf_id", "osf.io/", "")
    return df


def clean_twitter(df):
    df = clean_column(df, "twitter", " ", "")
    df = clean_column(df, "twitter", "@", "")
    df = clean_column(df, "twitter", "https://twitter.com/", "")
    return df


def clean_orcid(df):
    df = clean_column(df, "orcid", " ", "")
    df = clean_column(df, "orcid", "https://orcid.org/", "")
    df = clean_column(df, "orcid", "http://orcid.org/", "")
    df = clean_column(df, "orcid", "orcid.org/", "")
    return df


def clean_mattermost(df):
    df = clean_column(df, "mattermost", " ", "")
    df = clean_column(df, "mattermost", "@", "")
    return df


def main():

    clean_file(root_dir().joinpath("data", "contributors", "contributors.tsv"))
    clean_file(
        root_dir().joinpath("data", "contributors", "neuroview_contributors.tsv")
    )


if __name__ == "__main__":
    main()
