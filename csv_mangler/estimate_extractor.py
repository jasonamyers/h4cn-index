#!/usr/bin/env python
"""Pulls data specified by table and sequence number from ACS estimate files.

This version is particularly stupid - it expects offsets within the ACS estimate file to be explicitly
specified on the command line, along with factor levels to be written in the output. At least it's flexible.
"""
import os
import lookup

ESTIMATE_FILE_FIRST_DATA_INDEX = 6
ESTIMATE_FILE_SEQUENCE_INDEX = 4
ESTIMATE_FILE_LOCREC_INDEX = 5

RELEVANT_LOCRECS = frozenset([int(k) for k in lookup.LOCRECNO_TO_DESCRIPTOR.keys()])

def sequence_to_filename(seq_number):
    return 'e20115tn%04d000.txt'%seq_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Pulls data from ACS estimate files')
    parser.add_argument('input',
        action='store',
        help='Path to directory containing input csv estimate files'
    )
    parser.add_argument('rectype',
        action='store',
        help='record type (e.g. POVERTY)'
    )
    parser.add_argument('sequence',
        action='store',
        type=int,
        help='sequence number (e.g. 1)'
    )
    parser.add_argument('-n1',
        action='append',
        default=[],
        help='Field name to give to output (e.g. WHITE)'
    )
    parser.add_argument('-n2',
        action='append',
        default=[],
        help='Field name to give to output (e.g. 20_25)'
    )
    parser.add_argument('-n3',
        action='append',
        default=[],
        help='Field name to give to output (e.g. FEMALE|MALE)'
    )
    parser.add_argument('-i','--idx',
                        type=int,
                        action='append',
                        default=[],
                        help="Index of data field to extract"
                        )
    parser.add_argument('--float',
                        action='store_true',
                        default=False,
                        help='Expect floating-point valued data (default integer)')
    args = parser.parse_args()

    cast_fcn = float if args.float else int

    # awkward handling of potentially multiple factor levels specified in command line args
    assert( len(args.n1) == len(args.idx) )
    assert( len(args.n2) == len(args.idx) or len(args.n2)==0 )
    assert( len(args.n3) == len(args.n2) or len(args.n3)==0 )

    if len(args.n3) and len(args.n2) > 0:
        name_idx_pairs = zip(args.n1, args.n2, args.n3, args.idx)
    elif len(args.n2) > 0:
        name_idx_pairs = zip(args.n1, args.n2, args.idx)
    else:
        name_idx_pairs = zip(args.n1, args.idx)

    fname = sequence_to_filename(args.sequence)
    f = file(os.path.join(args.input, fname))
    for line in f:
        toks = line.strip().split(",")
        sequence = int(toks[ESTIMATE_FILE_SEQUENCE_INDEX])
        logrec = int(toks[ESTIMATE_FILE_LOCREC_INDEX])

        if sequence == args.sequence and logrec in RELEVANT_LOCRECS:
            location = lookup.LOCRECNO_TO_DESCRIPTOR['%07d'%logrec].replace(' ','_')
            if len(args.n3) > 0:
                for n1,n2,n3,idx in name_idx_pairs:
                    try:
                        val = str(cast_fcn(toks[idx]))
                    except ValueError:
                        val = ''
                    print '%s,%s,%s,%s,%s,%s'%(args.rectype,location,n1,val,n2,n3)
            elif len(args.n2) > 0:
                for n1,n2,idx in name_idx_pairs:
                    try:
                        val = str(cast_fcn(toks[idx]))
                    except ValueError:
                        val = ''
                    print '%s,%s,%s,%s,%s'%(args.rectype,location,n1,val,n2)
            else:
                for n1,idx in name_idx_pairs:
                    try:
                        val = str(cast_fcn(toks[idx]))
                    except ValueError:
                        val = ''
                    print '%s,%s,%s,%s'%(args.rectype,location,val,n1)

    f.close()

