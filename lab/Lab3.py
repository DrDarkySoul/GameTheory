import numpy as np


def analytic_method(point_quantity, detection_radius):
    return point_quantity / 2 * (1 - np.sqrt(1 - detection_radius ** 2))


def get_random_point():
    z = np.random.uniform(-1, 1)
    phi = np.random.uniform(0, 2 * np.pi)
    phi = 0 if phi == 2 * np.pi else phi
    r = np.sqrt(1 - (z ** 2))
    x = np.cos(phi) * r
    y = np.sin(phi) * r
    return np.array([x, y, z])


def get_points_array(point_quantity):
    points_list = []
    for _ in range(point_quantity):
        points_list.append(get_random_point())
    return points_list


def win_function(detection_radius, point_quantity):
    win = False
    p_b = get_random_point()
    p_a = get_points_array(point_quantity)
    max_distance = detection_radius / np.sin((np.pi - np.arcsin(detection_radius)) / 2)
    for a_i in p_a:
        distance = np.sqrt(np.sum((a_i - p_b) ** 2))
        if distance <= max_distance:
            win = True
    return win


def sphere_game(point_quantity, detection_radius, count):
    win_a = 0
    for i in range(0, count):
        if win_function(detection_radius, point_quantity):
            win_a += 1
    numerical_result = win_a / count
    analytic = analytic_method(point_quantity, detection_radius)

    print("Игра на сфере, где игрок 1 выбирает {0} точек, с радиусом {1}:".format(point_quantity, detection_radius))
    print("Выйгрыш игрока 1: {0: <3.4f}".format(numerical_result))
    print("Выйгрыш игрока 2: {0: <3.4f}".format(1 - numerical_result))
    print("Результат аналитического метода: {0:<3.4f}".format(analytic))
    print("Сравнение: {0:<3.4f}".format(np.abs(analytic - numerical_result)))


sphere_game(10, 0.2, 10000)
sphere_game(5, 0.4, 10000)
