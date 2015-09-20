from math import sqrt

def sub_sqrt(a, b):
    return (a - b)**2

def euclidean(x, y):
    return sqrt(sum(map(sub_sqrt, x, y)))

if __name__ == '__main__':
    assert euclidean((0, 1), (0, 0)) == 1
    assert euclidean((0, 0), (1, 1)) == sqrt(2)
