import numpy;
from calculate import mu, sigma, cov_indep
from predict import LDA, QDA

from scipy.stats import multivariate_normal

setosa = numpy.zeros(shape=(50, 4))
versicolour = numpy.zeros(shape=(50, 4))
virginica = numpy.zeros(shape=(50, 4))

# Reading data from input
with open("iris.data") as data:
    i = 0
    for line in data:
        line = line.split(",")
        if len(line) == 5:
            if i < 50:
                setosa[i][0] = float(line[0])
                setosa[i][1] = float(line[1])
                setosa[i][2] = float(line[2])
                setosa[i][3] = float(line[3])
            elif i < 100:
                versicolour[i % 50][0] = float(line[0])
                versicolour[i % 50][1] = float(line[1])
                versicolour[i % 50][2] = float(line[2])
                versicolour[i % 50][3] = float(line[3])
            else:
                virginica[i % 50][0] = float(line[0])
                virginica[i % 50][1] = float(line[1])
                virginica[i % 50][2] = float(line[2])
                virginica[i % 50][3] = float(line[3])
            i += 1

# Reducing the variables of the data
setosa = setosa[:, [0,1,2,3]]
versicolour = versicolour[:, [0,1,2,3]]
virginica = virginica[:, [0,1,2,3]]

# Calculating Mu
mu1 = mu(setosa)
mu2 = mu(versicolour)
mu3 = mu(virginica)

# Calculating Sigma
sigma1 = sigma(setosa, mu1)
sigma2 = sigma(versicolour, mu2)
sigma3 = sigma(virginica, mu3)

# Independent features
#sigma1 = cov_indep(sigma1)
#sigma2 = cov_indep(sigma2)
#sigma3 = cov_indep(sigma3)

# Calculate Avg. Sigma
sigma = (sigma1 + sigma2 + sigma3) / 3

# Making Predictions
LDA(setosa, versicolour, virginica, mu1, mu2, mu3, sigma)
QDA(setosa, versicolour, virginica, mu1, mu2, mu3, sigma1, sigma2, sigma3)
