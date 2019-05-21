import numpy as np

point_quantity = 5
sphere_radius = 10000
detection_radius = 4000
epsilon = detection_radius / sphere_radius
count = 10000


def analytic_method():
    return point_quantity / 2 * (1 - np.sqrt(1 - epsilon ** 2))


def get_random_point():
    z = np.random.uniform(-epsilon, epsilon)
    phi = np.random.uniform(0, 2 * np.pi)
    phi = 0 if phi == 2 * np.pi else phi
    r = np.sqrt(1 - (z ** 2))
    x = np.cos(phi) * r
    y = np.sin(phi) * r
    return np.array([x, y, z])


def get_points_array():
    points_list = []
    for i in range(point_quantity):
        points_list.append(get_random_point())
    return points_list


def win_function():
    win = False
    p_b = get_random_point()
    p_a = get_points_array()
    max_distance = epsilon / np.sin((np.pi - np.arcsin(epsilon / sphere_radius)) / 2)
    for p_a in p_a:
        distance = np.sqrt(np.sum((p_a - p_b) ** 2))
        if distance <= max_distance:
            win = True
    return win


win_a = 0
for i in range(0, count):
    if win_function():
        win_a += 1
numerical_result = win_a / count
analytic = analytic_method()
print("Игра на сфере, где игрок 1 выбирает {0} точек, с радиусом {1}:".format(point_quantity, detection_radius))
print("Выйгрыш игрока 1: {0: <3.4f}".format(numerical_result))
print("Выйгрыш игрока 2: {0: <3.4f}".format(1 - numerical_result))
print("Результат аналитического метода: {0:<3.4f}".format(analytic))
print("Сравнение: {0:<3.4f}".format(np.abs(analytic - numerical_result)))
