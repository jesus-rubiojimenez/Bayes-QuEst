import numpy as np

def ncklog(n, k):   
    
    # Dr Jesús Rubio
    # University of Exeter
    # J.Rubio-Jimenez@exeter.ac.uk
    #
    # Created: January 2022
    # Modified: June 2023
    #
    # Given the integers n and k, with k in [n, 0),
    #
    #   ncklog(n,k)
    #
    # returns the natural logarithm of the binomial coefficient c(n, k), i.e., log[c(n, k)].
    #
    # Originally coded in MATLAB for
    #
    #   J. Rubio et al., Phys. Rev. Lett. 127, 190402 (2021) - arXiv:2011.13018
    #   https://github.com/jesus-rubiojimenez/QuThermometry-global
    
    coefficient = 0
    for x in range(k + 1, n + 1):
        coefficient += np.log(x) - np.log(x - k)

    return coefficient
