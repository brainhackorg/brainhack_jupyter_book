"""Generate the contributors and acknowledgments tables for the book."""
from pathlib import Path

import pandas as pd
from utils import root_dir


def turn_twitter_handle_into_link(df):
    prefix = "https://twitter.com/"
    df["twitter"] = f"[twitter]({prefix}" + df["twitter"].astype(str) + ")"
    df.replace("[twitter](https://twitter.com/nan)", " ", inplace=True)
    return df


def turn_osf_id_into_link(df):
    return turn_into_link(df, "osf_id", "osf", "https://osf.io/")


def turn_into_link(df, col, content, prefix):
    df[col] = f"[{content}]({prefix}" + df[col].astype(str) + ")"
    df.replace(f"[{content}]({prefix}nan)", " ", inplace=True)
    return df


def merge_name_columns(df):
    df["Middle initial(s)"] = df["Middle initial(s)"].fillna("")

    df["Name"] = (
        df["First name"] + " " + df["Middle initial(s)"] + " " + df["Last name"]
    )
    df.drop(columns=["First name", "Middle initial(s)", "Last name"], inplace=True)

    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    return df


def rename_columns(df):
    renaming_map = {
        "participated in event (for example: led or joined a hackathon project)": "participated in event",
        "taught at event (for example: traintrack)": "taught at event",
        "prepared meeting venue (zoom) (for any meeting)": "prepared meeting venue",
        "managed meeting times (doodle)": "managed meeting times",
    }

    df = df.rename(columns=renaming_map)
    return df


def drop_columns(df):
    columns_to_drop = [
        "2nd affiliation",
        "3rd affiliation",
        "As co-author, I have read and approve submission of this manuscript",
        "ranking",
        "joint_first",
        "Author_ID",
        "Feel free to add any other information regarding your contribution.",
    ]

    df.drop(columns=columns_to_drop, inplace=True)

    return df


def process_file(file: Path):
    output_file = root_dir().joinpath("brainhack_book", file.stem + "_table.md")
    contributors = pd.read_csv(file, sep="\t")
    contributors = drop_columns(contributors)
    contributors = rename_columns(contributors)
    contributors = merge_name_columns(contributors)
    contributors = turn_twitter_handle_into_link(contributors)
    contributors = turn_osf_id_into_link(contributors)
    contributors = contributors.fillna(" ")
    contributors.to_markdown(buf=output_file, mode="wt", index=False)


def main():
    contributors_file = root_dir().joinpath("data", "contributors", "contributors.tsv")
    process_file(contributors_file)

    contributors_file = root_dir().joinpath(
        "data", "contributors", "neuroview_contributors.tsv"
    )
    process_file(contributors_file)

    acknowledgments_file = root_dir().joinpath(
        "data", "acknowledgments", "acknowledgments.csv"
    )
    acknowledgments = pd.read_csv(acknowledgments_file)
    output_file = root_dir().joinpath(
        "brainhack_book", acknowledgments_file.stem + "_table.md"
    )
    acknowledgments.to_markdown(buf=output_file, mode="wt", index=False)


if __name__ == "__main__":
    main()
