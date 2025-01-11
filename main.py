import json
import sys

# adding Folder_2 to the system path
sys.path.insert(0, './game')
sys.path.insert(1, './evo')

from evo import fitness, generate_random_hero
from hero import Hero

"""
Salva os dados de um herói em um arquivo JSON.

Args:
    hero (Hero): Um dicionário contendo os dados do herói.
    filename (str): O nome do arquivo JSON para salvar.
"""
def save_hero_to_json(hero: Hero, filename):
    try:
        with open(filename, 'w') as file:
            # name, strength, dexterity, vigor, intelligence, resistance, level
            data = {
                "name": hero.name,
                "level": hero.level,
                "strength": hero.strength,
                "dexterity": hero.dexterity,
                "vigor": hero.vigor,
                "intelligence": hero.intelligence,
                "resistance": hero.resistance,
                "experience": hero.exp,
                "max_floor": hero.max_floor,
                "fitness": hero.fitness
            }
            json.dump(data, file, indent=4)
        print(f"Herói salvo com sucesso no arquivo: {filename}")
    except Exception as e:
        print(f"Erro ao salvar o herói: {e}")

# Hero(name, strength, dexterity, vigor, intelligence, resistance)

# Lista de heróis com exemplos
# Heroes starts with 50 points
heroes = [generate_random_hero(0, 20) for _ in range(5)]

# Salvar cada herói no arquivo JSON
for i, hero in enumerate(heroes):
    heroes_data_folder = "data/heroes/"
    filename = f"hero_{i+1}.json"
    hero.setFitness(fitness(hero))
    save_hero_to_json(hero, heroes_data_folder+filename)
