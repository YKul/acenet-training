#!/bin/bash
#SBATCH --time=01
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=256M

module load python/3.11
virtualenv --no-download $SLURMTMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index asteval

python YKulish.py
