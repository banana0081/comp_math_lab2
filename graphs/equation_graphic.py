import matplotlib.pyplot as plt
import numpy as np


def eq(equation, root, start, end):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(which='major', color='white', linewidth=1)

    x = np.arange(start - 2, end + 2, 0.01)

    plt.plot([i for i in x], [equation(i) for i in x])

    plt.plot(root, equation(root), marker='o', markerfacecolor="red")

    ax.grid(which='major', color='#bbb', linewidth=0.8)
    ax.minorticks_on()

    return fig

def sys(equation1, equation2, root1, root2):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    delta = 0.01
    xrange = np.arange(root1 - 2, root1 + 2, delta)
    yrange = np.arange(root2 - 2, root2 + 2, delta)
    X, Y = np.meshgrid(xrange, yrange)

    F = equation1(X, Y)
    G = equation2(X, Y)

    plt.contour(X, Y, F, [0], colors=['blue'])
    plt.contour(X, Y, G, [0], colors=['red'])

    ax.grid(which='major', color='#bbb', linewidth=0.8)
    ax.minorticks_on()

    return fig
