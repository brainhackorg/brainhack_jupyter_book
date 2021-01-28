files: brainhack_book/acknowledgements.md data/contributors.tsv brainhack_book/contributions.md

osfid=4szct
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv

brainhack_book/acknowledgements.md : data/acknowledgements.csv data/acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py acknowledgements; \
	echo "build acknowledgements.md"

data/contributors.tsv :
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv; \
	echo "fetch contributors table from osf"

brainhack_book/contributiors.md : data/contributors.tsv data/contributors_descriptions.md  brainhack_book/mdtable.py
	python brainhack_book/mdtable.py contributors; \
	echo "build contributiors.md"

book :
	jupyter-book build brainhack_book