#!/usr/bin/env python

# Copyright (C) 2023, Yanhai Gong.
# gongyh@qibebt.ac.cn

# bins_stats is used to calc basic statistics of bins.

import os
import glob
import shutil
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import numpy

##################################################### CONFIGURATION ####################################################

parser = argparse.ArgumentParser()

parser.add_argument("-i", required=True, help="first bins folder name")

parser.add_argument("-o", required=True, help="output statistics file")

args = vars(parser.parse_args())
output_dir = args["o"]
if output_dir[-1] == "/":
    output_dir = output_dir + "stats.csv"

input_bin_folder = args["1"]
if input_bin_folder[-1] == "/":
    input_bin_folder = input_bin_folder[:-1]

######################################################### STATS ########################################################

wd = os.getcwd()

# get bin name list
bins_files = "%s/%s/*.fa" % (wd, input_bin_folder)

if len(bins_files) == 0:
    print(("No input bin detected from %s folder, please double-check!" % (bin_folder)))
    exit()

# calc statistics for each bin
out_fh = open(output_dir, "w")
out_fh.write("bin\tGC\tN50\tsize")

for bin_file in bins_files:
    bin = os.path.basename(bin_file)
    bin_file_name, bin_file_ext = os.path.splitext(bin)
    bin_content = SeqIO.parse(bin_file, "fasta")
    lengths = []
    num_gc = 0
    size = 0
    for contig in bin_content:
        contig_len = len(contig)
        size += contig_len
        lengths.append(contig_len)
        gc = sum(contig.seq.count(x) for x in "CGScgs")
    GC = gc / size
    all_len = sorted(lengths, reverse=True)
    csum = numpy.cumsum(all_len)
    csumn2 = min(csum[csum >= int(size / 2)])
    ind = numpy.where(csum == csumn2)
    n50 = all_len[ind[0]]
    out_fh.write("%s\t%.3f\t%d\t%d" % (bin_file_name, GC, n50, size))

out_fh.close()

print("\nAll done!")
