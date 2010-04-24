#!/usr/bin/python

import fasta
from fasta import fasta_itr
import sys

if len(sys.argv) < 2:
    print "usage:", sys.argv[0], "<fasta file>"
    exit()

fasta_file = sys.argv[1]

print '\t'.join(["header", "length", "a", "t", "g", "c", "at", "gc", "other"])

for rec in fasta_itr(fasta_file):
    l = len(rec.sequence)
    a,t,g,c,at,gc,other = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for bp in rec.sequence:
        if bp == 'A':
            a += 1
        elif bp == 'T':
            t += 1
        elif bp == 'G':
            g += 1
        elif bp == 'C':
            c += 1
        else:
            other += 1
    at = a + t
    gc = g + c
    print '\t'.join([rec.header, str(l)] + map(lambda count: str(count/l), [a, t, g, c, at, gc, other]))


