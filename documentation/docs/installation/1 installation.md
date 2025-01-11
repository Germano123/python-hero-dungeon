# Installation Guide

Welcome to **Hero Evolution: Infinite Dungeon**! This guide will walk you through setting up the project and running your first tests. Whether you're here to explore the evolutionary algorithm or dive into the visual gameplay with Pygame, we've got you covered.

---

## **Prerequisites**

Before you get started, make sure you have the following installed on your system:

- **Python 3.9 or higher**  
- **pip** (Python package manager)  
- Recommended: A virtual environment tool (like `venv`) to isolate dependencies.

---

## **Installation Steps**

1.Clone the Repository

```bash
git clone https://github.com/your-repo/hero-evolution-dungeon.git
cd hero-evolution-dungeon
```

2.Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3.Install Dependencies

```bash
pip install -r requirements.txt
```

---

### **Running the Evolutionary Algorithm (CLI-Only)**
If you'd like to test the evolutionary algorithm independently from the game, follow these steps:

1.Navigate to the evolution directory or wherever the algorithm files are stored

```bash
cd evo
```

2.Run the algorithm

```bash
bash
python run_evolution.py
```

This will:  

- Generate a population of heroes.  
- Evolve them based on the fitness function.  
- Display the results of the evolution process in the console.

3.Example Output

```bash
Generation 1: Hero A (Fitness: 25.3), Hero B (Fitness: 24.7)
Generation 2: Hero C (Fitness: 27.8), Hero D (Fitness: 26.1)
```

---

### **Running the Game with Pygame**
To test the visual gameplay and the dungeon mechanics, follow these steps:

Run the game in the root of the project:
```bash
python src/main.py
```

Example:

- You will see a grid of hero cards with basic stats.
- Dungeon floors and monsters will appear as you interact with the game.
