#!/usr/bin/env bash

# Script to extract INCOME table from 2 ACS 2007-2011 data files.
# source files are "e" (estimate) data files from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0060000.zip
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0061000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/income_by_district_and_race_130602d.csv

EXE="${ROOT}/estimate_extractor2.py ${DATA} INCOME"

SEQ=60
IDX=142 
${EXE} $SEQ -l1 ${ROOT}/factor_levels/income_levels.txt -l2 ${ROOT}/factor_levels/racial_levels1.txt --idx $IDX > $OUTPUT
${EXE} 61 -l1 ${ROOT}/factor_levels/income_levels.txt -l2 ${ROOT}/factor_levels/racial_levels2.txt --idx 6 >> $OUTPUT


