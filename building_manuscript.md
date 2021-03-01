# Instructions to builld Neuroview related content

This document explains how to build some of the pages that are related to the
Neuroview paper.

## Adding new authors to the brainhack consortium

This is the procedure to add authors to the preprint under the Brainhack
consortium.

1.  Add the new member to the OSF project as a
    [non-bibliographic contributor](https://osf.io/4szct/contributors/).

    - This can be made quicker if the person has a an OSF ID. Otherwise the
      person has to be added as an unregistered contributor with surname, name
      and email.
    - Note that this might require Admin access to the project.
    - Put the new member in the correct position (alphabetical order in the
      general team) and save the new contributor list.

2.  Add the new member to the [pre-print](https://psyarxiv.com/rytjq/)
    (`Edit preprint` --> `Authors` section) and follow the same procedure as
    above to put the person in the right position in the author list. This too
    might require admin access to the preprint.

3.  Update the list of authors in the PDF

    - Follow the [CONTRIBUTING](./CONTRIBUTING.md) instructions to generate an
      virtual environment and install all dependencies.

    - Add the late comer to the bottom of those 2 files:
      - `data/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv`
      - `data/affiliations_curated.tsv`
      - follow the format, check typo manually.

Run python script Run bash script (step 3- 5 can be achived by make
manuscript)\*\*

### Final cross-check

Make sure that the order of authors match:

- on the OSF project
- on the psyarxiv preprint
- in the pdf document
