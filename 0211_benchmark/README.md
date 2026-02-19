# Workflow

## 1) Geometry Optimization
Orca input:
<pre>
! BLYP D3 def2-SVP def2/J Opt

%pal nprocs 2 end

* xyzfile 0 1 molecule.xyz
</pre>

Starting geometries in xyz format can be found in the directory "*molecules*".

## 2) SCF
Orca input:
<pre>
! BLYP D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 1 opt.xyz
</pre>

Use the final geometry from the previous optimization as "*opt.xyz*" input.
The keyword in the *%output* section prints the composition of the converged MOs (molecular orbitals). Look at them carefully!

The MO energies (with opposite sign) from a converged Hartree-Fock are an estimate of the first ionization potential (in principle, this doesn't hold true for MOs from DFT!):
<pre>
----------------
ORBITAL ENERGIES
----------------

  NO   OCC          E(Eh)            E(eV) 
   0   2.0000     -26.352872      -717.0981 
   1   2.0000     -26.352617      -717.0912 
   2   2.0000     -26.350180      -717.0249 
   3   2.0000     -20.635536      -561.5215 
   4   2.0000     -20.584217      -560.1250 
   5   2.0000     -11.527357      -313.6753 
   6   2.0000     -11.419817      -310.7490 
   7   2.0000     -11.312195      -307.8205 
   8   2.0000     -11.239521      -305.8429 
   9   2.0000      -1.748800       -47.5873 
  10   2.0000      -1.651522       -44.9402 
  11   2.0000      -1.651129       -44.9295 
  12   2.0000      -1.504043       -40.9271 
</pre>
Core orbitals are atomic in nature, and their energies are very distant for different elements. Here, MOs from 5 to 8 are C 1s orbitals.

Toward the end of the output file, you find the final total electronic energy (units are Hartree):
<pre>

-------------------------   --------------------
FINAL SINGLE POINT ENERGY      -591.688633763406
-------------------------   --------------------

</pre>

## 3) Z+1 Δ-SCF
Orca input:
<pre>
! BLYP D3 def2-TZVP def2/J

%pal nprocs 2 end

%output Print[P_ReducedOrbPopMO_L] 1 end

* xyzfile 0 2 opt_modified.xyz
</pre>

The "*opt_modified.xyz*" file is a modified version of the previous "*opt.xyz*" where an atomic label is properly changed from the *Z* chemical element to the *Z+1* element. Atomic coordinates are left unchanged, as in this example:
<pre>
# ORIGINAL COORDINATES

C     -2.779600    1.351898   -0.000099
C     -1.463458    1.315906    0.000408
H     -3.371149    0.626498    0.534444
H     -3.329769    2.109340   -0.534361
H     -0.913299    0.558130    0.534206
H     -0.871919    2.040972   -0.534598

# Z+1 COORDINATES (C -> N)

N     -2.779600    1.351898   -0.000099
C     -1.463458    1.315906    0.000408
H     -3.371149    0.626498    0.534444
H     -3.329769    2.109340   -0.534361
H     -0.913299    0.558130    0.534206
H     -0.871919    2.040972   -0.534598
</pre>
Please, look at the charge and multiplicity values: if in the "base" calculation we had "**xyzfile 0 1*", with an extra-electron in the Z+1 calculation we will have "**xyzfile 0 2*"

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

The "*scf_converged.gbw*" should be a copy of the *.gbw* produced by the previous SCF calculation.

The *IonizeAlpha* is the number of the orbital which will be ionized. In order to choose this value, look at the orbitals composition printed in the output of the original (non ionized!) SCF calculation:
<pre>
------------------------------------------
LOEWDIN REDUCED ORBITAL POPULATIONS PER MO
-------------------------------------------
THRESHOLD FOR PRINTING IS 0.1%%
                      0         1         2         3         4         5   
                 -26.35287 -26.35262 -26.35018 -20.63554 -20.58422 -11.52736
                   2.00000   2.00000   2.00000   2.00000   2.00000   2.00000
                  --------  --------  --------  --------  --------  --------
 7 O  s               0.0       0.0       0.0      99.6       0.0       0.0
 8 C  dx2y2           0.0       0.0       0.0       0.0       0.1       0.0
 8 C  dxy             0.0       0.0       0.0       0.1       0.0       0.1
 9 O  s               0.0       0.0       0.0       0.0      99.5       0.0
10 C  s               0.0       0.0       0.0       0.0       0.0      98.5
11 F  s               0.1      99.7       0.0       0.0       0.0       0.0
11 F  dyz             0.0       0.0       0.0       0.0       0.0       0.2
12 F  s               0.0       0.0      99.8       0.0       0.0       0.0
12 F  dxy             0.0       0.0       0.0       0.0       0.0       0.2
13 F  s              99.7       0.1       0.0       0.0       0.0       0.0
13 F  pz              0.0       0.0       0.0       0.0       0.0       0.1
13 F  dz2             0.0       0.0       0.0       0.0       0.0       0.1
13 F  dyz             0.0       0.0       0.0       0.0       0.0       0.1
</pre>
Core orbitals typically exhibit a ~99% composition from a single orbital of a single atom.

It is important to check that the SCF finally converged to the expected ionized state. A fast way to understand what happened to the electrons is to look at population analysis:
<pre>
--------------------------------------------
MULLIKEN ATOMIC CHARGES AND SPIN POPULATIONS
--------------------------------------------
   0 C :   -0.734821    0.000755
   1 H :    0.227135    0.001353
   2 H :    0.201763    0.000201
   3 H :    0.202923   -0.001607
   4 C :    0.096177    0.010767
   5 H :    0.240978    0.000538
   6 H :    0.243608    0.001327
   7 O :   -0.290966    0.004515
   8 C :    0.421200    0.029832
   9 O :   -0.395920   -0.028231
  10 C :    1.287563   -1.210120
  11 F :   -0.165779    0.066212
  12 F :   -0.164006    0.057346
  13 F :   -0.169854    0.067112
</pre>
The +1.28 charge and -1.21 spin (an Alpha-spin electron has been removed) inidicate that the hole state is mainly localized on C 10.

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

The keyword *NRoots* specifies the number of calculated ionized states (e.g. 4 if the molecule has 4 C atoms). The two values in *CVSOrb* limit the orbitals window for core-valence separation: setting this to *5,8* means that we restrain the orbitals window from MO 5 to MO 8 (again: look at the orbitals composition!). *CoreHole* is the 1st state from which roots are counted: in this case, the lowest C 1s orbital is 5, and we are not interested in core orbitals from other elements. Others keywords should not be modified. The roots of the CC problem are printed in the output: they represent the ionization potential from the corresponding orbital:
<pre>
----------------------
EOM-CCSD RESULTS (RHS)
----------------------

IROOT=  1: 11.071691 au   301.276 eV 2429955.4 cm**-1
  Amplitude    Excitation
   0.675020     5 -> x
Percentage singles character=    101.13

IROOT=  2: 10.978268 au   298.734 eV 2409451.4 cm**-1
  Amplitude    Excitation
  -0.676977     6 -> x
Percentage singles character=    101.04

IROOT=  3: 10.848096 au   295.192 eV 2380881.8 cm**-1
  Amplitude    Excitation
  -0.674671     7 -> x
Percentage singles character=    101.14

IROOT=  4: 10.777477 au   293.270 eV 2365382.7 cm**-1
  Amplitude    Excitation
  -0.675095     8 -> x
Percentage singles character=    101.15  
</pre>
The *IP-EOM-DLPNO-CCSD* approximation can be substituted with *bt-PNO-IP-EOM-CCSD* for more accurate results, but the calculation may be much slower! Using basis sets smaller than a TZ is definitely not recommendable.
