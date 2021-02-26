import random
import sys
import time

num_sol = 0
local_best_fitness = sys.maxsize


def fitness_fn(x, y):
    # first chunk:
    first = 1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * (x ** 2) - 14 * y + 6 * x * y + 3 * (y ** 2))

    # second chunk:
    second = 30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * (x ** 2) + 4 * y - 36 * x * y + 27 * (y ** 2))

    fitness = first * second
    return fitness


def RHC(sp, p, z, seed):
    global num_sol, local_best_fitness
    num_sol = 0

    local_best_sp = []
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

        num_sol += 1

        if not ((sp[0] >= (-2)) and (sp[1] <= 2)):
            print("x, y is out of range")
            continue

        temp_fitness = fitness_fn(sp[0], sp[1])

        if temp_fitness < local_best_fitness:
            local_best_fitness = temp_fitness
            local_best_sp = sp.copy()

    return local_best_sp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # global_best_sp = []  # store only one sp at all, which is the best one
    # global_sp = []  # list to store the generated new sp
    global_fitness = []  # list to store the all the generated fitness
    global_runtime_arr = []  # list to store all the runtime
    sp_arr = [[0.4, -0.5], [-0.5, 0.3], [1, -2], [0, 0]]  # list for the assigned sp values
    p_arr = [30, 120]  # list for the assigned p values
    z_arr = [0.03, 0.1]  # list for the assigned z values
    seed_arr = [1, 2]  # list for the assigned seed values
    runtime_num = 0  # to keep track of which runtime are we in

    """The following implement is asking using for arguments, which is the slow way"""

    # if len(sys.argv) != 6:
    #     print("not enough argument!")
    #     sys.exit()
    #
    # sp1 = float(sys.argv[1])
    # sp2 = float(sys.argv[2])
    # my_p = sys.argv[3]
    # my_z = sys.argv[4]
    # my_seed = sys.argv[5]
    #
    # if (sp1 < -2) or (sp1 > 2):
    #     print("sp should start with range [-2,2]")
    #     sys.exit()
    #
    # if (sp2 < -2) or (sp2 > 2):
    #     print("sp should start with range [-2,2]")
    #     sys.exit()
    #
    # my_sp = [sp1, sp2]

    for my_sp in sp_arr:
        for my_p in p_arr:
            for my_z in z_arr:
                for my_seed in seed_arr:
                    local_best_fitness = sys.maxsize
                    num_sol = 0
                    runtime_num += 1
                    temp_start_time = time.time()
                    temp_best_sp = RHC(my_sp, my_p, my_z, my_seed).copy()
                    temp_time_taken = time.time() - temp_start_time  # calculate the runtime
                    global_runtime_arr.append(temp_time_taken)  # store the runtime
                    global_fitness.append(local_best_fitness)
                    # global_sp.append(temp_best_sp)  # store the sp value
                    print("\n\nRUNTIME #" + str(runtime_num))
                    print("SP:", end="")
                    print(my_sp, end=" ")
                    print("p:", end=" ")
                    print(my_p, end=" ")
                    print("z:", end=" ")
                    print(my_z, end=" ")
                    print("num_sol:", end=" ")
                    print(num_sol, end=" ")
                    print("seed:", end=" ")
                    print(my_seed, end=" ")
                    print("runtime:", end=" ")
                    print(temp_time_taken, end=" ")
                    print("num_sol:", end=" ")
                    print(num_sol, end=" ")
                    print("fitness:", end=" ")
                    print(local_best_fitness, end="")

    print("\n")
    best_fitness = min(global_fitness)
    print("The best fitness is: ", str(best_fitness))
