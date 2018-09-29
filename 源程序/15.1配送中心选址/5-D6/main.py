from math import *
import random

# distance:二维数组
# sites: 一维数组
# solution: map<Integer, List<Integer>>
def get_solution_map(distance):
    def solution_map(sites):
        solution = {}
        for s in sites:
            solution[s] = []
        for i in range(len(distance)):
            mark = None
            for j in sites:
                if mark is None:
                    mark = j
                else:
                    if distance[i][j] < distance[i][mark]:
                        mark = j
                    else:
                        pass
            solution[mark].append(i)
        return solution
    return solution_map


def zhangye_solution_map(solution, account):
    def inter(n, l):
        for i in l:
            if n == i:
                return True
            else:
                pass
        return False
    result = []
    for key in solution:
        r = [key]
        for i in range(len(account)):
            if inter(i, solution[key]):
                r.append(1)
            else:
                r.append(0)
        s = 0
        for j in solution[key]:
            s += account[j]
        r.append(s)
        result.append(r)
    return result

# distance: 二维数组
# account： 一维数组
# solution: Map<Integer, List<Integer>>
def get_fitness_function(distance, account):
    def fitness_function(solution):
        solution_map = get_solution_map(distance)
        solution = solution_map(solution)
        cost = 0
        for begin in solution:
            for end in solution[begin]:
                huo_wu_account = account[end]
                juli = distance[begin][end]
                cost += huo_wu_account * juli
        return cost
    return fitness_function

# gen: 一维数组,表示一个基因
# n: Integer
def gen_check(gen, n):
    for i in range(len(gen)):
        if gen[i] >= n:
            return False
        else:
            for j in range(i + 1, len(gen)):
                if gen[i] == gen[j]:
                    return False
                else:
                    pass
    return True

# pop: Integer,种群的大小
# n: 基因的个数
# r： 每个基因的范围
def gen_group_generate(pop, n, r):
    result = []
    for _ in range(pop):
        gen = None
        while True:
            gen = []
            for _ in range(n):
                gen.append(random.randint(0, r))
            if gen_check(gen, r):
                break
        result.append(gen)
    return result


def group_fitness_sum(gen_group, fitness_function):
    return sum(map(lambda x: 1 / x, map(fitness_function, gen_group)))


def filter_gen_group(group, n, value):
    group.sort(key=value, reverse=False)
    return group[:n]


def cross_over(x, y):
    mid = floor(len(x) / 2)
    xx = x[:mid]
    xx.extend(y[mid:])
    yy = y[:mid]
    yy.extend(x[mid:])
    return xx, yy


def make_baby(fitness_function, gen_group, cross_over_p, mutation_p):
    cross_over_p *= 100
    mutation_p *= 100
    fitness_sum = group_fitness_sum(gen_group, fitness_function)
    fitness_list = list(map(lambda x: fitness_function(x) / fitness_sum * 100, gen_group))
    for i in range(1, len(fitness_list)):
        fitness_list[i] += fitness_list[i - 1]
    x, y = None, None
    r = random.randint(0, 99)
    for i in range(len(fitness_list)):
        if r <= fitness_list[i]:
            x = gen_group[i]
            break
    r = random.randint(1, 100)
    for i in range(len(fitness_list)):
        if r <= fitness_list[i]:
            y = gen_group[i]
            break
    # 单点交叉
    xx, yy = cross_over(x, y)

    # 变异
    if random.randint(0, 99) < mutation_p:
        point = random.randint(0, len(xx) - 1)
        xx[point] = (xx[point] + 1) % r
    result = []
    if gen_check(xx, r):
        result.append(xx)
    if gen_check(yy, r):
        result.append(yy)
    return result


