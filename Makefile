pre: neuroview bookpage
all: pre book

book :
	jupyter-book build brainhack_book

test :
	jupyter-book build brainhack_book -W --builder linkcheck

validate_citation_cff: CITATION.cff
	cffconvert --validate

clean :
	rm -fr brainhack_book/_build/
