# Scale estimation: Poisson rates 
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
# See details in:
#       J. Boeyens et al., On the role of symmetry and geometry in global quantum sensing, arXiv:2502.14817 (2025)
#       J. Rubio, Quantum scale estimation, Quantum Sci. Technol. 8, 015009 (2023); arXiv:2111.11921 
#
# Dr Jesús Rubio
# University of Exeter
# J.Rubio-Jimenez@exeter.ac.uk
#
# Created: January 2022
# Last update: June 2025

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
