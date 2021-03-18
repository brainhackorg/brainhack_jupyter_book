pre: preprint bookpage
all: pre book

brainhack_book/preprint_contributors.md : data/contributors/preprint_contributors.tsv brainhack_book/preprint_contributors_descriptions.md  scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/contributors/preprint_contributors.tsv \
		-d brainhack_book/preprint_contributors_descriptions.md \
		-t brainhack_book/preprint_contributors.md ;

brainhack_book/contributors.md : data/contributors/contributors.tsv brainhack_book/contributors_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/contributors/contributors.tsv \
		-d brainhack_book/contributors_descriptions.md \
		-t brainhack_book/contributors.md ;

brainhack_book/preprint_acknowledgments.md : data/acknowledgments/preprint_acknowledgments.csv brainhack_book/preprint_acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/acknowledgments/preprint_acknowledgments.csv \
		-d brainhack_book/preprint_acknowledgments_descriptions.md \
		-t brainhack_book/preprint_acknowledgments.md;

brainhack_book/acknowledgments.md : data/acknowledgments/acknowledgments.csv brainhack_book/acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/acknowledgments/acknowledgments.csv \
		-d brainhack_book/acknowledgments_descriptions.md \
		-t brainhack_book/acknowledgments.md;

preprint: brainhack_book/preprint_acknowledgments.md brainhack_book/preprint_contributors.md

bookpage: brainhack_book/contributors.md brainhack_book/acknowledgments.md

manuscript : data/contributors/neuroview/affiliation_curated.tsv data/contributors/neuroview/coreteam_ranking.tsv
	bash scripts/neuroview_affiliations_organizer.sh no-email

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
