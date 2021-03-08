import pandas as pd

curated = pd.read_csv("data/affiliations_curated.tsv", sep="\t")
raw = pd.read_csv("data/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv", sep="\t", header=[0, 1, 2])
tpt = pd.read_csv("data/affiliation_consent_and_contributions_for_the_brainhack_consortium_tripetto.csv")

tpt["First and Last Name"] = tpt["First and Last Name"].str.split()
tpt["Affiliation"] = tpt["Affiliation"].str.split(", ")


for i, row in tpt.iterrows():
    curate_ix = (i + curated.shape[0])
    raw_ix = (i + raw.shape[0])
    if len(row["First and Last Name"]) == 2:
        curated.loc[curate_ix, ["First", "Last"]] = row["First and Last Name"]
        raw.loc[raw_ix, [raw.columns[9], raw.columns[10]]] = row["First and Last Name"]
    else:
        curated.loc[curate_ix, ["First", "Middle","Last"]] = row["First and Last Name"]
        raw.loc[raw_ix, [raw.columns[9], raw.columns[11], raw.columns[10]]] = row["First and Last Name"]

    if len(row["Affiliation"]) == 4:
        curated.loc[curate_ix, ["Department", "Institute", "City", "Country"]] = row["Affiliation"]
    else:
        curated.loc[curate_ix, "Department"] = ", ".join(row["Affiliation"])
    curated.loc[curate_ix, "Author_ID"] = 156 + i
    curated.loc[curate_ix, "Aff_Order"] = 1


raw.to_csv("data/tmp_tpt_merged_raw.tsv", sep="\t", index=False)
curated.to_csv("data/tmp_tpt_merged_curated.tsv", sep="\t", index=False)