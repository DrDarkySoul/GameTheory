import numpy as np
from numpy.linalg import inv

intersection = np.array([
    [[1, 0.5], [2, 0]],
    [[1, 2], [0.5, 0]]], float)

family = np.array([
    [[4, 0], [0, 1]],
    [[1, 0], [0, 4]]], float)

prisoner = np.array([
    [[-5, 0], [-10, -1]],
    [[-5, -10], [0, -1]]], float)


def analytic_method(bi_matrix):
    print("Аналитический метод:")
    matrix_dim, _ = bi_matrix[0].shape
    u = np.ones((1, matrix_dim), int)
    tmp_a = u.dot(inv(bi_matrix[0]).dot(u.transpose()))
    tmp_b = u.dot(inv(bi_matrix[0]).dot(u.transpose()))
    v_x = 1 / tmp_a
    v_y = 1 / tmp_b
    print("VX = {0:.2f}".format(v_x[0][0]))
    print("VY = {0:.2f}".format(v_y[0][0]))
    x = v_x * inv(bi_matrix[0]).dot(u.transpose())
    y = v_y * u.dot(inv(bi_matrix[0]))
    print("X = " + " ".join(["{0:.2f}".format(el) for el in x.transpose()[0]]))
    print("Y = " + " ".join(["{0:.2f}".format(el) for el in y[0]]))


def check_nash(bi_matrix, i, j):
    matrix_dim, _ = bi_matrix[0].shape
    best_a_strategy = True
    best_b_strategy = True
    for iterI in range(matrix_dim):
        if bi_matrix[0][iterI][j] > bi_matrix[0][i][j]:
            best_b_strategy = False
        if bi_matrix[1][i][iterI] > bi_matrix[1][i][j]:
            best_a_strategy = False
    return best_a_strategy and best_b_strategy


def check_pareto(bi_matrix, i, j):
    matrix_dim, _ = bi_matrix[0].shape
    best_strategy = True
    for iIter in range(matrix_dim):
        for jIter in range(matrix_dim):
            if ((bi_matrix[0][iIter][jIter] > bi_matrix[0][i][j] and
                 bi_matrix[1][iIter][jIter] >= bi_matrix[1][i][j]) or
                    (bi_matrix[1][iIter][jIter] > bi_matrix[1][i][j] and
                     bi_matrix[0][iIter][jIter] >= bi_matrix[0][i][j])):
                best_strategy = False
    return best_strategy


def generate_bi_matrix(min_, max_, dim):
    return np.array([np.random.randint(min_, max_, (dim, dim)), np.random.randint(min_, max_, (dim, dim))], int)
