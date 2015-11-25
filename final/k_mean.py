#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CLUSTERS = 3

def euclidean(p1, p2):
    return np.sqrt((p1['x']-p2['x'])**2 + (p1['y'] - p2['y'])**2)

def closest_cluster(row, centroids):
    closest  = 0
    distance = euclidean(row, centroids[0])

    for cluster in range(1, CLUSTERS):
        new_distance = euclidean(row, centroids[cluster])

        if new_distance < distance:
            closest  = cluster
            distance = new_distance

    return closest

def plot(data, iteration):
    for c in range(CLUSTERS):
        plt.plot(
            data[data['cluster'] == c]['x'],
            data[data['cluster'] == c]['y'],
            'o',
            label="cluster %d"%c
        )

    plt.legend()
    plt.title('Iteration %d'%iteration)
    plt.show()

if __name__ == '__main__':
    data = pd.read_csv('data.csv', names=('x', 'y'))

    # asign a random cluster to each observation
    data['cluster'] = np.random.randint(CLUSTERS, size=len(data['x']))

    plot(data, 0)

    times   = 0

    while True:
        changes = False
        # Compute each cluster's centroid
        centroids = {
            i: data[data['cluster'] == i].loc[:,['x', 'y']].mean()
            for i in range(CLUSTERS)
        }

        # Assign each observation the class of the closest centroid
        for i, row in data.iterrows():
            closest = closest_cluster(row, centroids)
            if closest != row['cluster']:
                data.loc[i, 'cluster'] = closest
                changes = True

        times += 1

        plot(data, times)

        if not changes:
            break

    print('clustering finished after %d iterations'%times)
