#!/usr/bin/env python3
import numpy as np
import pandas as pd
from names import names
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('spambase.data', names = names)

    # Remove last column (the class)
    data = data.loc[:,names[:-1]]

    # Normalize data
    data -= data.mean()
    data /= data.std()

    # Calculate covariance matrix
    cov = data.cov()

    # gives eigenvectors and eigenvalues, sorted ascending
    values, vectors = np.linalg.eigh(cov)

    # Sort ascending
    dim = len(values)
    for i in range(dim//2):
        j = dim - i - 1
        values[i], values[j] = values[j], values[i]

        aux = vectors[:,i].copy()
        vectors[:,i] = vectors[:,j]
        vectors[:,j] = aux

    plt.plot(values, 'o')
    plt.show()

    # Get dimention of final space
    p = int(input('¿Cuántos vectores quieres? '))
