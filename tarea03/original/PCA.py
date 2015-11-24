import numpy as np
import pandas as pd
from names import names

if __name__ == '__main__':
    data = pd.read_csv('spambase.data', names = names)

    # Normalize data
    for name in names:
        data[name] -= data[name].mean()

    # Calculate covariance matrix
    cov = data.cov()

    values, vectors = np.linalg.eig(cov)
