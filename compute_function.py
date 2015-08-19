import numpy as np
from math import log, exp
from downhill import downhill

if __name__ == '__main__':
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

    print(downhill(
        loglike,
        np.array([0]*59),
    ))
