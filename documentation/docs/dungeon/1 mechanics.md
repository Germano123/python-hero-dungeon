# Dungeon Mechanics

The dungeon is an endless challenge designed to test the heroes' abilities and serve as a proving ground for their evolution. Each floor introduces new threats and increasing difficulty, ensuring that only the strongest heroes survive and progress.

## Infinite Floors

The dungeon consists of an infinite number of floors. Heroes advance floor by floor, facing increasingly powerful enemies as they ascend. The endless nature of the dungeon ensures that no hero's potential is capped, providing a continuous challenge for evaluating fitness and growth.

### Floor Progression

- **Scaling Difficulty**: Each floor features enemies whose levels increase gradually. Every 10 floors, the level of enemies scales more significantly, ensuring a steep increase in difficulty over time.
- **Rewards**: Heroes gain experience points (XP) for defeating enemies, which contribute to their level progression and fitness score.

## Enemy Creatures

Each floor of the dungeon spawns a single enemy creature:

- **Randomized Levels**: Enemy levels are determined based on the current floor, with higher floors generating more powerful foes.
- **Strength and Abilities**: Enemies become more challenging as their levels increase, incorporating stronger attributes and abilities to test the heroes' limits.

## Hero Interaction

- **Combat**: Heroes engage in battle with the enemy creature on their current floor. Combat performance determines whether they advance or are defeated.
- **Leveling System**: Heroes gain XP equal to the enemy's level upon victory. They level up according to the formula:

  ```
  XP >= 5 * Hero Level
  ```

  When this threshold is reached, the hero advances to the next level, improving their attributes and fitness.

- **Defeat**: If a hero is defeated, their progress is recorded, including the floor they reached and their final fitness score. This data is used to refine future generations.

## What’s Next?

Learn more about combat strategies and mechanics in the **[Dungeon Combat](2%20combat.md)** section, or return to understand how heroes evolve through the **[Algorithms](../heroes/3%20algorithms.md)**.

