# Workflow

## 1) Geometry Optimization
Orca input:
<pre>
! wB97x-D3 def2-SVP def2/J Opt

%pal nprocs 2 end

* xyzfile 0 1 molecule.xyz
</pre>

## 2) SCF (orbital energies)
Orca input:
<pre>
! wB97x-D3 def2-SVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

## 3) Z+1 Δ-SCF
Orca input:
<pre>
! wB97x-D3 def2-SVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

## 4) Core-ionization Δ-SCF
Orca input:
<pre>
! wB97x-D3 def2-SVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

