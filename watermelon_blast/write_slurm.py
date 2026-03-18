#!/usr/bin/env python3

job = "blast"
time = "1:00:00"
queue = "cloud72"
email = "hanana@uark.edu"

print("#!/bin/bash")
print(f"#SBATCH --job-name={job}")
print(f"#SBATCH --time={time}")
print(f"#SBATCH -p {queue}")
print("#SBATCH -q cloud")
print("#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print(f"#SBATCH --mail-user={email}")
print("#SBATCH --mail-type=END")

print("module load blast")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")
