"""
Author: Hao-Ting Wang 02.11.2021

The current script add authorship ranking for the manuscript.

Ranking spreadsheet was downloaded on 18:16 pm 02.11.2021
The download of the file is not automated due to API aurthorization needed.

1. Give ranking order
2. fuzzy matching of names between gsheet and osf sheet
3. copy ranking over to osf sheet
4. sort osf sheet
    - core member by ranking
    - general by alphabet of last name
5. run `neuroview_affiliations_organizer.sh`
6. copy the ranking to curated sheet

Usage:
python neuroview_author_ranking.py
"""
import re
import pandas as pd
import numpy as np

gsheet_file = "General and core team members - core team members.tsv"
osf_file = "affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv"
curated_file="./data/affiliations_curated.tsv"

ranking = pd.read_csv(f"data/{gsheet_file}", sep="\t", skiprows=1)
osf = pd.read_csv(f"data/{osf_file}", sep="\t", header=[0, 1, 2])

# give ranking in gsheet
ranking["ranking"] = ranking.index + 1

# fuzzy name match
rename_gsheet = {'Unnamed: 3': "First", 'Unnamed: 4': "Last"}
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
        print(row["Last"])
        # Remi was missed by last name search
        osf_mask_first = osf[osf_first].str.match(row["First"])
        osf_idx = osf.index[osf_mask_first]
    else:
        osf_idx = osf.index[osf_mask_last]
    # copy ranking
    osf.loc[osf_idx, ("", "", "ranking")] = row["ranking"]

# sort by original order, add serial id
# (this is the same generation principal the author ID in organised file)
osf = osf.sort_index()
osf[("", "", "Author_ID")] = np.arange(osf.shape[0]) + 1
osf.to_csv(f"data/ranking.tsv", index=False, sep="\t")

# update curated result
curated = pd.read_csv(curated_file, sep="\t")
curated["ranking"] = 0
for i, row in curated.iterrows():
    mask = osf[("", "", "Author_ID")] == row["Author_ID"]
    rank = osf[mask][("", "", "ranking")].tolist()[0]
    curated.loc[i, "ranking"] = rank
# sort by rank, save
curated = curated.sort_values("ranking")
curated.to_csv(f"data/affiliations_curated_ranked.tsv", index=False, sep="\t")

