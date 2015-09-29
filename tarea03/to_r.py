if __name__ == '__main__':
    with open('filtered.data') as filteredfile,\
        open('predictor.data', 'w') as predictorfile,\
        open('observed.data', 'w') as observedfile:

        predictorlines = []
        observedlines = []

        for line in filteredfile:
            y, x = line.strip().split(' ')
            predictorlines.append(' '.join(x.split(','))+'\n')
            observedlines.append(y+'\n')

        predictorfile.writelines(predictorlines)
        observedfile.writelines(observedlines)
