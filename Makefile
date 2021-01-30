files: brainhack_book/acknowledgements.md brainhack_book/contributors.md

osfid=4szct
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv

brainhack_book/acknowledgements.md : data/acknowledgements.csv data/acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py acknowledgements; \
	echo "build acknowledgements.md"

brainhack_book/contributors.md : data/contributors_descriptions.md  brainhack_book/mdtable.py
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv; \
	python brainhack_book/mdtable.py contributors; \
	echo "build contributors.md"

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/