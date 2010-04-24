#!/usr/bin/python

# Erik Garrison <erik.garrison@bc.edu>

import fasta
from fasta import fasta_itr
import sys
import gzip

if len(sys.argv) < 3:
    print "usage:", sys.argv[0], "<mate1 fq.gz> <mate2 fq.gz>"
    print "Interleave and name mates from two files."
    print "Names the mates as current name appended with _1 or _2."
    print "For use in formatting input for ABySS."
    print "author: Erik Garrison <erik.garrison@bc.edu>"
    exit()

mate1_file = sys.argv[1]
mate2_file = sys.argv[2]

f1 = gzip.open(mate1_file)
f2 = gzip.open(mate2_file)

read_mate1 = ""
read_mate2 = ""

def get_next_read(file):
    header = ""
    sequence = ""
    header = file.readline()
    for i in range(0,3):
        line = file.readline()
        if not line:
            raise Exception("End of File")
        sequence += line
    return (header, sequence)

while True:
    try:
        for file in [(f1, "_1"),(f2, "_2")]:
            header, sequence = get_next_read(file[0])
            sys.stdout.write(header.strip() + file[1] + "\n")
            sys.stdout.write(sequence)
    except:
        break

sys.stdout.flush()
