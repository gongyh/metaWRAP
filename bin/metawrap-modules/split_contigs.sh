#!/usr/bin/env bash

##############################################################################################################################################################
#
# This script is meant to split assembled contigs into euk_contigs and pro_contigs
#
# Author of pipeline: Yanhai Gong. I do not have any authorship of the many programs this pipeline uses.
# For questions, bugs, and suggestions, contact me at gongyh@qibebt.ac.cn.
# 
##############################################################################################################################################################

help_message () {
        echo ""
        echo "Run on assembled contigs in fasta formart."
        echo "Usage: metaWRAP split_contigs -i contigs_fasta -o output_dir"
        echo "Options:"
        echo ""
        echo "  -i STR          input fasta file of assembled contigs"
        echo "  -o STR          output directory"
        echo "";}

comm () { ${SOFT}/print_comment.py "$1" "-"; }
error () { ${SOFT}/print_comment.py "$1" "*"; exit 1; }
warning () { ${SOFT}/print_comment.py "$1" "*"; }
announcement () { ${SOFT}/print_comment.py "$1" "#"; }


########################################################################################################
########################               LOADING IN THE PARAMETERS                ########################
########################################################################################################


# setting scripts and databases from config file (should be in same folder as main script)
config_file=$(which config-metawrap)
source $config_file

# Set defaults
in="false";out="false";


# load in params
OPTS=`getopt -o hi:o: --long help -- "$@"`
# make sure the params are entered correctly
if [ $? -ne 0 ]; then help_message; exit 1; fi

# loop through input params
while true; do
        case "$1" in
                -i) in=$2; shift 2;;
                -o) out=$2; shift 2;;
                -h | --help) help_message; exit 1; shift 1;;
                --) help_message; exit 1; shift; break ;;
                *) break;;
        esac
done

########################################################################################################
########################           MAKING SURE EVERYTHING IS SET UP             ########################
########################################################################################################
# check if all parameters are entered
if [ "$in" = "false" ] ; then 
        help_message; exit 1
fi

if [ "$out" = "false" ] ; then
        help_message; exit 1
fi

########################################################################################################
########################                    BEGIN PIPELINE!                     ########################
########################################################################################################
announcement "RUNNING EukRep ON ALL CONTIGS"

# setting up the output folder
if [ ! -d $out ]; then 
        mkdir $out;
else 
        echo "Warning: $out already exists."
fi

comm "Now processing $in"

EukRep -i $in -o ${out}/final_assembly_euk.fasta --min 1000 --prokarya ${out}/final_assembly_pro.fasta

# check if any files were processed
if [[ $( ls $out | grep ".fasta" | wc -l ) -eq 0 ]]; then 
        comm "Error: No fasta files generated!"
        help_message; exit 1
fi

########################################################################################################
########################       FINISHED RUNNING split_contigs PIPELINE!!!       ########################
########################################################################################################
announcement "FINISHED RUNNING split_contigs PIPELINE!!!"

