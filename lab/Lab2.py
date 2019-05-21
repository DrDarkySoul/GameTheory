from BrownRobins import brown_robinson_method, print_list
import numpy as np

a = -5
b = 5/12
c = 10/3
d = -2/3
e = -4/3

# Example

# a = -3
# b = 3/2
# c = 18/5
# d = -18/50
# e = -72/25

Hxx = 2 * a
Hyy = 2 * b

if (Hxx < 0.0) & (Hyy > 0.0):
    print("Игра выпукло-вогнутая")


def print_matrix(mtx):
    a = "[" + "\n"
    for m in mtx:
        a += print_list(m) + "\n"
    return a + ']'


def h(a, b, c, d, e, x, y):
    return a * x * x + b * y * y + c * x * y + d * x + e * y


def make_array(N):
    array = []
    for i in range(0, N + 1):
        array.append([])
        x = i / N
        for j in range(0, N + 1):
            y = j / N
            array[i].append(h(a, b, c, d, e, x, y))
    print(print_matrix(array))
    return array


def find_saddle_point(array, N):
    row_min = [np.amax(array)] * (N + 1)
    col_max = [np.amin(array)] * (N + 1)
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            row_min[j] = min(row_min[j], array[j][i])
            col_max[i] = max(col_max[i], array[j][i])
    print(print_list(row_min))
    print(print_list(col_max))
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if array[j][i] == row_min[j] == col_max[i]:
                print("Есть седловая точка:")
                print("x = {0: <5.4}, y = {1: <5.4}, H = {2: <5.4}".format(j/N, i/N, array[j][i]))
                return j/N, i/N, array[j][i]
    print("Седловых точек нет!")
    return -1, -1, -1


def number_method(a, b, c, d, e):
    print("Аналитическое решение")
    y = (c * d - 2 * a * e) / (4 * a * b - c * c)
    x = - ((c * y + d) / (2 * a))
    H = h(a, b, c, d, e, x, y)
    print("x = {0: <5.4}, y = {1: <5.4}, H = {2: <5.4}".format(x, y, H))


number_method(a, b, c, d, e)
for i in range(2, 11):
    arr = make_array(i)
    x, y, H = find_saddle_point(arr, i)
    if(x == -1) & (y == -1) & (H == -1):
        x_k, y_k = brown_robinson_method(np.array(arr))
        x = max(x_k)
        y = max(y_k)
        H = h(a, b, c, d, e, x, y)
        print("x = {0: <5.4}, y = {1: <5.4}, H = {2: <5.4}".format(x, y, H))
