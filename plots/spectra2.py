import sys
import numpy as np
import matplotlib.pyplot as plt

def lorentzian(x, x0, gamma, amplitude=1.0):
    """
    Lorentzian function.
    x0      : center position
    gamma   : half-width at half-maximum (HWHM)
    amplitude : peak height
    """
    return amplitude * (gamma**2) / ((x - x0)**2 + gamma**2)

# Parse arguments
if len(sys.argv) < 3:
    raise RuntimeError("Usage: python3 spectra.py -f <file> [ -s <shift> ]")
if sys.argv[1] == "-f":
    datafile = sys.argv[2]
else:
    raise RuntimeError("Usage: python3 spectra.py -f <file> [ -s <shift> ]")

# Read calculated peaks
calc_peaks = np.loadtxt(datafile, dtype=float, usecols=(1))

# Apply shift
zero_ref = np.min(calc_peaks)
calc_peaks = calc_peaks - zero_ref

# Set experimental peaks
exp_peaks = [7.46, 4.33, 1.72, 0.00]

# Set arbitrary FWHM
gamma = 0.5

# Set x-axis range
x = np.linspace(-2, 10, 2000)

# Plot
plt.figure(figsize=(8, 5))

for peak in exp_peaks:
    y = lorentzian(x, peak, gamma)
    plt.plot(x, y)

for peak in calc_peaks:
    plt.bar(peak, 0.5, width=0.5)


plt.gca().invert_xaxis()
plt.xlabel("x")
plt.ylabel("Intensity")
plt.tight_layout()
plt.show()

