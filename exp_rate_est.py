# Estimation of the rate k in the exponential probability density k*exp(-k*t)
#
# Input: 
#   - time: array of measured times
#
# Output:
#   - k-estimate (via scale-parameter estimation)
#   - Error (mean logarithmic error criterion)
# 
# Assumptions (within the Bayesian framework):
#   - Jeffreys's prior for scale parameters over an arbitrarily large positive interval
#   - Error constructed via the mean logarithmic error
#
#   See details in:
#       J. Rubio, Quantum Scale Estimation, arXiv:2111.11921 (2021)
#       J. Rubio et al., Global Quantum Thermometry, Phys. Rev. Lett. 127, 190402 (2021) - arXiv:2011.13018
#
# Dr Jesús Rubio
# University of Exeter
# J.Rubio-Jimenez@exeter.ac.uk
#
# Created: January 2022
# Last update: --

import numpy as np
from scipy import special

def expratest(time):
    
    # Number of data points
    mu = len(time)

    # Estimate and its associated error
    estimate = np.exp(special.polygamma(0, mu)) / (mu * np.mean(time))
    error = estimate * np.sqrt(special.polygamma(1, mu))

    print("The rate estimate and its associated error are:")
    return estimate, error
