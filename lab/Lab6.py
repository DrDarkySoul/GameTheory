import numpy as np

dim = 10
epsilon = 10e-6
control_low = 0
control_high = 100


def get_initial_opinions(control_l, control_h, dimension):
    return np.random.randint(control_l, control_h, dimension)


def print_matrix(matrix):
    print("Матрица доверия:")
    print("\n".join(", ".join("{0:.3f}".format(x) for x in row) for row in matrix))


def get_trust_matrix(dimension):
    matrix = []
    for _ in range(0, dimension):
        row = np.random.sample(dimension)
        matrix.append(row / row.sum())
    print_matrix(matrix)
    return np.array(matrix)


def matrix_reduce(matrix, eps, opinions):
    i = 0
    reduced = True
    while reduced:
        i += 1
        changed_opinions = matrix.dot(opinions).transpose()
        if all(x <= eps for x in np.abs(opinions - changed_opinions)):
            reduced = False
        opinions = changed_opinions
    return opinions, i


def solve(matrix, eps, op):
    op_result, iter_count = matrix_reduce(matrix, eps, op)
    print()
    print("Начальные мнения агентов: X(0) =", op)
    print("Количество итераций:", iter_count)
    print("Результирующее мнение агентов без влияния: X(t->inf) =", ", ".join("{0:.3f}".format(x) for x in op_result))
    print()


def get_agents(dimension):
    agents = np.arange(dimension)
    np.random.shuffle(agents)
    u_size, v_size = len(agents), len(agents)
    while u_size + v_size > len(agents):
        u_size = np.random.randint(1, len(agents))
        v_size = np.random.randint(1, len(agents))
    return agents[:u_size], agents[u_size:u_size + v_size]


def get_controls(control_l, control_h, sign):
    control = np.random.randint(control_l, control_h)
    return control if sign else -control


def solve_influence(matrix, dimension, eps):
    u_agents, v_agents = get_agents(dimension)
    print("Агенты первого игрока: {0}".format(sorted(u_agents)))
    print("Агенты второго игрока: {0}".format(sorted(v_agents)))
    u_control = get_controls(control_low, control_high, True)
    v_control = get_controls(control_low, control_high, False)
    print("Сформированное начальное мнение первого игрока: {0:.0f}".format(u_control))
    print("Сформированное начальное мнение второго игрока: {0:.0f}".format(v_control))
    influenced_opinions = initial_opinions
    for number in np.hstack((v_agents, u_agents)):
        influenced_opinions[number] = u_control if number in u_agents else v_control
    print("Изначальные мнения с учетом сформированных: X(0) =", influenced_opinions)
    result_opinions, iter_count = matrix_reduce(matrix, eps, influenced_opinions)
    print("Количество итераций:", iter_count)
    print("Результирующее мнение: X(t->inf) =", ", ".join("{0:.3f}".format(x) for x in result_opinions))


initial_opinions = get_initial_opinions(control_low, control_high, dim)
trust_matrix = get_trust_matrix(dim)

solve(trust_matrix, epsilon, initial_opinions)
solve_influence(trust_matrix, dim, epsilon)
