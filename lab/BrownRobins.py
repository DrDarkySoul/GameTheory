from numpy.linalg import inv
from random import randint
import numpy as np
import matplotlib.pyplot as plt


def add_vectors(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


def indexes(l, e):
    return [index for index, value in enumerate(l) if value == e]


def get_vector(e, s):
    return [e for _ in range(0, s)]


def print_list(lst):
    a = "["
    for l in lst:
        a += "{0: <7.2f} ".format(l)
    return a + ']'


def inverse_matrix_method(c):
    print("Аналитический метод:")
    s = np.size(c, 0)
    u = np.array(get_vector(1., s))
    c_inv = inv(c)
    x_numerator = np.dot(c_inv, u.transpose())
    x_denominator = np.dot(np.dot(u, c_inv), u.transpose())
    x = np.divide(x_numerator, x_denominator)
    y_numerator = np.dot(u, c_inv)
    y_denominator = np.dot(np.dot(u, c_inv), u.transpose())
    y = np.divide(y_numerator, y_denominator)
    value = np.divide(1, y_denominator)
    print("Оптимальная стратегия игрока 1:", print_list(y))
    print("Оптимальная стратегия игрока 2:", print_list(x))
    print("Цена игры: {0: <3.2f}".format(value))


def brown_robinson_method(c):
    print("Метод Брауна–Робинсона:")
    plot_top = []
    plot_bot = []
    size = np.size(c, 0)
    k = 1
    choice_a = randint(0, size - 1)
    choice_b = randint(0, size - 1)
    x_k = get_vector(0, size)
    y_k = get_vector(0, size)
    x_k[choice_a] = x_k[choice_a] + 1
    y_k[choice_b] = y_k[choice_b] + 1
    win_a = c[:, choice_a].tolist()
    loose_b = c[choice_b, :].tolist()
    v_top = max(win_a) / k
    v_bot = min(loose_b) / k
    v_top_min = v_top
    v_bot_max = v_bot
    eps = v_top - v_bot
    print('{0: <3} {1: <3} {2: <3} {3} {4} {5: <3.2f} {6: <3.2f} {7: <3.2f}'
          .format(k, choice_a + 1, choice_b + 1, print_list(win_a), print_list(loose_b), v_top, v_bot, eps))
    plot_bot.append(v_bot)
    plot_top.append(v_top)
    while eps >= 0.1:
        i_len = indexes(loose_b, min(loose_b))
        choice_a = i_len[randint(0, len(i_len) - 1)]
        j_len = indexes(win_a, max(win_a))
        choice_b = j_len[randint(0, len(j_len) - 1)]
        x_k[choice_a] = x_k[choice_a] + 1
        y_k[choice_b] = y_k[choice_b] + 1
        win_a = add_vectors(win_a, c[:, choice_a].tolist())
        loose_b = add_vectors(loose_b, c[choice_b, :].tolist())
        k += 1
        v_top = max(win_a) / k
        v_bot = min(loose_b) / k
        if v_top_min > v_top:
            v_top_min = v_top
        if v_bot_max < v_bot:
            v_bot_max = v_bot
        eps = v_top_min - v_bot_max
        print('{0: <3} {1: <3} {2: <3} {3} {4} {5: <3.2f} {6: <3.2f} {7: <3.2f}'
              .format(k, choice_a + 1, choice_b + 1, print_list(win_a), print_list(loose_b), v_top, v_bot, eps))
        plot_bot.append(v_bot)
        plot_top.append(v_top)
    y_k = [num / k for num in y_k]
    x_k = [num / k for num in x_k]
    print("Оптимальная стратегия игрока 1:", print_list(y_k))
    print("Оптимальная стратегия игрока 2:", print_list(x_k))
    print('Цена игры в промежутке от {0: <3.2} до {1: <3.2}'.format(v_bot, v_top))
    print("Количество раундов: ", k)
    plt.plot(plot_top)
    plt.plot(plot_bot)
    plt.show()
    return x_k, y_k
