neuroview: contributors brainhack_book/neuroview_acknowledgments.md brainhack_book/neuroview_contributors.md

osfid=4szct
osf_neuroviewcontributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_source.tsv

contributors:
	osf -p ${osfid} fetch ${osf_neuroviewcontributors} data/neuroview_contributors.tsv; \
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv

brainhack_book/neuroview_acknowledgments.md : data/neuroview_acknowledgments.csv data/neuroview_acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py neuroview acknowledgments; \

brainhack_book/neuroview_contributors.md : data/neuroview_contributors.tsv data/neuroview_contributors_descriptions.md  brainhack_book/mdtable.py
	python brainhack_book/mdtable.py neuroview contributors; \

brainhack_book/contributors.md : data/contributors.tsv data/contributors_descriptions.md brainhack_book/mdtable.py data/contributors.tsv
	python brainhack_book/mdtable.py contributors;

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/
