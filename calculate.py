import numpy;

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
        sigma += (matrix[:, [idx]] - mu) * (matrix[:, [idx]] - mu).T
    sigma /= N

    return sigma
