function [estimate,error] = expRateEst(t)
%% Estimation of the rate in an exponential probability density: k*exp(-k*t)
%
% Input: 
%   - t: measured times
%
% Output:
%   - k-estimate (via scale-parameter estimation)
%   - Error (mean logarithmic error criterion)
% 
% Assumptions (within the Bayesian framework):
%   - Jeffreys's prior for scale parameters over an arbitrarily large positive interval
%   - Error constructed via the mean logarithmic error
%
%   See details in: J. Rubio et al., Global Quantum Thermometry, Phys. Rev. Lett. 127, 190402 (2021) - arXiv:2011.13018
%
% Dr Jesús Rubio
% University of Exeter
% J.Rubio-Jimenez@exeter.ac.uk
%
% Created: July 2021
% Last update: --

%% Preparing input as column vectors
if ~iscolumn(t)==1
    t=t';
end

%% Estimation

% Number of data points
mu=length(t);

% Estimate
estimate=exp(psi(mu))/(mu*mean(t));

% Error
error=estimate*sqrt(psi(1,mu));

end
