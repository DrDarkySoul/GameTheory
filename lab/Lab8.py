import numpy as np

# C = np.array([
#     [5.,  8., 7.,  5., 4.],
#     [1., 10., 5.,  5., 6.],
#     [2.,  4., 3.,  6., 2.],
#     [3.,  5., 4., 12., 3.]
# ])

C = np.array([
    [5.,  8., 7.,  5., 4.],
    [1., 10., 5.,  5., 6.],
    [2.,  4., 3.,  6., 2.],
    [3.,  5., 4., 12., 3.]
])


def max_min(array):
    x = array.shape[0]
    y = array.shape[1]
    row_min = [1000.0] * x
    for i in range(0, x):
        for j in range(0, y):
            row_min[i] = min(row_min[i], array[i][j])
    return row_min.index(max(row_min)) + 1


def max_max(array):
    x = array.shape[0]
    y = array.shape[1]
    row_max = [-1000.0] * x
    for i in range(0, x):
        for j in range(0, y):
            row_max[i] = max(row_max[i], array[i][j])
    return row_max.index(max(row_max)) + 1


def vald_crit(array):
    print("Критерий Вальда:")
    print("Стратегия с индексом {0}".format(max_min(array)))


def opt_crit(array):
    print("Критерий максимума:")
    print("Стратегия с индексом {0}".format(max_max(array)))


def gurvic_crit(array, a):
    print("Критерий Гурвица:")
    print("Стратегия с индексом {0}".format(max_max(array)))


vald_crit(C)
opt_crit(C)
