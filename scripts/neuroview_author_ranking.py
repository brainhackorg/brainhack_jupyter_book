"""
Author: Hao-Ting Wang 02.11.2021

The current script add authorship ranking for the manuscript
and update OSF sheet with curated affiliation.

The curated affiliation "affiliations_curated.tsv" should be
updated when there's new entry in osf file. The Author ID is
should be continueous number starting from 1. All information
should be condfined to the header.

Ranking spreadsheet was downloaded on 20:48 pm 02.11.2021 GMT +0
The download of the file is not automated due to API aurthorization needed.

1. Give ranking order in gsheet
2. fuzzy matching of names between gsheet and osf sheet
3. copy ranking over to osf sheet
4. Update osf sheet with curated file on name and affiliations

The output is passed to `neuroview_affiliations_organizer.sh`
to generate Author Arrange suited format.

Usage:
python neuroview_author_ranking.py
"""
import sys
import re
import pandas as pd
import numpy as np

GSHEET_RANK = "coreteam_ranking.tsv"
OSF_RAW = "affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv"
AFF_CURATED = "affiliations_curated.tsv"
err_message = """Curated sheet and OSF sheet has unmatched number of auhtors.
Have you update curated sheet?"""

def assert_exit(condition, err_message):
    try:
        assert condition
    except AssertionError as Error:
        sys.exit(err_message)

ranking = pd.read_csv(f"data/{GSHEET_RANK}", sep="\t", skiprows=1)
osf = pd.read_csv(f"data/{OSF_RAW}", sep="\t", header=[0, 1, 2])
curated = pd.read_csv(f"data/{AFF_CURATED}", sep="\t")
curated = curated.fillna(" ")  # some authors has empty department info

assert_exit(curated["Author_ID"].unique().shape[0]==osf.shape[0], err_message)

# give ranking in gsheet
ranking["ranking"] = ranking.index + 1

# fuzzy name match between gsheet and osf
rename_gsheet = {'Unnamed: 1': "First", 'Unnamed: 2': "Last"}
ranking = ranking.rename(columns=rename_gsheet)
# sort osf sheet by last name and give ranking
osf_last = osf.columns[10]
osf_first = osf.columns[9]
osf = osf.iloc[osf[osf_last].str.lower().argsort()]  # ignore case when sorting
# assign ranking alphabetically;
# a general author will have a value > 1000
osf[("", "", "ranking")] = 1000 + np.arange(osf.shape[0])

for i, row in ranking.iterrows():
    # match last name, ignore case
    osf_mask_last = osf[osf_last].str.contains(row["Last"], flags=re.IGNORECASE)

    if sum(osf_mask_last) != 1:
        print(f"handle this case by first name: {row['Last']}")
        # Remi was missed by last name search
        osf_mask_first = osf[osf_first].str.match(row["First"])
        osf_idx = osf.index[osf_mask_first]
    else:
        osf_idx = osf.index[osf_mask_last]
    # copy ranking
    osf.loc[osf_idx, ("", "", "ranking")] = row["ranking"]

# add serial id with ame generation principal the author ID in organised file
osf = osf.sort_index()
author_ID = list(range(1, osf.shape[0] + 1))
osf[("", "", "Author_ID")] = author_ID

# update curated result to the OSF sheet
# parse curated stuff to dictionary for easy look up
revert_curate = []
for id in author_ID:  # some people's name are not capitalised etc so use ID
    mask_lines = curated["Author_ID"] == id
    lines = curated[mask_lines]
    author = {"Author_ID": id,
              "First": lines["First"].iloc[0],
              "Middle": lines["Middle"].iloc[0],
              "Last": lines["Last"].iloc[0]}
    aff = lines.loc[:, "Department":"Country"]
    for i in range(lines.shape[0]):
        author[f"affiliation_{i + 1}"] = aff.iloc[i].to_dict()
    revert_curate.append(author)

# dictionary to translate curated data and osf file
label_matcher = {"Author_ID": ("", "", "Author_ID"),
                 "First": osf.columns[9],
                 "Middle": osf.columns[11],
                 "Last": osf.columns[10],
                 "affiliation_1": osf.columns[12],
                 "affiliation_2": osf.columns[13],
                 "affiliation_3": osf.columns[14]}

# update osf sheet with curated content
for ca in revert_curate:
    for key, item in ca.items():
        if "Author_ID" in key:
            # find osf dataframe index
            mask = osf[label_matcher[key]] == ca[key]
            osf_idx = osf[mask].index
        elif "affiliation" in key:
            osf.loc[osf_idx, label_matcher[key]] = " / ".join(item.values())
        else:
            osf.loc[osf_idx, label_matcher[key]] = item

# sort the final result by ranking
osf = osf.sort_values(("", "", "ranking"))

# string quote set to "+" because there are valid strings with " or '
osf.to_csv("data/tmp_affiliations_curated_ranked.tsv",
           index=False, sep="\t", quotechar="+")