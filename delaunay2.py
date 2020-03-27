#!/usr/bin/env python
import itertools
import matplotlib.pyplot as plt
import numpy as np
import typing
from scipy.spatial import Delaunay


def dt(lhs: list, rhs: list) -> None:
    vertices = lhs + rhs
    tri = Delaunay(vertices)
    pairs = []  # [([x, y], [x, y]), ([x, y], [x, y]), ...]
    for simplex in tri.simplices:
        tmp = []
        for vertex in simplex:
            tmp.append(vertices[vertex])
        for pair in list(itertools.combinations(tmp, 2)):
            if ((pair[0] in lhs and pair[1] in rhs) or
                    (pair[0] in rhs and pair[1] in lhs)):
                pairs.append(pair)

    midpoints = []
    for pair in pairs:
        # midpoint segment formula
        midpoints.append([((pair[0][0] + pair[1][0])/2),
                          ((pair[0][1] + pair[1][1])/2)])
    midpoints.sort()
    midpoints = list(midpoints for midpoints,
                     _ in itertools.groupby(midpoints))

    for pair in pairs:
        plt.plot([x[0] for x in pair], [y[1] for y in pair], 'g-')
    plt.plot([x[0] for x in lhs], [y[1] for y in lhs], 'o-')
    plt.plot([x[0] for x in rhs], [y[1] for y in rhs], 'yo-')
    #plt.plot([x[0] for x in mp], [y[1] for y in mp], 'k+-')
    #for j, p in enumerate(points):
    #    plt.text(p[0]-0.03, p[1]+0.03, j, ha='right')
    #for j, s in enumerate(tri.simplices):
    #    p = np.asarray(points)[s].mean(axis=0)
    #    plt.text(p[0], p[1], '#%d' % j, ha='center')
    plt.show()


if __name__ == '__main__':
    points = np.load('track1.npy')
    #lhs = [[0.5, 1.5], [0.6, 1], [0.7, 1.6]]
    #rhs = [[0, 0.75], [0.3, 0.3], [0.7, 0.15], [0.9, 0.3], [1.1, 0.65]]
    dt(points[0], points[1])
    #dt([[0, 0], [0, 1.1]], [[1, 0], [1, 1]])
