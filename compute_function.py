import numpy as np
from downhill import downhill
from gmpy2 import log, exp
from random import random

if __name__ == '__main__':
    print("will compute the loglike function")
    x_data = []
    y_data = []

    with open('filtered.data', 'r') as datafile:
        for line in datafile:
            y, x = line.strip().split(' ')

            y_data.append(bool(y))
            x_data.append(np.array([1] + list(map(float, x.split(',')))))

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

    loglike = makeloglike(x_data, y_data)

    # print(loglike(np.array(ß)))
    # print(loglike(np.array([0]*59)))

    # print(downhill(
    #     loglike,
    #     np.array([random()*10]*59),
    # ))
