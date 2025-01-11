# Introduction to Evolution

The evolution system is the heart of this project, driving the creation of increasingly powerful and specialized heroes. By applying principles of evolutionary algorithms, heroes adapt and improve over successive generations, paving the way for the ultimate hero capable of conquering the endless dungeon.

## Why Evolution?

Evolution allows us to:

1. **Simulate Adaptation**: Heroes evolve to overcome the challenges posed by progressively stronger dungeon enemies.
2. **Discover Potential**: Through generations, heroes with unique combinations of attributes emerge, highlighting exceptional potential.
3. **Optimize Over Time**: By applying fitness-based selection, we ensure that the best traits are carried forward, leading to stronger and more capable heroes.

## How It Works

### 1. Initial Population
The process begins with an initial population of randomly generated heroes. Each hero has randomly assigned attributes, including:

- **Strength**: Determines physical damage dealt.
- **Dexterity**: Influences agility and turn order.
- **Vigor**: Affects health and survivability.
- **Intelligence**: Governs critical thinking and decision-making (future implementation).
- **Resistance**: Improves defense against attacks.

### 2. Fitness Evaluation
Each hero is tested in the dungeon, and their performance determines their fitness score. The fitness score is calculated based on:

- **Dungeon Progress**: The floor reached before defeat.
- **Combat Efficiency**: The ability to deal damage while minimizing damage received.
- **Level Advancement**: The hero's level at the time of defeat.

### 3. Selection
Heroes with higher fitness scores are more likely to be selected as parents for the next generation. This ensures that the strongest traits are preserved and passed on.

### 4. Crossover
During reproduction, two parent heroes combine their DNA to create offspring. Attributes from both parents are mixed to produce a new hero with inherited traits. For example:

- Parent 1: High Strength, Low Dexterity
- Parent 2: Low Strength, High Dexterity
- Offspring: Balanced Strength and Dexterity

### 5. Mutation
To maintain diversity and introduce variability, mutations occur randomly in offspring. These mutations can:

- Slightly increase or decrease an attribute.
- Introduce unexpected traits, such as higher resistance or unique attribute combinations.

### 6. Iteration
This process repeats for multiple generations. Over time, heroes become more specialized, with attributes fine-tuned for overcoming the dungeon’s escalating challenges.

## Example Cycle
1. **Generation 1**: 100 random heroes are generated.
2. **Evaluation**: Each hero is tested in the dungeon, and their fitness scores are recorded.
3. **Selection**: The top 20% of heroes are selected as parents.
4. **Reproduction**: Offspring are created via crossover and mutation.
5. **Generation 2**: A new generation of 100 heroes is created.
6. **Repeat**: The cycle continues until the desired performance level is achieved.

## What’s Next?
Explore how fitness is calculated in detail in the **[Fitness](2%20fitness.md)** section or learn about the mechanics of creating new heroes through **[Crossover and Mutation](3%20crossover_mutation.md)**.

