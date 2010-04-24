#!/usr/bin/python

import fasta
from fasta import fasta_itr
import sys

if len(sys.argv) < 2:
    print "usage:", sys.argv[0], "<fasta file>"
    exit()

fasta_file = sys.argv[1]

for rec in fasta_itr(fasta_file):
    print len(rec.sequence)
