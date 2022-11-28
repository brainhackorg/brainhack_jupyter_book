pre: neuroview bookpage
all: pre book

brainhack_book/neuroview_contributors.md : data/contributors/neuroview_contributors.tsv brainhack_book/neuroview_contributors_descriptions.md  scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/contributors/neuroview_contributors.tsv \
		-d brainhack_book/neuroview_contributors_descriptions.md \
		-t brainhack_book/neuroview_contributors.md ;

brainhack_book/contributors.md : data/contributors/contributors.tsv brainhack_book/contributors_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/contributors/contributors.tsv \
		-d brainhack_book/contributors_descriptions.md \
		-t brainhack_book/contributors.md ;

brainhack_book/neuroview_acknowledgments.md : data/acknowledgments/neuroview_acknowledgments.csv brainhack_book/neuroview_acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/acknowledgments/neuroview_acknowledgments.csv \
		-d brainhack_book/neuroview_acknowledgments_descriptions.md \
		-t brainhack_book/neuroview_acknowledgments.md;

brainhack_book/acknowledgments.md : data/acknowledgments/acknowledgments.csv brainhack_book/acknowledgments_descriptions.md scripts/mdtable.py
	python scripts/mdtable.py \
		-f data/acknowledgments/acknowledgments.csv \
		-d brainhack_book/acknowledgments_descriptions.md \
		-t brainhack_book/acknowledgments.md;

neuroview: brainhack_book/neuroview_acknowledgments.md brainhack_book/neuroview_contributors.md

bookpage: brainhack_book/contributors.md brainhack_book/acknowledgments.md

book :
	jupyter-book build brainhack_book

test :
	jupyter-book build brainhack_book -W --builder linkcheck

clean :
	rm -fr brainhack_book/_build/
	rm -f brainhack_book/neuroview_acknowledgments.md
	rm -f brainhack_book/neuroview_contributors.md
	rm -f brainhack_book/contributors.md
	rm -f brainhack_book/acknowledgments.md
