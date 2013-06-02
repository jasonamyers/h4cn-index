#!/usr/bin/env bash

# Script to extract Gini inequality coefficient table from ACS 2007-2011 data.
# http://en.wikipedia.org/wiki/Gini_coefficient
# source file is "e" (estimate) data file from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0060000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/gini_by_district_130602d.csv

EXE="${ROOT}/estimate_extractor.py ${DATA}"
SEQ=60
${EXE} GINICOEFF $SEQ --float -n1 ALL -i 141 > $OUTPUT
