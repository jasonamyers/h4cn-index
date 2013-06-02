Code for extracting data from 2007-2011 US Census American Community
Survey Summary File csv.

Original data from:
http://www2.census.gov/acs2011_5yr/summaryfile/
and
http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/

Basic format here is some python scripts to pull the data, coupled
with bash scripts that call the python with appropriate
arguments. So: bash -> python -> data output. Look in the bash scripts
first to understand what's going on here.

Assumed directory structure:

$ROOT -- *.py and *.sh
      |
      - data_orig (contains e20115tn*.txt files - see individual
      |		  extract_*.sh scripts for more info)
      _ data_extracted (holds results of *.sh scripts)

There is lots and lots of copy-pasted code between the various python
and bash scripts. Many of the python scripts have some slightly nasty
index mangling to make the data references come out right, especially
when data is pulled out separately for FEMALE and MALE.

The bash scripts all define a $ROOT variable, which should be the
directory containing the python code. data_orig and data_extracted are
expected to be subdirectories off of $ROOT. The original census
estimate data (files beginning with "e20115tn") should be in
$ROOT/data_orig. Each bash script should contain a link to the
original data source on the census web site in comments.

The best guide that I've found to the ACS Census data is:
http://www2.census.gov/acs2011_5yr/summaryfile/ACS_2007_2011_SF_Tech_Doc.pdf

The indicies for each data field are described in:
http://www2.census.gov/acs2011_5yr/summaryfile/Sequence_Number_and_Table_Number_Lookup.txt
or equivalently:
http://www2.census.gov/acs2011_5yr/summaryfile/Sequence_Number_and_Table_Number_Lookup.csv
