import pandas as pd


emails = False

DATA_DIR = "data/contributors/neuroview"

# curated = pd.read_csv(f"{DATA_DIR}/affiliation_curated.tsv", sep="\t")
raw = pd.read_csv(f"{DATA_DIR}/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv", sep="\t", header=[0, 1, 2])
tpt = pd.read_csv(f"{DATA_DIR}/affiliation_consent_and_contributions_for_the_brainhack_consortium_tripetto_raw.csv")

if emails:
    source_osf = pd.read_csv(f"{DATA_DIR}/affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv", sep="\t", header=[0, 1, 2])
    source_tpt = pd.read_csv(f"{DATA_DIR}/affiliation_consent_and_contributions_for_the_brainhack_consortium_tripetto_source.csv")

    # merge the email to raw sheet
    raw = raw.set_index(raw.columns[0])
    source_osf = source_osf.set_index(source_osf.columns[0])
    raw = pd.concat([raw, source_osf[source_osf.columns[14]]], axis=1, join="inner").reset_index()

    tpt = tpt.set_index("First and Last Name")
    source_tpt = source_tpt.set_index("First and Last Name")
    tpt = pd.concat([tpt, source_tpt["Email address"]], axis=1, join="inner").reset_index()

tpt["First and Last Name"] = tpt["First and Last Name"].str.split()
tpt["Affiliation"] = tpt["Affiliation"].str.split(", ")

# merge the raw
for i, row in tpt.iterrows():
    # curate_ix = (i + curated.shape[0])
    raw_ix = (i + raw.shape[0])
    if len(row["First and Last Name"]) == 2:
        # curated.loc[curate_ix, ["First", "Last"]] = row["First and Last Name"]
        raw.loc[raw_ix, [raw.columns[9], raw.columns[10]]] = row["First and Last Name"]
    else:
        # curated.loc[curate_ix, ["First", "Middle","Last"]] = row["First and Last Name"]
        raw.loc[raw_ix, [raw.columns[9], raw.columns[11], raw.columns[10]]] = row["First and Last Name"]

    # if len(row["Affiliation"]) == 4:
    #     curated.loc[curate_ix, ["Department", "Institute", "City", "Country"]] = row["Affiliation"]
    # else:
    #     curated.loc[curate_ix, "Department"] = ", ".join(row["Affiliation"])
    if emails:
        raw.loc[raw_ix, raw.columns[-1]] = row["Email address"]
    # curated.loc[curate_ix, "Author_ID"] = 156 + i
    # curated.loc[curate_ix, "Aff_Order"] = 1

raw.to_csv(f"{DATA_DIR}/tmp_tpt_merged_raw.tsv", sep="\t", index=False)
# curated.to_csv(f"{DATA_DIR}/tmp_tpt_merged_curated.tsv", sep="\t", index=False)