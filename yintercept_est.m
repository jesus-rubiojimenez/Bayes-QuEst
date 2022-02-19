function [estimate,error] = yinterceptEst(y)
%% Estimation of the y-axis intercept: y=n
%
% Input: y
%   -> Note that x is not needed for this (trivial) estimation problem. 
%
% Output:
%   - n-estimate (posterior mean)
%   - Error (square root of the mean square error)
% 
% Assumptions (within the Bayesian framework):
%   - Flat prior with support on the real line
%   - Information about errors restricted to that captured by independent Gaussian densities
%   - Mean square error criterion
%
% Dr Jesús Rubio
% University of Exeter
% J.Rubio-Jimenez@exeter.ac.uk
%
% Created: July 2021
% Last update: --

%% Preparing input as column vectors
if ~iscolumn(y)==1
    y=y';
end

%% Estimation of n in y=n

% Estimate
estimate=mean(y);

% Error
error=sqrt(var(y)/length(y));

end