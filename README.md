# Computational XPS project on C3SE Vera
Core-ionization calculations will be performed with Orca 6.0.1 on the [Vera cluster](https://www.c3se.chalmers.se/about/Vera/) hosted at C3SE.

Remote login through desktop interface is available at Open OnDemand: (https://www.c3se.chalmers.se/documentation/connecting/ondemand/)

To remotely login through a ssh client:
<pre>
 ssh <_username_>@vera1.c3se.chalmers.se
</pre>

The environment for executing Orca is set up trough:
<pre>
 module load ORCA/6.0.1-gompi-2023b 
</pre>

To submit job scripts to the SLURM queuing system:
<pre>
  sbatch <_script_name_>
</pre>

Example of SLURM submission script (parallel MPI execution over 4 processors):
<pre>
#!/bin/bash
#SBATCH -A KBTX16VT2603
#SBATCH -p cpu
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -J orca_job
#SBATCH -t 01:00:00
#SBATCH --mem-per-cpu=1000
#SBATCH -o slurm-%x-%j.out
#SBATCH -e slurm-%x-%j.err

module purge
module load ORCA/6.0.1-gompi-2023b

exe=$( which orca )

srun $exe my_calculation.inp > my_calculation.out
</pre>
