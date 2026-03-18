#!/bin/bash
#SBATCH --job-name=blast
#SBATCH --time=1:00:00
#SBATCH -p cloud72
#SBATCH -q cloud
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-user=hanana@uark.edu
#SBATCH --mail-type=END
module load blast
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn
