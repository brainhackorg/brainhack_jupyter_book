files: brainhack_book/neuroview_acknowledgments.md brainhack_book/neuroview_contributors.md

osfid=4szct
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv

brainhack_book/neuroview_acknowledgments.md : data/acknowledgments.csv data/neuroview_acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py acknowledgments; \

brainhack_book/neuroview_contributors.md : data/neuroview_contributors_descriptions.md  brainhack_book/mdtable.py
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv; \
	python brainhack_book/mdtable.py contributors; \

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/