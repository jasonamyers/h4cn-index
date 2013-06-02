#!/usr/bin/env bash

# Script to extract median income table from ACS 2007-2011 data.
# source file is "e" (estimate) data file from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0069000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/medianincome_by_district_and_race_and_gender_130602d.csv

EXE="${ROOT}/estimate_extractor.py ${DATA}"
# looking at full-time workers only
SEQ=69
${EXE} MEDIANINCOME $SEQ -n1 ALL -n2 MALE -i 103 -n1 ALL -n2 FEMALE -i 106 -n1 WHITE -n2 MALE -i 110 -n1 WHITE -n2 FEMALE -i 113 -n1 AFAM -n2 MALE -i 117 -n1 AFAM -n2 FEMALE -i 120 -n1 AMERIND -n2 MALE -i 124 -n1 AMERIND -n2 FEMALE -i 127 -n1 ASIAN -n2 MALE -i 131 -n1 ASIAN -n2 FEMALE -i 134 -n1 PACISL -n2 MALE -i 138 -n1 PACISL -n2 FEMALE -i 141 -n1 OTHER -n2 MALE -i 145 -n1 OTHER -n2 FEMALE -i 148 -n1 MIXED -n2 MALE -i 152 -n1 MIXED -n2 FEMALE -i 155 -n1 WHITE_NONLATIN -n2 MALE -i 159 -n1 WHITE_NONLATIN -n2 FEMALE -i 162 -n1 LATIN -n2 MALE -i 166 -n1 LATIN -n2 FEMALE -i 169 > $OUTPUT
