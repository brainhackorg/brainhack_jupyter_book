neuroviewcontributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv

pre: contributors preprint bookpage
all: pre book

contributors:
	osf -p ${osfid} fetch -f ${osf_neuroviewcontributors} data/${osf_neuroviewcontributors}
	cp data/${osf_neuroviewcontributors} data/contributors.tsv
	cp data/${osf_neuroviewcontributors} data/preprint_contributors.tsv

brainhack_book/preprint_contributors.md : data/preprint_contributors.tsv brainhack_book/preprint_contributors_descriptions.md  scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/preprint_contributors.tsv \
		-d brainhack_book/preprint_contributors_descriptions.md \
		-t brainhack_book/preprint_contributors.md \
		--contributor;

brainhack_book/contributors.md : data/contributors.tsv brainhack_book/contributors_descriptions.md scripts/mdtable.py data/contributors.tsv
	python scripts/mdtable.py \
		-f data/contributors.tsv \
		-d brainhack_book/contributors_descriptions.md \
		-t brainhack_book/contributors.md \
		--contributor;

brainhack_book/preprint_acknowledgments.md : data/preprint_acknowledgments.csv brainhack_book/preprint_acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/preprint_acknowledgments.csv \
		-d brainhack_book/preprint_acknowledgments_descriptions.md \
		-t brainhack_book/preprint_acknowledgments.md;

brainhack_book/acknowledgments.md : data/acknowledgments.csv brainhack_book/acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/acknowledgments.csv \
		-d brainhack_book/acknowledgments_descriptions.md \
		-t brainhack_book/acknowledgments.md;

preprint: brainhack_book/preprint_acknowledgments.md brainhack_book/preprint_contributors.md

bookpage: brainhack_book/contributors.md brainhack_book/acknowledgments.md

manuscript : data/affiliations_curated.tsv data/coreteam_ranking.tsv
ifeq (,$(wildcard data/${neuroviewcontributors}))
	osf -p ${osfid} fetch ${neuroviewcontributors} data/${neuroviewcontributors}
endif
	python scripts/neuroview_author_ranking.py
	bash scripts/neuroview_affiliations_organizer.sh

book :
	jupyter-book build brainhack_book

test :
	jupyter-book build brainhack_book -W --builder linkcheck

clean :
	rm -fr brainhack_book/_build/
	rm -f brainhack_book/preprint_acknowledgments.md
	rm -f brainhack_book/preprint_contributors.md
	rm -f brainhack_book/contributors.md
	rm -f brainhack_book/acknowledgments.md
	rm -f data/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv
	rm -f data/contributors.tsv
	rm -f data/preprint_contributors.tsv