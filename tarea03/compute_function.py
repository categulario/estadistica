import numpy as np
from modules.downhill import downhill
from modules.bacteria import bacteria
from gmpy2 import log, exp
from random import random

if __name__ == '__main__':
    print("will compute the loglike function")
    x_data = []
    y_data = []

    with open('filtered.data', 'r') as datafile:
        for line in datafile:
            data = list(map(float, line.strip().split(',')))

            y_data.append(bool(data[-1]))
            x_data.append(np.array([1] + data[:-1]))

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

    print('Done computing loglike function')

    loglike = makeloglike(x_data, y_data)

    # downhill method is a method for minimizing, but we need to maximize, so
    # here we propose another function to minimize that maximize the original
    # function

    start_position  = np.array([random()*2-1 for i in range(58)])

    print(bacteria(
        loglike,
        start_position,
    ))
