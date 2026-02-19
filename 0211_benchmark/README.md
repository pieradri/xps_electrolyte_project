# Workflow

## 1) Geometry Optimization
Orca input:
<pre>
! BLYP D3 def2-SVP def2/J Opt

%pal nprocs 2 end

* xyzfile 0 1 molecule.xyz
</pre>

Starting geometries in xyz format can be found in the directory "*molecules*".

## 2) SCF (orbital energies)
Orca input:
<pre>
! BLYP D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

Use the final geometry from the previous optimization as "*opt.xyz*" input.
The keyword in the *%output* section prints the composition of the converged MOs. Look at them carefully!

## 3) Z+1 Δ-SCF
Orca input:
<pre>
! BLYP D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 2 opt_modified.xyz
</pre>

The "*opt_modified.xyz*" file is a modified version of the previous "*opt.xyz*" where an atomic label is properly changed from the *Z* chemical element to the *Z+1* element. Atomic coordinates are left unchanged. Please, look at the charge and multiplicity values: if in the "base" calculation we had "**xyzfile 0 1*", with an extra-electron in the Z+1 calculation we will have "**xyz 0 2*"

## 4) Core-ionization Δ-SCF
Orca input:
<pre>
! UKS BLYP D3 def2-TZVP def2/J DeltaSCF NoDIIS MORead

%pal nprocs 2 end

%moinp "scf_converged.gbw"

%scf
  IonizeAlpha 7
end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

The "*scf_converged.gbw*" should be a copy of the *.gbw* produced by the previous SCF calculation. In order to choose the *IonizeAlpha* value, look at the orbitals composition.

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
 CoreHole 5
 printlevel 3
 maxiter 500
end

* xyzfile 0 1 opt.xyz
</pre>

The keyword *NRoots* specifies the number of calculated ionized states. The two values in *CVSOrb* limit the orbitals window for core-valence separation. *CoreHole* is the 1st state from which roots are counted. The *IP-EOM-DLPNO-CCSD* approximation can be substituted with *bt-PNO-IP-EOM-CCSD* for more accurate results, but the calculation may be much slower!
