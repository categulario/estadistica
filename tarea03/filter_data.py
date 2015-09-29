"""
Select a randomly chosen third part of the base data.
"""
from random import random

def filterlines(datafile, portion=.5):
    """get randomly chosen portion lines of datafile"""
    with open(datafile, 'r') as spamdata:
        for line in spamdata:
            if random() < portion:
                yield line

if __name__ == '__main__':
    contador = 0

    with open('filtered.data', 'w') as filtereddata:
        filtereddata.writelines(filterlines(
            'original/spambase.data',
            portion=1/3
        ))
