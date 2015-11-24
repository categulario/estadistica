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

    start_position  = np.array([
 -415.13706028, -152.15349808, -181.37182028,  213.73064215, -480.21752158,
 -116.11664233,  130.54036518, -715.76024621, -518.37865949,   87.99690483,
 -202.29212272, -496.08981483,  133.90909097,  140.48507997, -345.03532793,
  -28.08525562,  460.60559221,  600.97004537,  117.79596141,  460.63317922,
  -49.79520073,  134.66670158, -545.78892386, -662.40181546,  -40.59083835,
 -724.33573462, -150.96701151,  260.02208168, -107.0426301,   -84.51987622,
  169.89099796,  331.26404442,  539.2255355,   333.21013874,  326.48829431,
  425.59668043, -382.01179524, -247.30256622,  -57.30219139,  561.417539,
  421.5380726,  -282.06129456,  -13.86115061,  549.51752798,  296.00434855,
 -498.49141151,  119.66687203, -173.43813235,    3.40013412, -339.36465881,
  -58.55844672, -252.89898841,  397.87751323, -610.07940549, -163.69428162,
 -380.41579214,  276.00784445,   43.7352992, ])

    print(bacteria(
        loglike,
        start_position,
    ))
