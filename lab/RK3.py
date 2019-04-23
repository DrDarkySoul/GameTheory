import itertools
import math

Vt = {
    "1": 4,
    "2": 1,
    "3": 3,
    "4": 1,
    "12": 6,
    "13": 8,
    "14": 6,
    "23": 5,
    "24": 3,
    "34": 3,
    "123": 9,
    "124": 8,
    "134": 10,
    "234": 7,
    "1234": 11,
}

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


def get_keys(string):
    length = len(string)
    arr = [0] * length
    if length == 0:
        return arr
    for i in range(0, length):
        arr[i] = int(string[i])
    return arr


def get_tuple(string):
    answer = []
    for i in range(2, len(string)):
        a = list(itertools.combinations(string, i))
        answer.append(a)
    return answer


def set_to_str(s):
    answer = ""
    for i in s:
        answer += str(i)
    return answer


def check_set(set_1, set_2, value):
    str_1 = set_to_str(set_1)
    str_2 = set_to_str(set_2)
    summ = Vt[str_1] + Vt[str_2]
    if value <= summ:
        return False
    return True


def check_vp_set(set_1, set_2):
    str_1 = set_to_str(set_1)
    str_2 = set_to_str(set_2)
    sum_1 = Vt[str_1] + Vt[str_2]
    str_1 = set_to_str(set.union(set_1, set_2))
    str_2 = set_to_str(set.intersection(set_1, set_2))
    sum_2 = Vt[str_1] + Vt[str_2]
    if sum_2 < sum_1:
        return False
    return True


def to_int_tuple(tup):
    arr = []
    for i in tup:
        arr.append(int(i))
    return arr


def check_sa(v):
    for key, value in v.items():
        if len(key) > 1:
            set_k = set(get_keys(key))
            tuple_ = get_tuple(key)
            for li in tuple_:
                for tup in li:
                    set_1 = set(to_int_tuple(tup))
                    set_2 = set_k - set_1
                    sa = check_set(set_1, set_2, value)
                    if not sa:
                        print(set_1, set_2)
                        return False
    return True


def check_vp(v):
    for key, value in v.items():
        if len(key) > 1:
            a = get_tuple(key)
            b = get_tuple(key)
            for li in a:
                for tup in li:
                    for lib in b:
                        for tupb in lib:
                            set_1 = set(to_int_tuple(tup))
                            set_2 = set(to_int_tuple(tupb))
                            sa = check_vp_set(set_1, set_2)
                            if not sa:
                                print(set_1, set_2)
                                return False
    return True


def shaply(v):
    N = 4
    answer = []
    for j in range(0, N):
        sum_ = 0
        for key, value in v.items():
            if str(j) in key:
                S = len(key)
                for i in get_keys(key):
                    sum_ += math.factorial(S-1) * math.factorial(N-S) * (value - Vt[key.replace(str(i), "")])
        answer.append(sum_/math.factorial(N))
    return N


a = check_sa(Vt)
b = check_vp(Vt)

print(shaply(Vt))

