![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.1%2B-green?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-0.0.1-yellow)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![Made with MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-darkgreen?logo=read-the-docs)

![Infinite Dungeon](https://img.shields.io/badge/Dungeon-Infinite-red)
![Heroes Evolution](https://img.shields.io/badge/Heroes-Evolution-purple)
![AI Algorithms](https://img.shields.io/badge/AI-Evolutionary-orange)

### Keywords
[ Game Development, Procedural Generation, Evolutionary Algorithms, Dungeon Crawler, Turn-based Combat, Genetic Programming, Python, PyGame, Roguelike, Idle Game]

# Hero Evolution: Infinite Dungeon

## Table of Contents
- [Introduction](#introduction)
- [Game Mechanics](#game-mechanics)
  - [Dungeon](#dungeon)
  - [Hero](#hero)
  - [Monsters](#monsters)
  - [Generation System](#generation-system)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Game](#running-the-game)
  - [Extending the System](#extending-the-system)
- [Future Features](#future-features)

---

## Introduction

**Hero Evolution** is an idle-style game that simulates an infinite dungeon spawning endless hordes of monsters. Players manage heroes who explore the dungeon, gain experience, and fight progressively stronger enemies. The ultimate goal is to identify and create the special hero from a future generation capable of defending against the infinite horde of monsters.

This project explores procedural mechanics, evolutionary algorithms, and RPG gameplay, making it an ideal playground for both developers and game enthusiasts interested in algorithm-driven games.

---

## Game Mechanics

### Dungeon
The dungeon is an infinite series of floors, each spawning a monster with attributes scaled to the current floor level. 
- **Floor Scaling**: Monster levels and strength increase every 10 floors.
- **Infinite Progression**: Heroes battle through floors until they are defeated.
- **Hero Defeat**: Upon losing a battle, the hero is recorded for analysis, contributing to future generations.

### Hero
Heroes are the main characters, created procedurally with attributes such as:
- **Health Points (HP)**: Determines how much damage a hero can withstand.
- **Attack**: Damage inflicted on monsters.
- **Defense**: Reduces incoming damage.
- **Speed**: Determines turn order during combat.
- **Special Abilities**: Unique traits such as:
  - `Damage Boost`: Temporarily doubles attack.
  - `Defense Boost`: Temporarily doubles defense.
  - `Heal`: Restores a portion of HP.
  - `Critical Strike`: Deals triple damage for one attack.

Heroes gain experience by defeating monsters and level up using the formula:
```
EXP >= 5 * Hero Level
```
Level-ups improve attributes, making heroes stronger with each progression.

### Monsters
Monsters are generated for each floor and possess the following attributes:
- **Level**: Scaled to the dungeon floor.
- **Health Points (HP)**: Scaled to monster level.
- **Attack**: Determines the damage dealt to heroes.
- **Defense**: Reduces damage received from heroes.
- **Speed**: Determines turn order during combat.

### Generation System
Defeated heroes are stored for evaluation based on:
- **Maximum Floor Reached**
- **Hero Level at Defeat**

This data is used in an evolutionary algorithm to generate new heroes with optimized attributes, aiming to produce the ultimate hero capable of surviving infinite floors.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hero-dungeon.git
   cd hero-dungeon
   ```

2. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

---

## Usage

### Running the Game
The game runs as a simulation:
1. Create a hero using the `Hero` class.
2. Start the dungeon with the `Dungeon` class.
3. Observe the hero's progression and collect defeat data for further analysis.

```python
from hero import Hero
from dungeon import Dungeon

# Create a hero
hero = Hero(name="Valiant Warrior")

# Create and run the dungeon
dungeon = Dungeon()
dungeon.enter_dungeon(hero)

# Display defeated heroes
print("\nDefeated Heroes:")
for hero_data in dungeon.failed_heroes:
    print(hero_data)
```

### Extending the System
Developers can extend the project by:
- Adding new monster types with unique abilities.
- Introducing equipment or items for heroes.
- Expanding the evolutionary algorithm for hero generation.

---

## Future Features

### Planned Expansions
1. **Item System**: Introduce weapons, armor, and consumables to enhance hero stats.
2. **Monster Types**: Add diverse monster archetypes such as magical, undead, or elemental creatures with unique resistances and attacks.
3. **Evolutionary Algorithm Refinement**: Incorporate attributes like fitness scores to generate even more optimized heroes.
4. **Multiplayer Mode**: Enable multiple heroes to cooperate or compete in the dungeon.
5. **Idle Automation**: Allow the game to simulate dungeon progression over time without manual input.

---

**Hero Evolution** is an ongoing project with endless potential. Join the quest to create the ultimate hero and defend the world against the infinite horde of monsters!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Germano123/python-hero-dungeon.git&type=Date)](https://star-history.com/#Germano123/python-hero-dungeon.git&Date)
