.PHONY: data/brainhack-timeline_new.csv

pre: figures
all: pre book

figures:
	python scripts/generate_figures.py

book:
	jupyter-book build brainhack_book

test: figures
	jupyter-book build brainhack_book -W --builder linkcheck

validate_citation_cff: CITATION.cff
	cffconvert --validate

clean:
	rm -fr brainhack_book/_build/ brainhack_book/_*html

data/brainhack-timeline_new.csv:
	curl -L "https://docs.google.com/spreadsheets/d/121FUOXP9zE5lv7UhKR80RuCflQlpczwkxFB_rA1Pk_g/export?format=csv" \
	-o data/brainhack-timeline_new.csv
