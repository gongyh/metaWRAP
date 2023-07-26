#!/usr/bin/env python
import sys

# This script summarizes the statistics of each bin by parsing
# the eukcc_folder/eukcc.csv file of the EukCC output


if len(sys.argv) == 3:
    binner = sys.argv[2]
    print("bin\tcompleteness\tcontamination\tGC\tlineage\tN50\tsize\tbinner")
elif len(sys.argv) == 4:
    source = {}
    for line in open(sys.argv[3]):
        cut = line.strip().split("\t")
        source[cut[0]] = cut[7]
    print("bin\tcompleteness\tcontamination\tGC\tlineage\tN50\tsize\tbinner")
else:
    print("bin\tcompleteness\tcontamination\tGC\tlineage\tN50\tsize")


for line in open(sys.argv[1]):
    cl = line.strip().split("\t")
    c0 = cl[0]
    if c0 == "bin":  # header
        continue
    name = c0[:-3]
    if len(sys.argv) == 3:
        print("\t".join([name, cl[1], cl[2], cl[3], "", cl[4], cl[5], binner]))

    elif len(sys.argv) == 4:
        print("\t".join([name, cl[1], cl[2], cl[3], "", cl[4], cl[5], source[name]]))

    else:
        print("\t".join([name, cl[1], cl[2], cl[3], "", cl[4], cl[5]]))
