from calculate import probability

def LDA(setosa, versicolour, virginica, mu1, mu2, mu3, sigma):
    N = setosa.shape[1]

    training1 = 0
    training2 = 0
    training3 = 0
    test1 = 0
    test2 = 0
    test3 = 0

    for i in range(N):
        # Setosa training & test data
        if probability(setosa[:, [i]], mu1, sigma) < probability(setosa[:, [i]], mu2, sigma) or probability(setosa[:, [i]], mu1, sigma) < probability(setosa[:, [i]], mu3, sigma):
            if i < 40:
                training1 += 1
            else:
                test1 += 1

        # Versicolour training & test data
        if probability(versicolour[:, [i]], mu2, sigma) < probability(versicolour[:, [i]], mu1, sigma) or probability(versicolour[:, [i]], mu2, sigma) < probability(versicolour[:, [i]], mu3, sigma):
            if i < 40:
                training2 += 1
            else:
                test2 += 1

        # Virginica training & test data
        if probability(virginica[:, [i]], mu3, sigma) < probability(virginica[:, [i]], mu1, sigma) or probability(virginica[:, [i]], mu3, sigma) < probability(virginica[:, [i]], mu2, sigma):
            if i < 40:
                training3 += 1
            else:
                test3 += 1

    print "\n===== LDA =====\n"

    print "Setosa Predictions:"
    print "Training data: " + str(training1) + " out of 40, or " + str(training1 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test1) + " out of 10, or " + str(test1 / 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test1 + training1) + " out of 50, or " + str((test1 + training1) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Versicolour Predictions:"
    print "Training data: " + str(training2) + " out of 40, or " + str(training2 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test2) + " out of 10, or " + str(test2 / 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test2 + training2) + " out of 50, or " + str((test2 + training2) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Virginica Predictions:"
    print "Training data: " + str(training3) + " out of 40, or " + str(training3 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test3) + " out of 10, or " + str(test3/ 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test3 + training3) + " out of 50, or " + str((test3 + training3) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Overall Predictions:"
    print "Training data: " + str(training1 + training2 + training3) + " out of 120, or " + str( (training1 + training2 + training3) / 120.0  * 100) + "% classified incorrectly."
    print "Test data: " + str(test1 + test2 + test3) + " out of 30, or " + str((test1 + test2 + test3) / 30.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(training1 + training2 + training3 + test1 + test2 + test3) + " out of 150, or " + str((training1 + training2 + training3 + test1 + test2 + test3) / 150.0 * 100) + "% classified incorrectly.\n"

def QDA(setosa, versicolour, virginica, mu1, mu2, mu3, sigma1, sigma2, sigma3):
    N = setosa.shape[1]

    training1 = 0
    training2 = 0
    training3 = 0
    test1 = 0
    test2 = 0
    test3 = 0

    for i in range(N):
        # Setosa training & test data
        if probability(setosa[:, [i]], mu1, sigma1) < probability(setosa[:, [i]], mu2, sigma2) or probability(setosa[:, [i]], mu1, sigma1) < probability(setosa[:, [i]], mu3, sigma3):
            if i < 40:
                training1 += 1
            else:
                test1 += 1

        # Versicolour training & test data
        if probability(versicolour[:, [i]], mu2, sigma2) < probability(versicolour[:, [i]], mu1, sigma1) or probability(versicolour[:, [i]], mu2, sigma2) < probability(versicolour[:, [i]], mu3, sigma3):
            if i < 40:
                training2 += 1
            else:
                test2 += 1

        # Virginica training & test data
        if probability(virginica[:, [i]], mu3, sigma3) < probability(virginica[:, [i]], mu1, sigma1) or probability(virginica[:, [i]], mu3, sigma3) < probability(virginica[:, [i]], mu2, sigma2):
            if i < 40:
                training3 += 1
            else:
                test3 += 1

    print "\n===== QDA =====\n"

    print "Setosa Predictions:"
    print "Training data: " + str(training1) + " out of 40, or " + str(training1 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test1) + " out of 10, or " + str(test1 / 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test1 + training1) + " out of 50, or " + str((test1 + training1) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Versicolour Predictions:"
    print "Training data: " + str(training2) + " out of 40, or " + str(training2 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test2) + " out of 10, or " + str(test2 / 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test2 + training2) + " out of 50, or " + str((test2 + training2) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Virginica Predictions:"
    print "Training data: " + str(training3) + " out of 40, or " + str(training3 / 40.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test3) + " out of 10, or " + str(test3/ 10.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(test3 + training3) + " out of 50, or " + str((test3 + training3) / 50.0 * 100) + "% classified incorrectly.\n"

    print "Overall Predictions:"
    print "Training data: " + str(training1 + training2 + training3) + " out of 120, or " + str( (training1 + training2 + training3) / 120.0 * 100) + "% classified incorrectly."
    print "Test data: " + str(test1 + test2 + test3) + " out of 30, or " + str((test1 + test2 + test3) / 30.0 * 100) + "% classified incorrectly."
    print "TOTAL: " + str(training1 + training2 + training3 + test1 + test2 + test3) + " out of 150, or " + str((training1 + training2 + training3 + test1 + test2 + test3) / 150.0 * 100) + "% classified incorrectly.\n"
