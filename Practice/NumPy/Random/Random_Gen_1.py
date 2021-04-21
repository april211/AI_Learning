from numpy.random import default_rng            # Call default_rng to get a new instance of a Generator


rng = default_rng()
vals = rng.standard_normal(5)
more_vals = rng.standard_normal(5)

print(vals)
print(more_vals)

"""
Distributions
beta(a, b[, size])
Draw samples from a Beta distribution.

binomial(n, p[, size])
Draw samples from a binomial distribution.

chisquare(df[, size])
Draw samples from a chi-square distribution.

dirichlet(alpha[, size])
Draw samples from the Dirichlet distribution.

exponential([scale, size])
Draw samples from an exponential distribution.

f(dfnum, dfden[, size])
Draw samples from an F distribution.

gamma(shape[, scale, size])
Draw samples from a Gamma distribution.

geometric(p[, size])
Draw samples from the geometric distribution.

gumbel([loc, scale, size])
Draw samples from a Gumbel distribution.

hypergeometric(ngood, nbad, nsample[, size])
Draw samples from a Hypergeometric distribution.

laplace([loc, scale, size])
Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay).

logistic([loc, scale, size])
Draw samples from a logistic distribution.

lognormal([mean, sigma, size])
Draw samples from a log-normal distribution.

logseries(p[, size])
Draw samples from a logarithmic series distribution.

multinomial(n, pvals[, size])
Draw samples from a multinomial distribution.

multivariate_normal(mean, cov[, size, …])
Draw random samples from a multivariate normal distribution.

negative_binomial(n, p[, size])
Draw samples from a negative binomial distribution.

noncentral_chisquare(df, nonc[, size])
Draw samples from a noncentral chi-square distribution.

noncentral_f(dfnum, dfden, nonc[, size])
Draw samples from the noncentral F distribution.

normal([loc, scale, size])
Draw random samples from a normal (Gaussian) distribution.

pareto(a[, size])
Draw samples from a Pareto II or Lomax distribution with specified shape.

poisson([lam, size])
Draw samples from a Poisson distribution.

power(a[, size])
Draws samples in [0, 1] from a power distribution with positive exponent a - 1.

rayleigh([scale, size])
Draw samples from a Rayleigh distribution.

standard_cauchy([size])
Draw samples from a standard Cauchy distribution with mode = 0.

standard_exponential([size])
Draw samples from the standard exponential distribution.

standard_gamma(shape[, size])
Draw samples from a standard Gamma distribution.

standard_normal([size])
Draw samples from a standard Normal distribution (mean=0, stdev=1).

standard_t(df[, size])
Draw samples from a standard Student’s t distribution with df degrees of freedom.

triangular(left, mode, right[, size])
Draw samples from the triangular distribution over the interval [left, right].

uniform([low, high, size])
Draw samples from a uniform distribution.

vonmises(mu, kappa[, size])
Draw samples from a von Mises distribution.

wald(mean, scale[, size])
Draw samples from a Wald, or inverse Gaussian, distribution.

weibull(a[, size])
Draw samples from a Weibull distribution.

zipf(a[, size])
Draw samples from a Zipf distribution.
"""

# https://numpy.org/doc/stable/reference/random/index.html#numpyrandom
# https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState
