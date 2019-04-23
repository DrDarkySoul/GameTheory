import numpy as np

# C = np.array([
#     [5.,  8., 7.,  5., 4.],
#     [1., 10., 5.,  5., 6.],
#     [2.,  4., 3.,  6., 2.],
#     [3.,  5., 4., 12., 3.]
# ])

# Example

C = np.array([
    [5.,  8., 7.,  5., 4.],
    [1., 10., 5.,  5., 6.],
    [2.,  4., 3.,  6., 2.],
    [3.,  5., 4., 12., 3.]
])


def max_min(array):
    x = array.shape[0]
    y = array.shape[1]
    row_min = [np.amax(array)] * x
    for i in range(0, x):
        for j in range(0, y):
            row_min[i] = min(row_min[i], array[i][j])
    win = max(row_min)
    return [row_min.index(win) + 1, win]


def max_max(array):
    win = np.amax(array)
    return [np.where(array == win)[0][0] + 1, win]


def math_expectation(array):
    x = array.shape[0]
    y = array.shape[1]
    row_exp = [np.amin(array)] * x
    for i in range(0, x):
        row_exp = sum(array[i])/y
    win = max(row_exp)
    return [row_exp.index(win) + 1, win]


def bernulli_crit(array):
    print("Критерий Бернулли:")
    answer = math_expectation(array)
    print("Стратегия с индексом {0} с выигрышом {1}".format(answer[0], answer[1]))


def vald_crit(array):
    print("Критерий Вальда:")
    answer = max_min(array)
    print("Стратегия с индексом {0} с выигрышом {1}".format(answer[0], answer[1]))


def opt_crit(array):
    print("Критерий максимума:")
    answer = max_max(array)
    print("Стратегия с индексом {0} с выигрышом {1}".format(answer[0], answer[1]))


def gurvic_crit(array, a):
    print("Критерий Гурвица:")
    x = array.shape[0]
    row_crit = [np.amin(array)] * x
    for i in range(0, x):
        minimum = np.amin(array[i])
        maximum = np.amax(array[i])
        row_crit[i] = (a * minimum) + (1 - a) * maximum
    win = max(row_crit)
    print("Стратегия с индексом {0} и выйгрышом {1}".format(row_crit.index(win) + 1, win))


bernulli_crit(C)
vald_crit(C)
opt_crit(C)
gurvic_crit(C, 0.5)
