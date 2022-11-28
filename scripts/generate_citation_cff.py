from pathlib import Path

import pandas as pd
from cffconvert.cli.create_citation import create_citation
from cffconvert.cli.validate_or_write_output import validate_or_write_output
from utils import load_citation, root_dir, write_citation


def return_author_list_for_cff(contributors):

    author_list = []

    for _, row in contributors.iterrows():

        given_names = row["First name"].strip()
        if isinstance(row["Middle initial(s)"], (str)) and row[
            "Middle initial(s)"
        ] not in ["", " "]:
            given_names += " " + row["Middle initial(s)"].strip()

        author = {
            "given-names": given_names,
            "family-names": row["Last name"].strip(),
            "affiliation": row["affiliation"]
            .strip()
            .replace(" /", ",")
            .replace(",  , ", ", ")
            .replace(",  ,", "")
            .replace("/ ", ""),
        }
        if not pd.isna(row["orcid"]):
            author["orcid"] = f"https://orcid.org/{row['orcid'].strip()}"
        author_list.append(author)

    order = [author["family-names"] for author in author_list]
    order = sorted(order)

    author_list = sorted(author_list, key=lambda k: order.index(k["family-names"]))

    return author_list


def main():

    contributors_file = root_dir().joinpath("data", "contributors", "contributors.tsv")
    contributors = pd.read_csv(contributors_file, sep="\t")

    citation_file = root_dir().joinpath("CITATION.cff")
    citation = load_citation(citation_file)
    citation["authors"] = return_author_list_for_cff(contributors)
    write_citation(citation_file, citation)
    citation = create_citation(infile=citation_file, url=None)
    validate_or_write_output(
        outfile=None, outputformat=None, validate_only=True, citation=citation
    )

    contributors.drop(columns=["affiliation", "orcid"], inplace=True)
    contributors.to_csv(contributors_file, sep="\t", index=False)

    contributors_file = root_dir().joinpath(
        "data", "contributors", "neuroview_contributors.tsv"
    )
    contributors = pd.read_csv(contributors_file, sep="\t")

    citation = load_citation(citation_file)
    citation["authors"] = return_author_list_for_cff(contributors)
    citation_file = citation_file.parent.joinpath(citation_file.stem + "_neuroview.CFF")
    write_citation(citation_file, citation)
    citation = create_citation(infile=citation_file, url=None)
    validate_or_write_output(
        outfile=None, outputformat=None, validate_only=True, citation=citation
    )

    contributors.drop(columns=["affiliation", "orcid"], inplace=True)
    contributors.to_csv(contributors_file, sep="\t", index=False)


if __name__ == "__main__":
    main()
