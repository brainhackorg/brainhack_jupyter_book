osfid=4szct
osf_neuroviewcontributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv
osf_contributors=affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv

contributors:
	osf -p ${osfid} fetch ${osf_neuroviewcontributors} data/preprint_contributors.tsv; \
	osf -p ${osfid} fetch ${osf_contributors} data/contributors.tsv

brainhack_book/preprint_acknowledgments.md : data/preprint_acknowledgments.csv brainhack_book/preprint_acknowledgments_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py -f data/preprint_acknowledgments.csv \
		-d brainhack_book/preprint_acknowledgments_descriptions.md \
		-t brainhack_book/preprint_acknowledgments.md --contributor;

brainhack_book/preprint_contributors.md : data/preprint_contributors.tsv brainhack_book/preprint_contributors_descriptions.md  brainhack_book/mdtable.py
	python brainhack_book/mdtable.py -f data/preprint_contributors.tsv \
		-d brainhack_book/preprint_contributors_descriptions.md \
		-t brainhack_book/preprint_contributors.md --contributor;

brainhack_book/contributors.md : data/contributors.tsv brainhack_book/contributors_descriptions.md brainhack_book/mdtable.py data/contributors.tsv
	python brainhack_book/mdtable.py -f data/contributors.tsv \
		-d brainhack_book/contributors_descriptions.md \
		-t brainhack_book/contributors.md --contributor;

brainhack_book/acknowledgments.md : data/acknowledgments.csv brainhack_book/acknowledgments_descriptions.md brainhack_book/mdtable.py
	python brainhack_book/mdtable.py -f data/acknowledgments.csv \
		-d brainhack_book/acknowledgments_descriptions.md \
		-t brainhack_book/acknowledgments.md --contributor;

preprint: brainhack_book/preprint_acknowledgments.md brainhack_book/preprint_contributors.md

bookpage: brainhack_book/contributors.md brainhack_book/acknowledgments.md

book :
	jupyter-book build brainhack_book

clean :
	rm -r brainhack_book/_build/
	# rm data/*contributors.tsv
	rm brainhack_book/preprint_acknowledgments.md
	rm brainhack_book/preprint_contributors.md
	rm brainhack_book/contributors.md
	rm brainhack_book/acknowledgments.md

