#!/bin/bash
# Original script: Stephanie Noble Feb 09 2021
# Edited by Hao-Ting Wang Feb 10 2021
# Cleaning the paper affiliation for authorarranger to generate author list
# The file contain special charactors, so the final tsv needs to be saved as a xlsx file MANUALLY
# authorarranger:
# https://authorarranger.nci.nih.gov/#/user-guide
#
# Usage:
# bash neuroview_affiliations_organizer.sh


python scripts/trippetto_to_curated.py
python scripts/neuroview_author_ranking.py

cd data/contributors/neuroview/
# edit filename
orig_file="affiliation_and_consent_for_the_brainhack_neuroview_preprint_raw_ranked.tsv"
out_file="manscript_affiliation.tsv"

cut -f10-15 "$orig_file" > tmp_auth
cat "$orig_file" | rev | cut -f 4 | rev > tmp_email
paste -d '\t' tmp_auth tmp_email > tmp

#reorder and remove the first two lines
awk -v OFS="\t" -F"\t" 'NR > 2 {print $1,$3,$2,$7,$4,$5,$6}' tmp > tmp2

#rename affiliation headers
sed 's#Affiliation (please use the format: Department / Institution / City / Country)#Department / Institute / City / Country#g; s#Your 2nd affiliation (optional) - please use same format as above#Department / Institute / City / Country#g; s#Your 3rd affiliation (optional) - please use same format as above#Department / Institute / City / Country#g' tmp2 > tmp3

# separate 1st-3rd affils
cut -f1-5 tmp3 > aff1
cut -f1-4,6 tmp3 > aff2
cut -f1-4,7 tmp3 > aff3

# remove forward slash as well as white space separate by tab explicitly
sed 's: / :\t:g' aff1 > aff1_tmp
sed 's: / :\t:g' aff2 > aff2_tmp
sed 's: / :\t:g' aff3 > aff3_tmp

# empty first 4 columns (names) for aff2 and aff3
awk -v OFS="\t" -F"\t" '{$1=""; $2=""; $3=""; $4=""; print ;}' aff2_tmp > aff2_tmp2
awk -v OFS="\t" -F"\t" '{$1=""; $2=""; $3=""; $4=""; print ;}' aff3_tmp > aff3_tmp2

# add line number to start of the line (NR-1: as subject ID) and affiliation order(1; 2; 3)
awk -v OFS="\t" -F"\t" '{print NR-1,1,$s}' aff1_tmp > aff1_sep
awk -v OFS="\t" -F"\t" '{print NR-1,2,$s}' aff2_tmp2 > aff2_sep
awk -v OFS="\t" -F"\t" '{print NR-1,3,$s}' aff3_tmp2 > aff3_sep

# re-merge
paste -d '\n' aff1_sep aff2_sep aff3_sep > tmp

# remove lines that does not contain alphabets (lines with line number and tabs only)
sed '/[[:alpha:]]/!d' tmp > $out_file

# remove line 2 and three
sed -i '2d;3d' $out_file

# replace some header labels to fit AuthorArranger in line 1 (header)
sed -i '1!b;s/0/ranking/' $out_file
sed -i '1!b;s/1/Aff_Order/' $out_file
sed -i '1!b;s/First name/First/' $out_file
sed -i '1!b;s/Middle initial(s)/Middle/' $out_file
sed -i '1!b;s/Last name/Last/' $out_file

# you might want to clean up all those tmp* and aff* files - not all my tools support editing in place and I didn't want to mv everything
rm *tmp*; rm aff?; rm aff?_sep
echo "======================================================================================"
echo "Now, manually save data/contributors/neuroview/$out_file to a xlsx file, pass it to AuthorArrange"
echo "https://authorarranger.nci.nih.gov/#/user-guide"
echo "======================================================================================"