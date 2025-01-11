import sys

# adding Folder_2 to the system path
sys.path.insert(0, '../game')

from evo import fitness, generate_random_hero, generate_next_generation
from hero import Hero

"""Expected output
Generation 1: Hero A (Fitness: 25.3), Hero B (Fitness: 24.7)
Generation 2: Hero C (Fitness: 27.8), Hero D (Fitness: 26.1)
"""
generation_count = 5

min_attribute_val = 0
max_attribute_val = 20

heroes = [generate_random_hero(min_attribute_val, max_attribute_val) for _ in range(generation_count)]

# show first generation fitness
print("População inicial:")
for hero in heroes:
    print(f"{hero.name} - Fitness: {fitness(hero)}")

# define how many generations
max_generations = 3

for index in range(max_generations):
    # generate next generation with mutation
    mutation_rate = 0.2
    next_gen = generate_next_generation(heroes, mutation_rate=mutation_rate, population_size=generation_count)
    
    # show generations
    print(f"\nGeneration {index+1}:")
    for hero in next_gen:
        print(f"{hero.name} - Fitness: {fitness(hero)}")
