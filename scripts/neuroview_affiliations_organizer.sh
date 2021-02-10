#!/bin/bash

# edit filename
orig_file='/Users/steph//Downloads/affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw.tsv'


cut -f10-15 "$orig_file" > tmp

#reorder
awk -v OFS="\t" -F"\t" '{print $1,$3,$2,$4,$5,$6}' tmp > tmp2

#rename affiliation headers
sed 's#Affiliation (please use the format: Department / Institution / City / Country)#Department/Institution/City/Country#g; s#Your 2nd affiliation (optional) - please use same format as above#Department/Institution/City/Country#g; s#Your 3rd affiliation (optional) - please use same format as above#Department/Institution/City/Country#g' tmp2 > tmp3

# separate 1st-3rd affils
cut -f1-4 tmp3 > aff1
cut -f1-3,5 tmp3 > aff2
cut -f1-3,6 tmp3 > aff3

# columns for each affiliation subfield (separately in case there are issues)
sed 's#\/#	#g' aff1 > aff1_sep
sed 's#\/#	#g' aff2 > aff2_tmp
sed 's#\/#	#g' aff3 > aff3_tmp

# empty first 3 columns (names) for aff2 and aff3
awk -v OFS="\t" -F"\t" '{$1=""; $2=""; $3=""; print ;}' aff2_tmp > aff2_sep
awk -v OFS="\t" -F"\t" '{$1=""; $2=""; $3=""; print ;}' aff3_tmp > aff3_sep


# re-merge
paste -d '\n'  aff1_sep aff2_sep aff3_sep > tmp

# remove empty rows (whitespace)
sed '/^[[:space:]]*$/d' tmp > tmp2

# add empty column headers
# this seems not to like adding multiple empty columns next to each other - will have to figure it out
awk -F"\t" '{$1=FS$1;$5=FS$5;$6=FS$6;$7=FS$7;$9=FS$9;$11=FS$11;$13=FS$13;$14=FS$14}1' OFS="\t" tmp2 > affiliations_organized.txt


# you might want to clean up all those tmp* and aff* files - not all my tools support editing in place and I didn't want to mv everything
# rm tmp*; rm aff*
