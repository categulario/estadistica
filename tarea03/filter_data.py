from random import random

def filterlines(datafile, resultfile, portion=.5):
    """get randomly chosen portion lines of datafile"""
    with open(datafile, 'r') as spamdata, open(resultfile, 'r') as resultdata:
        for line in spamdata:
            if random() < portion:
                yield resultdata.readline().strip() + ' ' + line
            else:
                resultdata.readline()

if __name__ == '__main__':
    contador = 0

    with open('filtered.data', 'w') as filtereddata:
        filtereddata.writelines(filterlines(
            'spambase.data',
            'spambase.result',
            portion=1/3
        ))
