import numpy;
from calculate import mu, sigma

setosa = numpy.zeros(shape=(4, 50))
versicolour = numpy.zeros(shape=(4, 50))
virginica = numpy.zeros(shape=(4, 50))

# Reading data from input
with open("iris.data") as data:
    i = 0
    for line in data:
        line = line.split(",")
        if len(line) == 5:
            if i < 50:
                setosa[0][i] = float(line[0])
                setosa[1][i] = float(line[1])
                setosa[2][i] = float(line[2])
                setosa[3][i] = float(line[3])
            elif i < 100:
                versicolour[0][i % 50] = float(line[0])
                versicolour[1][i % 50] = float(line[1])
                versicolour[2][i % 50] = float(line[2])
                versicolour[3][i % 50] = float(line[3])
            else:
                virginica[0][i % 50] = float(line[0])
                virginica[1][i % 50] = float(line[1])
                virginica[2][i % 50] = float(line[2])
                virginica[3][i % 50] = float(line[3])
            i += 1

# Calculating Mu
mu1 = mu(setosa)
mu2 = mu(versicolour)
mu3 = mu(virginica)

# Calculating Sigma
sigma1 = sigma(setosa, mu1)
sigma2 = sigma(versicolour, mu1)
sigma3 = sigma(virginica, mu1)

# Calculate Avg. Sigma
sigma = (sigma1 + sigma2 + sigma3) / 3
