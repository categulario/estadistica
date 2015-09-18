from metrics import euclidean
from math import exp
from random import random, gauss
from matplotlib import pyplot as plt
from functools import partial

def k_nearest(data, x, metric=euclidean, k=11):
    """
    Take X and return the mos probable class given by its nearest neighbours

    data is an array of 2-tuples, the first value being a tuple of coordinates
    and the second one, the class it belogs
    """
    distances = []
    for dat in data:
        distances.append((metric(dat[0], x), dat[1]))

    distances.sort(key=lambda x: x[0])

    # lets see which is the most common
    classes = {}
    for item in distances[:k]:
        if item[1] in classes:
            classes[item[1]] += 1
        else:
            classes[item[1]] = 1

    classes = list(classes.items())

    classes.sort(key=lambda x: x[1])

    return classes[-1][0]

def random_point(mean=0, variance=1):
    x = random()*6 - 3
    return exp(-x**2/2)

def make_points(num, mean=0, variance=1):
    return [gauss(mean, variance) for i in range(num)]


if __name__ == '__main__':
    num = 200

    x_blue = make_points(num)
    y_blue = make_points(num)

    x_red = make_points(num, mean=2)
    y_red = make_points(num, mean=2)

    fig, ax = plt.subplots()
    ax.set_title('Click sobre la gráfica para clasificar')

    def make_class(item, category='Azul'):
        return tuple(item), category

    make_class_b = partial(make_class, category='Verde')

    joined_data = list(map(make_class, zip(x_blue, y_blue)))
    joined_data += list(map(make_class_b, zip(x_red, y_red)))

    def onpick(event):
        point = event.xdata, event.ydata

        print(k_nearest(joined_data, point))

    ax.plot(x_blue, y_blue, 'o', x_red, y_red, 'o')
    fig.canvas.mpl_connect('button_press_event', onpick)

    plt.show()
