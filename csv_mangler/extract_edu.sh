#!/usr/bin/env bash

# Script to extract education level table from ACS 2007-2011 data.
# source file is "e" (estimate) data file from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0043000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/education_by_district_and_race_and_gender_130602d.csv

EXE="${ROOT}/estimate_extractor_edu_by_gender.py ${DATA} EDU"

SEQ=43
IDX=125
${EXE} $SEQ -l1 ${ROOT}/factor_levels/edu_levels.txt -l2 ${ROOT}/factor_levels/racial_levels_edu1.txt --idx $IDX > $OUTPUT


