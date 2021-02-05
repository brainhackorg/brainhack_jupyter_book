osfid=4szct
osf_neuroviewcontributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv

contributors:
	osf -p ${osfid} fetch ${osf_neuroviewcontributors} data/preprint_contributors.tsv; \
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv

brainhack_book/preprint_acknowledgments.md : data/preprint_acknowledgments.csv data/preprint_acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py preprint acknowledgments; \

brainhack_book/preprint_contributors.md : data/preprint_contributors.tsv data/preprint_contributors_descriptions.md  brainhack_book/mdtable.py
	python brainhack_book/mdtable.py preprint contributors; \

brainhack_book/contributors.md : data/contributors.tsv data/contributors_descriptions.md brainhack_book/mdtable.py data/contributors.tsv
	python brainhack_book/mdtable.py contributors;

brainhack_book/acknowledgments.md : data/acknowledgments.csv data/acknowledgements_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py acknowledgments; \

preprint: contributors brainhack_book/preprint_acknowledgments.md brainhack_book/preprint_contributors.md

bookpage: contributors brainhack_book/contributors.md brainhack_book/acknowledgments.md

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/
	rm data/*contributors.tsv
	rm brainhack_book/preprint_acknowledgments.md
	rm brainhack_book/preprint_contributors.md
	rm brainhack_book/contributors.md
	rm brainhack_book/acknowledgments.md

