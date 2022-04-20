import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog


C2 = [[5, 9],
      [8, 3]]

C3 = np.array([[5, 8, 6, 4, 7],
               [3, 2, 4, 8, 9]])

C4 = np.array([[-4, 2],
               [5, 7],
               [2, -8],
               [-1, 4],
               [6, -3]])

C5 = np.array([[2, 6, 4, 5],
               [7, 2, 3, 1],
               [5, 3, 6, 2]])


def line_intersection(line1, line2, bounds=[0, 1]):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if x <= bounds[0] or x >= bounds[1]:
        return None
    return x, y


def plot_C2():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 9)
    ax.plot([0, 1], [C2[0][0], C2[1][0]])
    ax.plot([0, 1], [C2[0][1], C2[1][1]])

    V_graph = line_intersection(
        [(0, C2[0][0]), (1, C2[1][0])],
        [(0, C2[0][1]), (1, C2[1][1])])
    ax.plot([V_graph[0], V_graph[0]], [0, V_graph[1]], linewidth=3)

    plt.savefig('C2.png')


def plot_C3():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 9)
    for x in C3.T:
        ax.plot([0, 1], [x[0], x[1]])

    def find_line(C3):
        def f(current_line, border=0):
            a = []
            for i, x in enumerate(C3.T):
                a.append({'line': x, 'point_intersection': line_intersection(
                    [(0, current_line[0]), (1, current_line[1])],
                    [(0, x[0]), (1, x[1])],
                    [border, 1]
                )})
            a = list(filter(lambda x: x['point_intersection'] is not None, a))
            b = list(filter(lambda x: x['point_intersection'][0] == min(
                map(lambda x: x['point_intersection'][0], a)), a))
            if b:
                b = b[0]
            else:
                return None, None
            second_line = b['line']
            X.append(b['point_intersection'][0])
            Y.append(b['point_intersection'][1])
            return second_line, b['point_intersection'][0]

        start_value = min(C3[0])
        start_index = np.where(C3[0] == start_value)[0][0]
        initial_line = C3[:, start_index]
        X = [0]
        Y = [initial_line[0]]

        prev_line = initial_line
        next_line, border = f(initial_line)
        while next_line is not None:
            prev_line = next_line
            next_line, border = f(next_line, border)

        X.append(1)
        Y.append(prev_line[1])
        ax.plot(X, Y, linewidth=5)
        return X, Y

    a = find_line(C3)
    V_graph = list(filter(lambda x: x[1] == max(a[1]), zip(*a)))[0]
    ax.plot([V_graph[0], V_graph[0]], [ax.get_ylim()[0], V_graph[1]], linewidth=3)

    plt.savefig('C3.png')


def plot_C4():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(-8, 7)
    for x in C4:
        ax.plot([0, 1], [x[0], x[1]])

    def find_line(C4):
        def f(current_line, border=0):
            a = []
            for x in C4:
                a.append({'line': x, 'point_intersection': line_intersection(
                    [(0, current_line[0]), (1, current_line[1])],
                    [(0, x[0]), (1, x[1])],
                    [border, 1]
                )})
            a = list(filter(lambda x: x['point_intersection'] is not None, a))
            b = list(filter(lambda x: x['point_intersection'][0] == min(
                map(lambda x: x['point_intersection'][0], a)), a))
            if b:
                b = b[0]
            else:
                return None, None
            second_line = b['line']
            X.append(b['point_intersection'][0])
            Y.append(b['point_intersection'][1])
            return second_line, b['point_intersection'][0]

        start_value = max(C4[:, 0])
        start_index = np.where(C4[:, 0] == start_value)[0][0]
        initial_line = C4[start_index, :]
        X = [0]
        Y = [initial_line[0]]

        prev_line = initial_line
        next_line, border = f(initial_line)
        while next_line is not None:
            prev_line = next_line
            next_line, border = f(next_line, border)

        X.append(1)
        Y.append(prev_line[1])
        ax.plot(X, Y, linewidth=5)
        return X, Y

    a = find_line(C4)
    V_graph = list(filter(lambda x: x[1] == min(a[1]), zip(*a)))[0]
    ax.plot([V_graph[0], V_graph[0]], [ax.get_ylim()[0], V_graph[1]], linewidth=3)

    plt.savefig('C4.png')


def plot_C5():
    c = [1, 1, 1, 1]
    A_ub = -C5
    b_ub = [-1, -1, -1]
    res = linprog(c=c, A_ub=A_ub, b_ub=b_ub, method='simplex')

    print('V =', 1/res.fun)
    print('p = ', res.x/res.fun)


if __name__ == '__main__':
    # plot_C2()
    # plot_C3()
    # plot_C4()
    plot_C5()
