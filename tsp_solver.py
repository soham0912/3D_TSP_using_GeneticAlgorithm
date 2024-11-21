import random
import numpy as np
import math
from multiprocessing import Pool

def r_inp(filen):
    with open(filen, 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    locations = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    return n, locations

def create_ind(num_cit):
    path = list(range(num_cit))
    path.append(path[0])
    return path

def nearest_neighbor_ind(locations):
    start_city = random.randint(0, len(locations) - 1)
    unvisited = set(range(len(locations)))
    unvisited.remove(start_city)
    path = [start_city]

    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_dis(locations[current_city], locations[city]))
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    path.append(start_city)
    return path

def initialize_pop(pop_size, num_cit, locations):
    pop = [create_ind(num_cit) for _ in range(pop_size - 5)]
    pop += [nearest_neighbor_ind(locations) for _ in range(5)]
    return pop

def euclidean_dis(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)

def total_path_dis(p, locations):
    return sum(euclidean_dis(locations[p[i]], locations[p[i + 1]]) for i in range(len(p) - 1))

def tournament_sel(pop, fitn, t_size):
    selected = random.sample(list(zip(pop, fitn)), t_size)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

def order_cross(par1, par2):
    size = len(par1) - 1
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end] = par1[start:end]
    par2_filtered = [city for city in par2 if city not in child]
    current_index = 0
    for i in range(size):
        if child[i] == -1:
            child[i] = par2_filtered[current_index]
            current_index += 1
    child.append(child[0])
    return child

def pmx_crossover(par1, par2):
    size = len(par1) - 1
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end] = par1[start:end]
    for i in range(start, end):
        if par2[i] not in child:
            pos = i
            while start <= pos < end:
                pos = par2.index(par1[pos])
            child[pos] = par2[i]
    for i in range(size):
        if child[i] == -1:
            child[i] = par2[i]
    child.append(child[0])
    return child

def order_or_pmx(par1, par2):
    if random.random() < 0.5:
        return order_cross(par1, par2)
    else:
        return pmx_crossover(par1, par2)

def swap_mut(ind, mut_rate):
    for i in range(1, len(ind) - 1):
        if random.random() < mut_rate:
            j = random.randint(1, len(ind) - 2)
            ind[i], ind[j] = ind[j], ind[i]

def adaptive_mutation(mut_rate, no_improvement_count):
    return min(mut_rate + (no_improvement_count / 1000), 0.1)

def probabilistic_elitism(population, locations, elite_fraction=0.05):
    sorted_pop = sorted(population, key=lambda ind: total_path_dis(ind, locations))
    elite_size = int(len(population) * elite_fraction)
    return sorted_pop[:elite_size] + random.sample(sorted_pop[elite_size:], 2)

def determine_pop_size(num_cities):
    if num_cities <= 50:
        return 250
    elif 50 < num_cities < 100:
        return 225
    elif 100 <= num_cities < 200:
        return 200
    elif 200 <= num_cities < 400:
        return 150
    elif 400 <= num_cities < 500:
        return 100
    else:
        return 50

def genetic_algo(ls, generations, mutation_rate, patience=50):
    n_cities = len(ls)
    pop_size = determine_pop_size(n_cities)
    population = initialize_pop(pop_size, n_cities, ls)
    best_fitness = float('inf')
    best_individual = None
    no_improvement_count = 0
    fitness_cache = {}

    for g in range(generations):
        fitnesses = []
        for ind in population:
            if tuple(ind) not in fitness_cache:
                fitness_cache[tuple(ind)] = total_path_dis(ind, ls)
            fitnesses.append(1 / fitness_cache[tuple(ind)])

        new_pop = []
        while len(new_pop) < pop_size:
            par1 = tournament_sel(population, fitnesses, 10)
            par2 = tournament_sel(population, fitnesses, 10)
            child = order_or_pmx(par1, par2)
            swap_mut(child, mutation_rate)
            new_pop.append(child)

        new_pop += probabilistic_elitism(population, ls)
        population = new_pop[:pop_size]

        current_best_ind = min(population, key=lambda ind: total_path_dis(ind, ls))
        current_best_fitness = total_path_dis(current_best_ind, ls)

        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_individual = current_best_ind
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        mutation_rate = adaptive_mutation(mutation_rate, no_improvement_count)

        if no_improvement_count >= patience:
            break

    return best_individual, best_fitness

def write_output(filename, total_dis, path, ls):
    with open(filename, 'w') as f:
        f.write(f"{total_dis:.3f}\n")
        for idx in path:
            f.write(f"{ls[idx][0]} {ls[idx][1]} {ls[idx][2]}\n")

def main():
    random.seed(42)
    inp_file = "./input.txt"
    out_file = "./output.txt"
    num_cities, ls = r_inp(inp_file)
    best_path, best_distance = genetic_algo(ls, generations=800, mutation_rate=0.01)
    write_output(out_file, best_distance, best_path, ls)

if __name__ == '__main__':
    main()
