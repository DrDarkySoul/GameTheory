N = 1
# a = -5
# b = 5/12
# c = 10/3
# d = -2/3
# e = -4/3

a = -3
b = 3/2
c = 18/5
d = -18/50
e = -72/25

Hxx = 2*a
Hyy = 2*b

if (Hxx < 0.0) & (Hyy > 0.0):
    print("Игра выпукло-вогнутая")


def number_method(a, b, c, d, e):
    print("Аналитическое решение")
    y = (c * d - 2 * a * e) / (4 * a * b - c * c)
    x = - ((c * y + d) / (2 * a))
    H = a * x * x + b * y * y + c * x * y + d * x + e * y
    print("x = ", x, ", y = ", y, "H = ", H)


number_method(a, b, c, d, e)
