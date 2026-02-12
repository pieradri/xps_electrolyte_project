# Workflow

## 1) Geometry Optimization
Orca input:
<pre>
! B97 D3 def2-SVP def2/J Opt

%pal nprocs 2 end

* xyzfile 0 1 molecule.xyz
</pre>

Starting geometriies in xyz format can be found in the directory "*molecules*".

## 2) SCF (orbital energies)
Orca input:
<pre>
! B97 D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

## 3) Z+1 Δ-SCF
Orca input:
<pre>
! B97 D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile +1 1 opt_modified.xyz
</pre>

## 4) Core-ionization Δ-SCF
Orca input:
<pre>
! UKS B97 D3 def2-TZVP def2/J DeltaSCF NoDIIS MORead

%pal nprocs 2 end

%moinp "scf_converged.gbw"

%scf
  IonizeAlpha 7
end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

## 4) IP-EOM-CCSD
Orca input:
<pre>
! IP-EOM-DLPNO-CCSD cc-pVTZ cc-pVTZ/C ExtremeSCF TightPNO NoFrozenCore

%pal nprocs 8 end

%maxcore 4000

%output Print[P_ReducedOrbPopMO_L] 1 end

%mdci
 NRoots 4
 DTol 1e-7
 CVSOrb 5,8
 CVSEP true
 DoCVS true
 DoCore true
 corehole 5
 printlevel 3
 maxiter 500
end

* xyzfile 0 1 opt.xyz
</pre>
