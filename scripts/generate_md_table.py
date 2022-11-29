from pathlib import Path

import pandas as pd
from rich import print
from utils import root_dir


def merge_name_columns(df):

    df["Name"] = (
        df["First name"] + " " + df["Middle initial(s)"] + " " + df["Last name"]
    )
    df.drop(columns=["First name", "Middle initial(s)", "Last name"], inplace=True)

    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    return df


def rename_colums(df):

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
    contributors = rename_colums(contributors)
    contributors = merge_name_columns(contributors)
    # contributors = contributors.fillna(' ', inplace=True)
    contributors.to_markdown(buf=output_file, mode="wt", index=False)


def main():

    contributors_file = root_dir().joinpath("data", "contributors", "contributors.tsv")
    process_file(contributors_file)

    contributors_file = root_dir().joinpath(
        "data", "contributors", "neuroview_contributors.tsv"
    )
    process_file(contributors_file)


if __name__ == "__main__":
    main()