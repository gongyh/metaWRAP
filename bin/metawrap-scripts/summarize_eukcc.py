#!/usr/bin/env python
import sys
# This script summarizes the statistics of each bin by parsing 
# the eukcc_folder/eukcc.csv file of the EukCC output


if len(sys.argv)==3: 
	binner=sys.argv[2]
	print("bin\tcompleteness\tcontamination\tbinner")
elif len(sys.argv)==4:
	source={}
	for line in open(sys.argv[3]):
		cut=line.strip().split("\t")
		source[cut[0]]=cut[7]
	print("bin\tcompleteness\tcontamination\tbinner")
else:
	print("bin\tcompleteness\tcontamination")


for line in open(sys.argv[1]):
	dic=eval(line.strip().split("\t")[1])
	name=line.split("\t")[0]


	if len(sys.argv)==3:	
		print("\t".join([name, str(dic["completeness"]),\
		 str(dic["contamination"]), binner]))

	elif len(sys.argv)==4:
		print("\t".join([name, str(dic["completeness"]),\
		 str(dic["contamination"]), source[name]]))

	else:
		print("\t".join([name, str(dic["completeness"]),\
		 str(dic["contamination"])[:5]]))
