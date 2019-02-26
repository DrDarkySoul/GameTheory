from numpy.linalg import inv
from random import randint
import numpy as np

C = np.array([
    [1., 11., 11.],
    [7., 5., 8.],
    [16., 6., 2.]
])


def add_vectors(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


def inverse_matrix_method(c):
    print("Аналитический метод:")
    u = np.array([1., 1., 1.])
    c_inv = inv(c)
    x_numerator = np.dot(c_inv, u.transpose())
    x_denominator = np.dot(np.dot(u, c_inv), u.transpose())
    x = np.divide(x_numerator, x_denominator)
    y_numerator = np.dot(u, c_inv)
    y_denominator = np.dot(np.dot(u, c_inv), u.transpose())
    y = np.divide(y_numerator, y_denominator)
    value = np.divide(1, y_denominator)
    print("Оптимальная стратегия игрока 1:", y)
    print("Оптимальная стратегия игрока 2:", x)
    print("Цена игры:", value)


def brown_robinson_method(c):
    print("Метод Брауна–Робинсона:")
    k = 1
    choice_a = randint(0, 2)
    choice_b = randint(0, 2)
    x_k = [0, 0, 0]
    y_k = [0, 0, 0]
    x_k[choice_a] = x_k[choice_a] + 1
    y_k[choice_b] = y_k[choice_b] + 1
    win_a = c[:, choice_a].tolist()
    loose_b = c[choice_b, :].tolist()
    v_top = max(win_a) / k
    v_bot = min(loose_b) / k
    eps = v_top - v_bot
    # print(k, choice_a + 1, choice_b + 1, win_a, loose_b, v_top, v_bot, eps)
    while eps >= 0.1:
        choice_a = loose_b.index(min(loose_b))
        choice_b = win_a.index(max(win_a))
        x_k[choice_a] = x_k[choice_a] + 1
        y_k[choice_b] = y_k[choice_b] + 1
        win_a = add_vectors(win_a, c[:, choice_a].tolist())
        loose_b = add_vectors(loose_b, c[choice_b, :].tolist())
        k += 1
        v_top = max(win_a) / k
        v_bot = min(loose_b) / k
        eps = v_top - v_bot
        # print(k, choice_a + 1, choice_b + 1, win_a, loose_b, v_top, v_bot, eps)
    y_k = [num / k for num in y_k]
    x_k = [num / k for num in x_k]
    print("Оптимальная стратегия игрока 1:", y_k)
    print("Оптимальная стратегия игрока 2:", x_k)
    print("Цена игры в промежутке:", v_bot, v_top)


inverse_matrix_method(C)
brown_robinson_method(C)

