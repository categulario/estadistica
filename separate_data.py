from random import random

def filterlines(filename, portion=.5):
    """get randomly chosen portion lines of filename"""
    with open(filename, 'r') as spamdata:
        for line in spamdata:
            if random() < portion:
                yield line

if __name__ == '__main__':
    contador = 0

    with open('filtered.data', 'w') as filtereddata:
        filtereddata.writelines(filterlines('spambase.data', portion=1/3))
