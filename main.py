import random, sys

num_sol = 0
best_fitness = sys.maxsize
best_sp = []


def fitness_fn(x, y):
    # first chunk:
    first = 1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * (x ** 2) - 14 * y + 6 * x * y + 3 * (y ** 2))

    # second chunk:
    second = 30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * (x ** 2) + 4 * y - 36 * x * y + 27 * (y ** 2))

    fitness = first * second
    return fitness


def RHC(sp, p, z, seed):
    global num_sol, best_fitness, best_sp
    z = float(z)

    # set the seed:
    random.seed(seed)

    for i in range(int(p)):
        # best_sp = []
        # random sign:
        sign = [-1, 1][random.randrange(2)]
        z1 = sign * (random.random() * 10 % z)
        z2 = sign * (random.random() * 10 % z)

        # assign changes to sp:
        sp[0] += z1
        sp[1] += z2

        if not ((sp[0] >= (-2)) and (sp[1] <= 2)):
            print("x, y is out of range")
            continue

        num_sol += 1
        temp_fitness = fitness_fn(sp[0], sp[1])

        if temp_fitness < best_fitness:
            best_fitness = temp_fitness
            best_sp = sp.copy()
            print(sp)
            print(" " + str(best_fitness))

    return best_sp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_best_sp = []

    if len(sys.argv) != 6:
        print("not enough argument!")
        sys.exit()

    sp1 = float(sys.argv[1])
    sp2 = float(sys.argv[2])
    my_p = sys.argv[3]
    my_z = sys.argv[4]
    my_seed = sys.argv[5]

    if (sp1 < -2) or (sp1 > 2):
        print("sp should start with range [-2,2]")
        sys.exit()

    if (sp2 < -2) or (sp2 > 2):
        print("sp should start with range [-2,2]")
        sys.exit()

    my_sp = [sp1, sp2]

    for i in range(32):
        my_best_sp = RHC(my_sp, my_p, my_z, my_seed).copy()

    print("best solution: ")
    print(my_best_sp)
    print("num solutions generated: \n" + str(num_sol))
    print("best fitness: \n" + str(best_fitness))
