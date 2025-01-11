import random
from hero import Hero

"""
Gera um nome aleatório combinando um primeiro nome e um sobrenome.

Returns:
    str: Um nome completo gerado aleatoriamente.
"""
def generate_random_name() -> str:
    first_names = [
        "Arthas", "Elyra", "Kael", "Lirien", "Thrand", "Doran", "Velora", "Baldric", "Ceris", "Fenrir"
    ]
    last_names = [
        "Stormblade", "Duskwalker", "Brightflame", "Ironfist", "Nightshade", "Shadowmourn", "Windwhisper", "Duskbane", "Emberfall", "Frostward"
    ]
    
    # Escolher aleatoriamente um primeiro nome e um sobrenome
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    # Retornar o nome completo
    return f"{first_name} {last_name}"

"""
Gera um novo herói com características aleatórias, dentro de valores mínimos e máximos inteiros.

Args:
    min (int): O valor mínimo para os atributos.
    max (int): O valor máximo para os atributos.
    
Returns:
    Hero: Um objeto Hero com atributos aleatórios.
"""
def generate_random_hero(min: int, max: int) -> Hero:
    return Hero(
        name=generate_random_name(),        # Nome gerado aleatoriamente
        strength=random.randint(min, max), # Força entre min e max
        dexterity=random.randint(min, max),# Destreza entre min e max
        vigor=random.randint(min, max),    # Vigor entre min e max
        intelligence=random.randint(min, max), # Inteligência entre min e max
        resistance=random.randint(min, max)    # Resistência entre min e max
    )

"""
Faz um mix aleatório das características de dois herois para gerar um novo

:param hero1: Primeiro heroi
:param hero2: Segundo heroi
"""
def crossover(hero1: Hero, hero2: Hero) -> Hero:
    return Hero(
        name=generate_random_name(),
        strength=random.choice([hero1.strength, hero2.strength]),
        dexterity=random.choice([hero1.dexterity, hero2.dexterity]),
        vigor=random.choice([hero1.vigor, hero2.vigor]),
        intelligence=random.choice([hero1.intelligence, hero2.intelligence]),
        resistance=random.choice([hero1.resistance, hero2.resistance])
    )

"""
Gera uma nova geração de heróis, com base no cruzamento e mutação.

:param heroes: Lista de heróis da geração atual.
:param mutation_rate: Taxa de mutação para as habilidades dos heróis.
:param population_size: Número de heróis a serem gerados na próxima geração.
:return: Lista de heróis na próxima geração.
"""
def generate_next_generation(heroes: list[Hero], mutation_rate:float=0.1, population_size:int=10) -> list[Hero]:
    next_generation = []
    
    # Gera a próxima geração de heróis
    while len(next_generation) < population_size:
        # Seleciona os melhores pais para cruzamento
        parent1, parent2 = select_parents(heroes)
        
        # Gera o próximo herói a partir do cruzamento dos pais
        next_hero = crossover(parent1, parent2)
        
        # Aplica mutação ao próximo herói
        next_hero = mutate(next_hero, mutation_rate)
        
        # Adiciona o herói à próxima geração
        next_generation.append(next_hero)
    
    return next_generation


"""
Aplica uma mutação no herói com uma certa probabilidade em cada habilidade.
A mutação altera aleatoriamente o valor das habilidades dentro de um intervalo.

:param hero: O herói a ser mutado.
:param mutation_rate: A probabilidade de cada habilidade ser mutada.
:return: O herói mutado.
"""
def mutate(hero: Hero, mutation_rate:float=0.1) -> Hero:
    if random.random() < mutation_rate:
        # Mutar força
        hero.strength += random.uniform(-10, 10)  # Aumenta ou diminui até 10 pontos
        hero.strength = max(0, min(hero.strength, 100))  # Garante que o valor fique entre 0 e 100
        
    if random.random() < mutation_rate:
        # Mutar destreza
        hero.dexterity += random.uniform(-10, 10)
        hero.dexterity = max(0, min(hero.dexterity, 100))  # Garante que o valor fique entre 0 e 100
        
    if random.random() < mutation_rate:
        # Mutar vigor
        hero.vigor += random.uniform(-10, 10)
        hero.vigor = max(0, min(hero.vigor, 100))  # Garante que o valor fique entre 0 e 100
        
    if random.random() < mutation_rate:
        # Mutar inteligência
        hero.intelligence += random.uniform(-10, 10)
        hero.intelligence = max(0, min(hero.intelligence, 100))  # Garante que o valor fique entre 0 e 100
        
    if random.random() < mutation_rate:
        # Mutar resistência
        hero.resistance += random.uniform(-10, 10)
        hero.resistance = max(0, min(hero.resistance, 100))  # Garante que o valor fique entre 0 e 100
    
    return hero

"""
Calcula o fitness de um herói com base em seus atributos.

Args:
    hero (dict): Um dicionário contendo os dados do herói.

Returns:
    float: O valor do fitness calculado.
"""
def fitness(hero: Hero) -> float:
    fitness = (
        hero.level * 2 +
        hero.strength * 1.5 +
        hero.dexterity * 1.2 +
        hero.vigor * 1.3 +
        hero.max_floor * 3
    )
    return f"%.3f" %(fitness)

"""
Seleciona dois guerreiros com os melhores atributos para geração de um novo
Args:
    heroes (list[Hero]): uma lista de herois
Returns:
    tuple[Hero]: uma tupla com os dois melhores herois de acordo com o fitness
"""
def select_parents(heroes: list[Hero]) -> tuple[Hero, Hero]:
    # Ordena os heróis com base no fitness em ordem decrescente.
    heroes_sorted = sorted(heroes, key=fitness, reverse=True)
    
    # Seleciona os dois melhores heróis como pais.
    return heroes_sorted[0], heroes_sorted[1]

# Gerar uma população inicial de heróis
initial_min_val = 0
initial_max_val = 20
heroes = [generate_random_hero(initial_min_val, initial_max_val) for _ in range(10)]

# Exibir a população inicial com suas pontuações de fitness
print("População inicial:")
for hero in heroes:
    print(f"{hero} - Fitness: {fitness(hero)}")

# Gerar a próxima geração com mutação e um número específico de heróis
population_size = 5  # Definir o número de heróis na próxima geração
next_gen = generate_next_generation(heroes, mutation_rate=0.2, population_size=population_size)

# Exibir a próxima geração
print("\nPróxima geração:")
for hero in next_gen:
    print(f"{hero} - Fitness: {fitness(hero)}")

