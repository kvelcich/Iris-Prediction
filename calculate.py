import numpy;
import math

# Calculates the value for Mu
def mu(matrix):
    M = matrix.shape[1]
    N = matrix.shape[0] - 10

    mu = numpy.zeros(shape=(M, 1))
    for idx in range(N):
        mu += matrix[[idx], :].T
    mu /= N

    return mu

# Calculates the value for Sigma
def sigma(matrix, mu):
    P = matrix.shape[1]
    N = matrix.shape[0] - 10

    matrix = matrix[0:40, :]
    cov = numpy.zeros(shape=(P, P))
    for i in matrix:
        cov += (i - mu.T).T * (i - mu.T)
    cov /= N

    return cov

# Calculates the Multivariate Normal PDF
def pdf(x, mu, sigma):
    P = x.shape[0]

    prob = 1 / math.sqrt(((2 * math.pi) ** P) * numpy.linalg.det(sigma))
    ins = numpy.dot(numpy.dot((x - mu).T, numpy.linalg.inv(sigma)), x - mu)
    exp = math.exp(-0.5 * ins)

    return prob * exp

# Converts covariance to be independent
def cov_indep(sigma):
    M = sigma.shape[0]

    cov =  numpy.zeros(shape=(M, M))
    for i in range(M):
        cov[i, i] = sigma[i, i]

    return cov
