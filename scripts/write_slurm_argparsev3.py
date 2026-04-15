#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser(description="Generate a Slurm script to run a BLAST job on HPC")

# add a positional argument, in this case, the position in the Slurm is time
parser.add_argument("walltime", help="Walltime for the Slurm job", type=int)

# add a poptional argument, job_name
parser.add_argument("-j", "--job_name", help="Name of the Slurm job")

# parse the arguments
args = parser.parse_args()

print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={args.job_name}")
print(f"#SBATCH --partition comp01")
print(f"#SBATCH --nodes=1")
print(f"#SBATCH --qos comp")
print(f"#SBATCH --cpus-per-task=32")
print(f"#SBATCH --time={args.walltime}:00:00")
print(f"#SBATCH --output=%x.%j.out")
print(f"#SBATCH --error=%x.%j.err")
print(f"#SBATCH --mail-type=ALL")
print(f"#SBATCH --mail-user=hanana@uark.edu")

print()
print(f"export OMP_NUM_THREADS=32")

print()
print(f"module purge")
print(f"module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")

print()
print(f"cd $SLURM_SUBMIT_DIR")

#print("module load blast")

print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")