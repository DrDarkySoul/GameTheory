from BrownRobins import brown_robinson_method
import numpy as np

a = -5
b = 5/12
c = 10/3
d = -2/3
e = -4/3

Hxx = 2 * a
Hyy = 2 * b

if (Hxx < 0.0) & (Hyy > 0.0):
    print("Игра выпукло-вогнутая")


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
    print(array)
    return array


def find_saddle_point(array, N):
    row_min = [0.0] * (N + 1)
    col_max = [-1000.0] * (N + 1)
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            row_min[j] = min(row_min[j], array[j][i])
            col_max[i] = max(col_max[i], array[j][i])
    print(row_min, col_max)
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if array[j][i] == row_min[j] == col_max[i]:
                print("Есть седловая точка:")
                print("x= ", j/N, ", y= ", i/N, ", H= ", array[j][i])
                return j/N, i/N, array[j][i]
    print("Седловых точек нет!")
    return -1, -1, -1


def number_method(a, b, c, d, e):
    print("Аналитическое решение")
    y = (c * d - 2 * a * e) / (4 * a * b - c * c)
    x = - ((c * y + d) / (2 * a))
    H = h(a, b, c, d, e, x, y)
    print("x = ", x, ", y = ", y, "H = ", H)


number_method(a, b, c, d, e)
for i in range(2, 11):
    arr = make_array(i)
    x, y, H = find_saddle_point(arr, i)
    if(x == -1) & (y == -1) & (H == -1):
        x_k, y_k = brown_robinson_method(np.array(arr))
        x = max(x_k)
        y = max(y_k)
        H = h(a, b, c, d, e, x, y)
        print("x = ", x, ", y = ", y, "H = ", H)
