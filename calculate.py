import numpy;
import math

# Calculates the value for Mu
def mu(matrix):
    N = matrix.shape[1] - 10

    mu = numpy.zeros(shape=(4, 1))
    for idx in range(N):
        mu += matrix[:, [idx]]
    mu /= N

    return mu

# Calculates the value for Sigma
def sigma(matrix, mu):
    M = matrix.shape[0]
    N = matrix.shape[1] - 10

    sigma = numpy.zeros(shape=(M, M))
    for idx in range(N):
        sigma += numpy.outer((matrix[:, [idx]] - mu), (matrix[:, [idx]] - mu).T)
    sigma /= N

    return sigma

def probability(x, mu, sigma):
    P = x.shape[0]

    prob = 1 / ( (2 * math.pi) ** (P / 2) * numpy.linalg.det(sigma) ** (0.5) )
    exp = math.exp(-0.5 * numpy.dot(numpy.dot((x - mu).T, numpy.linalg.inv(sigma)), x - mu))

    return prob * exp
