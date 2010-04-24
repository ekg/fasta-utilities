#!/usr/bin/python

import fasta
from fasta import fasta_itr
import sys

if len(sys.argv) < 3:
    print "usage:", sys.argv[0], "<contig_file> <contig length cutoff>"
    exit()

contig_file = sys.argv[1]
cutoff = int(sys.argv[2])

for rec in fasta_itr(contig_file):
    if len(rec.sequence) > cutoff:
        print rec
