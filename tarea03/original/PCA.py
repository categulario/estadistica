#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
from names import names
import matplotlib.pyplot as plt

if __name__ == '__main__':
    alldata = pd.read_csv('spambase.data', names = names)

    data    = alldata.sample(frac=1/3)

    # Remove last column (the class)
    classes = data.loc[:,names[-1]]
    data    = data.loc[:,names[:-1]]

    alldata_classes = alldata.loc[:,names[-1]]
    alldata = alldata.loc[:,names[:-1]]

    # Normalize data
    data -= data.mean()
    data /= data.std()

    alldata -= alldata.mean()
    alldata /= alldata.std()

    # Calculate covariance matrix
    cov = data.cov()

    # gives eigenvectors and eigenvalues, sorted ascending
    values, vectors = np.linalg.eigh(cov)

    # Sort ascending (assume descending order)
    dim = len(values)
    for i in range(dim//2):
        j = dim - i - 1
        values[i], values[j] = values[j], values[i]

        aux = vectors[:,i].copy()
        vectors[:,i] = vectors[:,j]
        vectors[:,j] = aux

    # Get dimention of final space
    if '--ask' in sys.argv:
        plt.plot(values, 'o')
        plt.show()

        p = int(input('¿Cuántos vectores quieres? '))
    else:
        p = 3

    # Compute the feature vector matrix (dim x p)
    feature = vectors[:,:p]

    # Finally compute new data multiplying feature vector matrix with
    # data matrix
    final_train = np.dot(feature.T, data.T).T

    final_total = np.dot(feature.T, alldata.T).T

    # Add the class column
    reduced_train_data = np.append(final_train, classes.reshape((len(classes), 1)), axis=1)

    reduced_data = np.append(final_total, alldata_classes.reshape((len(alldata_classes), 1)), axis=1)

    # Save the reduced-dimention data to a file
    formats = ('%f',)*p + ('%d',)
    np.savetxt("train.csv", reduced_train_data, delimiter=",", fmt=formats)
    np.savetxt("reduced.csv", reduced_data, delimiter=",", fmt=formats)

    # plot the new data
    if p == 1:
        df = pd.DataFrame(reduced_train_data, columns=('x', 'class'))
        spam = df[df['class'] == 1]
        nospam = df[df['class'] == 0]

        plt.plot(spam['x'], np.zeros(len(spam['x'])), 'r^', label='spam')
        plt.plot(nospam['x'], np.zeros(len(nospam['x'])), 'bo', label='nospam')

        plt.legend(loc='best')
    elif p == 2:
        df = pd.DataFrame(reduced_train_data, columns=('x', 'y', 'class'))
        spam = df[df['class'] == 1]
        nospam = df[df['class'] == 0]

        plt.plot(spam['x'], spam['y'], 'ro', label='spam')
        plt.plot(nospam['x'], nospam['y'], 'bo', label='nospam')

        plt.legend(loc='best')
    elif p == 3:
        from mpl_toolkits.mplot3d import Axes3D

        df = pd.DataFrame(reduced_train_data, columns=('x', 'y', 'z', 'class'))
        spam = df[df['class'] == 1]
        nospam = df[df['class'] == 0]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(spam['x'], spam['y'], spam['z'], c = 'r', marker='o')
        ax.scatter(nospam['x'], nospam['y'], nospam['z'], c='b', marker='^')

    if p in (1, 2, 3):
        plt.show()
