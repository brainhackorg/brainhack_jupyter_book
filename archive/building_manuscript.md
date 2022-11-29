# Instructions to builld Neuroview related content

** Not needed now that the manuscript is published **

This document explains how to build some of the pages that are related to the
Neuroview paper.

## Adding new authors to the brainhack consortium

This is the procedure to add authors to the preprint under the Brainhack
consortium.

1.  Add the new member to the OSF project as a
    [non-bibliographic contributor](https://osf.io/4szct/contributors/).

- This can be made quicker if the person has a an OSF ID. Otherwise the person
  has to be added as an unregistered contributor with surname, name and email.
- Note that this might require Admin access to the project.
- Put the new member in the correct position (alphabetical order in the general
  team) and save the new contributor list.

2.  Add the new member to the [pre-print](https://psyarxiv.com/rytjq/)
    (`Edit preprint` --> `Authors` section) and follow the same procedure as
    above to put the person in the right position in the author list. This too
    might require admin access to the preprint.

### Update the list of authors in the PDF

1. Follow the [CONTRIBUTING](./CONTRIBUTING.md) instructions to generate an
   virtual environment and install all dependencies.

2. Add the late comer to the bottom of those 2 files:

   - `data/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv`
   - `data/affiliations_curated.tsv`
   - follow the format, check typo manually.
   - commit those changes to the repo.

3. Run the following command: `make manuscript`

4. Use the generated `data/authors_affiliations.tsv` (MUST be converted to
   `.xlsx` format to accomandate special characters) file as input in the online
   [NIH author arranger](https://authorarranger.nci.nih.gov/#/web-tool) to
   create the `authors_affiliations_preprint.docx` that contains the list of
   authors and affiliations.

5. Copy paste the relevant part of those lists in the
   [google doc ofd the manuscript](https://docs.google.com/document/d/1Rfjyb2ueF0BX0EavK9oCd1SfjdNb1CiaXTl5AjFWy9Y/edit?usp=sharing)

   - make sure to paste the "general team" members under the
     `Brainhack consortium` section.

6. Download the google doc as a PDF and upload the version of the preprint on
   psyarxiv.

## Updating the pages of the jupyter book with NeuroView related content

1. Run the following command:

`make contributors` `make bookpage`

Commit the resulting ouput and open a pull request to add the changes.

## Final cross-check

Make sure that the order of authors match:

- on the OSF project
- on the psyarxiv preprint
- in the pdf document
