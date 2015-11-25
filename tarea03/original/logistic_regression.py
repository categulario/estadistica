"""
Compute and minimize the loglike function given the data
"""
import numpy as np
import pandas as pd
from numpy import log, exp
from scipy.optimize import minimize

names = ('x', 'y', 'z', 'class')

def makeloglike(x_data, y_data):
    def loglike(ß):
        def term(x, y):
            dot = ß.dot(x)
            if y:
                return dot - log(1 + exp(dot))
            else:
                return -log(1 + exp(dot))
        return sum(
            map(term, x_data, y_data)
        )

    return loglike

def make_P(ß):
    def P(x):
        dot = ß.dot(x)
        return exp(dot)/(1 + exp(dot))
    return P

if __name__ == '__main__':
    x_data = []
    y_data = []

    data = pd.read_csv('train.csv', names=names)

    print('Done computing loglike function')

    loglike = makeloglike(
        np.array(data.loc[:,names[:-1]]),
        np.array(data.loc[:,names[-1]]),
    )

    x0 = np.zeros(3)

    res = minimize(lambda x: 1/(1 + loglike(x)), x0)

    if res.success:
        print('function evaluated %d times'%res.nfev)
        ß = res.x

        P = make_P(ß)

        # test this function
        testdata = np.loadtxt("reduced.csv", delimiter=",")

        success = 0
        total = 0

        for x in testdata:
            if np.round(P(x[:-1])) == x[-1]: success += 1
            total += 1

        print(success/total * 100)
    else:
        print('optimization did not success')
        print(res.message)