def genetic_algorithm_zxx_facade(distance, account, center, pop, cross_over_p, mutation_p, gen_time):
    fitness_function = get_fitness_function(distance, account)
    solution_map = get_solution_map(distance)
    gen_group = gen_group_generate(pop, center, len(account) - 1)
    picture = []
    def gen_check_c(gen):
        for i in range(len(gen)):
            if gen[i] >= 12:
                return False
            else:
                for j in range(i + 1, len(gen)):
                    if gen[i] == gen[j]:
                        return False
                    else:
                        pass
        return True
    for i in range(gen_time):
        mark = 0
        picture.append(fitness_function(gen_group[mark]))
        children = make_baby(fitness_function, gen_group, cross_over_p, mutation_p)
        gen_group.extend(children)
        gen_group = list(filter(gen_check_c, gen_group))
        filter_gen_group(gen_group, pop, fitness_function)
    solution = gen_group[0]
    cost = fitness_function(solution)
    solution = solution_map(solution)
    solution = zhangye_solution_map(solution, account)
    return cost, solution, picture


def genetic_algorithm_zxx_facade_test():
    distance = [
        [0, 1, 6, 7, 4, 3, 4, 6, 6, 9, 8, 9],
        [1, 0, 5, 6, 5, 4, 5, 7, 7, 10, 9, 10],
        [6, 5, 0, 3, 6, 9, 10, 12, 12, 15, 14, 15],
        [7, 6, 3, 0, 3, 10, 11, 13, 13, 16, 15, 12],
        [4, 5, 6, 3, 0, 7, 8, 10, 10, 13, 12, 9],
        [3, 4, 9, 10, 7, 0, 6, 4, 9, 10, 6, 6],
        [4, 5, 10, 11, 8, 6, 0, 2, 9, 5, 4, 9],
        [6, 7, 12, 13, 10, 4, 2, 0, 10, 6, 2, 7],
        [6, 7, 12, 13, 10, 9, 9, 10, 0, 4, 6, 13],
        [9, 10, 15, 16, 13, 10, 5, 6, 4, 0, 4, 9],
        [8, 9, 14, 15, 12, 6, 4, 2, 6, 4, 0, 5],
        [9, 10, 15, 12, 9, 6, 9, 7, 13, 9, 5, 0],
    ]
    account = [5, 4, 2, 3, 2, 4, 3, 5, 4, 3, 2, 2]
    center = 10
    pop = 100
    cross_over_p = 0.80
    mutation_p = 0.05
    gen_time = 100
    cost, solution , picture= genetic_algorithm_zxx_facade(distance, account, center, pop, cross_over_p, mutation_p, gen_time)
    print(cost, solution, picture)


# genetic_algorithm_zxx_facade_test()


def fengzhang(center, pop, cross_over_p, mutation_p, gen_time):
    distance = [
        [0, 1, 6, 7, 4, 3, 4, 6, 6, 9, 8, 9],
        [1, 0, 5, 6, 5, 4, 5, 7, 7, 10, 9, 10],
        [6, 5, 0, 3, 6, 9, 10, 12, 12, 15, 14, 15],
        [7, 6, 3, 0, 3, 10, 11, 13, 13, 16, 15, 12],
        [4, 5, 6, 3, 0, 7, 8, 10, 10, 13, 12, 9],
        [3, 4, 9, 10, 7, 0, 6, 4, 9, 10, 6, 6],
        [4, 5, 10, 11, 8, 6, 0, 2, 9, 5, 4, 9],
        [6, 7, 12, 13, 10, 4, 2, 0, 10, 6, 2, 7],
        [6, 7, 12, 13, 10, 9, 9, 10, 0, 4, 6, 13],
        [9, 10, 15, 16, 13, 10, 5, 6, 4, 0, 4, 9],
        [8, 9, 14, 15, 12, 6, 4, 2, 6, 4, 0, 5],
        [9, 10, 15, 12, 9, 6, 9, 7, 13, 9, 5, 0],
    ]
    account = [5, 4, 2, 3, 2, 4, 3, 5, 4, 3, 2, 2]
    return genetic_algorithm_zxx_facade(
        distance, account, int(center), int(pop), float(cross_over_p), float(mutation_p), int(gen_time)
    )


def fengzhuang_test():
    print(
        fengzhang(
        center = 3,
        pop = 100,
        cross_over_p = 0.80,
        mutation_p = 0.09,
        gen_time = 100))


# fengzhuang_test()
