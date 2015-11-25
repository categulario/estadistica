#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
from names import names
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('spambase.data', names = names).sample(frac=1/3)

    # Remove last column (the class)
    classes = data.loc[:,names[-1]]
    data    = data.loc[:,names[:-1]]

    # Normalize data
    data -= data.mean()
    data /= data.std()

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
        p = 2

    # Compute the feature vector matrix (dim x p)
    feature = vectors[:,:p]

    # Finally compute new data multiplying feature vector matrix with
    # data matrix
    final = np.dot(feature.T, data.T).T

    # Add the class column
    reduced_data = np.append(final, classes.reshape((len(classes), 1)), axis=1)

    # Save the reduced-dimention data to a file
    formats = ('%f',)*p + ('%d',)
    np.savetxt("reduced.csv", reduced_data, delimiter=",", fmt=formats)

    # plot the new data
    df = pd.DataFrame(reduced_data, columns=('x', 'y', 'class'))
    spam = df[df['class'] == 1]
    nospam = df[df['class'] == 0]

    if p == 2:
        plt.plot(spam['x'], spam['y'], 'ro', label='spam')
        plt.plot(nospam['x'], nospam['y'], 'bo', label='nospam')

        plt.legend(loc='best')

        plt.show()
