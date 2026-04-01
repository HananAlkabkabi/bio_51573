#!/usr/bin/env python3

job_name = "blast"
walltime = "1:00:00"

print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={job_name}")
print(f"#SBATCH --partition comp01")
print(f"#SBATCH --nodes=1")
print(f"#SBATCH --qos comp")
print(f"#SBATCH --cpus-per-task=32")
print(f"#SBATCH --time={walltime}:00:00")
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