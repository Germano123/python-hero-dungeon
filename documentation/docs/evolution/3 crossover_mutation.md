# Crossover and Mutation

Crossover and mutation are the primary mechanisms that drive the evolution of heroes in the game. These processes ensure genetic diversity, allowing for the emergence of powerful heroes capable of overcoming the dungeon’s challenges.

## What is Crossover?
Crossover is a process where two parent heroes combine their attributes to create offspring. This simulates genetic inheritance, blending traits from both parents to produce unique heroes.

### Crossover Process
1. **Selection of Parents**:
   - Two parent heroes are selected based on their fitness scores.
   - Higher fitness scores increase the likelihood of being selected, but randomization ensures diversity.

2. **Attribute Mixing**:
   - Each attribute (e.g., strength, dexterity) is inherited based on a weighted average or randomly chosen from one of the parents.
   - Example:
     - Parent 1 Strength: 15
     - Parent 2 Strength: 10
     - Offspring Strength: Randomly between 10 and 15 or calculated as an average (e.g., 12.5).

3. **Special Traits**:
   - Rare traits or abilities may have a small chance to transfer fully from one parent.

## What is Mutation?
Mutation introduces randomness into the offspring’s attributes, ensuring variety and the potential for unexpected heroes with extraordinary traits.

### Mutation Process
1. **Probability**:
   - Each attribute has a small chance (e.g., 5%) to mutate.
   - The mutation rate can be adjusted to balance gameplay.

2. **Value Changes**:
   - Mutations slightly increase or decrease an attribute within a predefined range.
   - Example:
     - Base Strength: 12
     - Mutation: +3
     - Final Strength: 15

3. **Rare Mutations**:
   - Occasionally, mutations can result in extreme changes, such as doubling an attribute or unlocking unique abilities.

## Example Workflow
1. **Select Parents**:
   - Hero A (Strength: 14, Dexterity: 10, Vigor: 12)
   - Hero B (Strength: 12, Dexterity: 14, Vigor: 11)

2. **Crossover**:
   - Offspring inherits:
     - Strength: Average of 14 and 12 = 13
     - Dexterity: Randomly chosen = 10
     - Vigor: Average of 12 and 11 = 11.5

3. **Mutation**:
   - Dexterity mutates: +2
   - Final Dexterity: 12

4. **Result**:
   - Offspring Attributes: Strength = 13, Dexterity = 12, Vigor = 11.5

## Visualizing Crossover and Mutation
Here are suggestions for visual aids:

### 1. Crossover Diagram
- A visual representation of two parent heroes passing their attributes to an offspring.
- Example:
  - Parent A and Parent B connected by lines to Offspring.
  - Attributes displayed in a table or on a radial graph.

### 2. Mutation Example
- Show an attribute bar (e.g., strength) before and after mutation.
- Include annotations highlighting the mutation process.

### 3. Generational Flowchart
- Diagram illustrating multiple generations:
  - Parents producing offspring.
  - Offspring with mutations shown in distinct colors.

## Balancing Crossover and Mutation
To maintain a fun and fair gameplay experience:
- **Crossover** ensures continuity by retaining the best traits.
- **Mutation** prevents stagnation by introducing randomness.
- Together, they create a dynamic and unpredictable evolution system.

## What’s Next?
Learn how heroes are visually represented in the game: **[Interface: Heroes](../interface/2%20heroes.md)**.

