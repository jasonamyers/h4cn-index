#!/usr/bin/env bash

# Script to extract OCC table from ACS 2007-2011 data.
# source file is "e" (estimate) data file from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0076000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/occuptation_by_district_and_race_and_gender_130602d.csv

EXE="${ROOT}/estimate_extractor_occupation_by_gender.py ${DATA} OCC"

SEQ=76
IDX=116
${EXE} $SEQ -l1 ${ROOT}/factor_levels/occ_levels.txt -l2 ${ROOT}/factor_levels/racial_levels_occ1.txt --idx $IDX > $OUTPUT


