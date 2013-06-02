#!/usr/bin/env python
"""Pulls data specified by table and sequence number from ACS estimate files.

Quite similar to estimate_extractor_edu_by_gender, with different hardcoded skip values
to handle the different spacing of occupation data between MALE and FEMALE.
"""
import os
import itertools
import lookup

ESTIMATE_FILE_FIRST_DATA_INDEX = 6
ESTIMATE_FILE_SEQUENCE_INDEX = 4
ESTIMATE_FILE_LOCREC_INDEX = 5

GENDER_OFFSET = 6

RELEVANT_LOCRECS = frozenset([int(k) for k in lookup.LOCRECNO_TO_DESCRIPTOR.keys()])

def sequence_to_filename(seq_number):
    return 'e20115tn%04d000.txt'%seq_number

def load_levels_file(fname):
    """Returns sequence of string level names
    """
    f = open(fname, 'r')
    try:
        lines = f.readlines()
    finally:
        f.close()
    levels = []
    for line in lines:
        level = line.strip()
        if (not level.startswith('#')) and (not level==''):
            levels.append(level)
    return levels

def generate_factors(inner_levels, outer_levels):
    init_factors = list(itertools.product(outer_levels, inner_levels))
    factors = [(f[1], f[0]) for f in init_factors]
    return factors

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Pulls data from ACS estimate files')
    parser.add_argument('input',
        action='store',
        help='Path to directory containing input csv estimate files'
    )
    parser.add_argument('rectype',
        action='store',
        help='record type (e.g. OCC)'
    )
    parser.add_argument('sequence',
        action='store',
        type=int,
        help='sequence number (e.g. 1)'
    )
    parser.add_argument('-l1',
        action='store',
        default=None,
        help='Filename containing levels for factor 1'
    )
    parser.add_argument('-l2',
        action='store',
        default=None,
        help='Filename containing levels for factor 2'
    )
    parser.add_argument('--idx',
                        type=int,
                        action='store',
                        help="Index of first data field to extract"
                        )
    args = parser.parse_args()

    levels1 = load_levels_file(args.l1)
    if not args.l2 is None:
        levels2 = load_levels_file(args.l2)
    else:
        levels2 = ['ALL']

    factors = generate_factors(levels1, levels2)

    fname = sequence_to_filename(args.sequence)
    f = file(os.path.join(args.input, fname))
    for line in f:
        toks = line.strip().split(",")
        sequence = int(toks[ESTIMATE_FILE_SEQUENCE_INDEX])
        logrec = int(toks[ESTIMATE_FILE_LOCREC_INDEX])

        if sequence == args.sequence and logrec in RELEVANT_LOCRECS:
            location = lookup.LOCRECNO_TO_DESCRIPTOR['%07d'%logrec].replace(' ','_')
            idx = args.idx
            for n1,n2 in factors:
                # hardcode skip of total across genders
                if n1=='ALL' and not n2=='WHITE':
                    idx+=GENDER_OFFSET+1
                male_val = int(toks[idx])
                female_val = int(toks[idx+GENDER_OFFSET])
                idx += 1
                print '%s,%s,%s,%d,%s,MALE'%(args.rectype,location,n2,male_val,n1)
                print '%s,%s,%s,%d,%s,FEMALE'%(args.rectype,location,n2,female_val,n1)



