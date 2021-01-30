neuroview: brainhack_book/neuroview_acknowledgments.md brainhack_book/neuroview_contributors.md

bookpages: brainhack_book/acknowledgments.md brainhack_book/contributors.md

osfid=4szct
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv

brainhack_book/neuroview_acknowledgments.md : data/neuroview_acknowledgments.csv data/neuroview_acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py neuroview acknowledgments; \

brainhack_book/neuroview_contributors.md : data/neuroview_contributors_descriptions.md  brainhack_book/mdtable.py
	osf -p ${osfid} fetch ${osf_contributors} data/neuroview_contributors.tsv; \
	python brainhack_book/mdtable.py neuroview contributors; \

brainhack_book/acknowledgments.md : data/acknowledgments.csv data/neuroview_acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py acknowledgments; \

brainhack_book/contributors.md : data/contributors_descriptions.md  brainhack_book/mdtable.py
	osf -p ${osfid} fetch ${osf_contributors} data/neuroview_acknowledgments.tsv; \
	python brainhack_book/mdtable.py contributors; \

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/