#!/usr/bin/env python3
# Calcula la normal a la playa
import matplotlib.pyplot as plt
import numpy as np

data  = []

def onpick(event):
    global data

    x = event.xdata
    y = event.ydata

    if event.button == 3:
        data = np.array(data)
        np.savetxt("data.csv", data, delimiter=",", fmt=('%f', '%f'))
        exit()

    if x != None and y != None:
        data.append([x, y])

        plt.plot(x, y, 'ro')
        plt.draw()

if __name__ == '__main__':
    fig, ax = plt.subplots()

    cid = fig.canvas.mpl_connect('button_press_event', onpick)

    plt.axis([-5, 5, -5, 5])

    plt.title("Escoge puntos para tus datos")
    plt.xlabel("Click derecho cuando termines ;)")

    plt.show()
