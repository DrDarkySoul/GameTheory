from itertools import combinations
import numpy as np

Vt = {
    "": 0,
    "1": 4,
    "2": 1,
    "3": 3,
    "4": 1,
    "1 2": 6,
    "1 3": 8,
    "1 4": 6,
    "2 3": 5,
    "2 4": 3,
    "3 4": 3,
    "1 2 3": 9,
    "1 2 4": 8,
    "1 3 4": 10,
    "2 3 4": 7,
    "1 2 3 4": 11,
}

I = "1 2 3 4"

# Example

# Vt = {
#     "1": 0,
#     "2": 1,
#     "3": 1,
#     "12": 1,
#     "13": 1,
#     "23": 1,
#     "123": 4,
# }


def print_game(game):
    for k, v in Vt.items():
        if k != "":
            print("v({0}) = {1};".format(k, v))


def get_vector_shepli(game):
    all_team = [set(k.split(" ")) for k in game.keys() if k != ""]
    vector = np.zeros(5)
    for i in range(1, 5):
        for team in all_team:
            v_s = " ".join(sorted(list(team)))
            v_s_i = " ".join(sorted(list(team.difference(set(str(i))))))
            vector[i] += np.math.factorial(len(team) - 1) * np.math.factorial(4 - len(team)) * (game[v_s] - game[v_s_i])
    return (vector / np.math.factorial(4))[1:5]


def check_super_additive(game):
    is_super_additive = True
    error_coal = []
    all_teams = [set(k.split(" ")) for k in game.keys() if k != "" and k != I]
    for s, t in combinations(all_teams, 2):
        if not s & t:
            key_s = " ".join(sorted(list(s)))
            key_t = " ".join(sorted(list(t)))
            key_st = " ".join(sorted(list(s | t)))
            if game[key_st] < game[key_s] + game[key_t]:
                is_super_additive = False
                error_coal.append(key_st)
    return is_super_additive, error_coal


def check_convex(game):
    is_convex = True
    all_teams = [set(k.split(" ")) for k in game.keys() if k != "" and k != I]
    for s, t in combinations(all_teams, 2):
        if not s & t:
            key_s = " ".join(sorted(list(s)))
            key_t = " ".join(sorted(list(t)))
            key_s_t = " ".join(sorted(list(s | t)))
            key_st = " ".join(sorted(list(s & t)))
            if game[key_st] + game[key_s_t] < game[key_s] + game[key_t]:
                is_convex = False
    return is_convex


while True:
    print("Игра:")
    print_game(Vt)
    is_sa, err = check_super_additive(Vt)
    if not is_sa:
        print("Игра не супераддитивна на наборе {0}".format(err))
    else:
        print("Игра супераддитивна")
    is_conv = check_convex(Vt)
    if not is_conv:
        print("Игра не выпукла")
    else:
        print("Игра выпукла")
    sheply = get_vector_shepli(Vt)
    print("Вектор Шепли ", " ".join(["{0:.2f}".format(x) for x in sheply]))
    sheply_sum = sum(sheply)
    print("Групповая рационализация:")
    if sheply_sum == Vt[I]:
        print("{0:.2f}".format(sheply_sum), "=", Vt[I])
        print("Выполняется")
    else:
        print("{0:.2f}".format(sheply_sum), "!=", Vt[I])
        print("Не выполняется")
    print("Индивидуальная рационализация:")
    for i in range(1, 5):
        print("x{0}:".format(i), "{0:.2f}".format(sheply[i-1]), ">=", Vt[str(i)])
    if not is_sa:
        print("Изменим игру".format(err))
        for key in set(err):
            Vt[key] += 1
    else:
        break
    print()
    print()




