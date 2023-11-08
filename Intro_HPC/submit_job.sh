#!/bin/bash
#SBATCH --job-name=HPC_Intro
#SBATCH --nodes=1
#SBATCH -o runner.%J.out
#SBATCH --time=00:02:00
#SBATCH --ntasks-per-node=1
#SBATCH -A edu18
#SBATCH --partition=cpu
#SBATCH --reservation=eurocc-cpu


module load SciPy-bundle/2019.10-foss-2019b-Python-3.7.4

printf "\nCalculating pi for $1 iterations\n\n"

time python pi_1.py --n $1