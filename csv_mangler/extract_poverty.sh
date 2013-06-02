#!/usr/bin/env bash

# Script to extract POVERTY table from 3 ACS 2007-2011 data files.
# source files are "e" (estimate) data files from:
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0047000.zip
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0048000.zip
# http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/20115tn0049000.zip

ROOT=/data/hack4change2013/csv_mangler
DATA=${ROOT}/data_orig/
OUTPUT=${ROOT}/data_extracted/poverty_by_district_and_race_130602d.csv

EXE="${ROOT}/estimate_extractor.py ${DATA}"

${EXE} POVERTY 47 -n1 ALL -n2 ALL -i 6 -n1 ALL -n2 POVERTY -i 7 -n1 WHITE -n2 ALL -i 65 -n1 WHITE -n2 POVERTY -i 66 -n1 AFAM -n2 ALL -i 124 -n1 AFAM -n2 POVERTY -i 125 -n1 AMERIND -n2 ALL -i 183 -n1 AMERIND -n2 POVERTY -i 184 > $OUTPUT
${EXE} POVERTY 48 -n1 ASIAN -n2 ALL -i 6 -n1 ASIAN -n2 POVERTY -i 7 -n1 PACISL -n2 ALL -i 65 -n1 PACISL -n2 POVERTY -i 66 -n1 OTHER -n2 ALL -i 124 -n1 OTHER -n2 POVERTY -i 125 -n1 MIXED -n2 ALL -i 183 -n1 MIXED -n2 POVERTY -i 184 >> $OUTPUT
${EXE} POVERTY 49 -n1 WHITE_NONLATIN -n2 ALL -i 6 -n1 WHITE_NONLATIN -n2 POVERTY -i 7 -n1 LATIN -n2 ALL -i 65 -n1 LATIN -n2 POVERTY -i 66 >> $OUTPUT
