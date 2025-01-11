# Fitness Evaluation

Fitness evaluation is the cornerstone of the evolution system, determining which heroes are most suited to face the challenges of the dungeon. By quantifying a hero's performance, we identify the strongest candidates to carry their traits into the next generation.

## What is Fitness?
Fitness is a numerical score that reflects a hero's overall effectiveness in combat, survivability, and progression within the dungeon. This score is used to:

1. **Rank Heroes**: Identify which heroes performed best during their trials.
2. **Guide Selection**: Determine which heroes will become parents for the next generation.
3. **Measure Progress**: Track improvements across generations.

## Fitness Criteria
A hero’s fitness score is calculated using multiple factors:

### 1. Dungeon Progression
- **Definition**: The number of floors a hero successfully clears before being defeated.
- **Weight**: Heavily weighted since progression reflects adaptability and strength.

### 2. Combat Performance
- **Damage Efficiency**: The ratio of damage dealt to damage taken.
- **Consistency**: Ability to sustain performance across multiple encounters.
- **Critical Hits**: The frequency and impact of critical strikes (future implementation).

### 3. Level Advancement
- **Experience Points (XP)**: Gained by defeating enemies; used to calculate the hero’s level.
- **Level Growth**: Heroes that reach higher levels during their dungeon run are rewarded with higher fitness scores.

## Fitness Formula
The fitness score is calculated using the following formula:

```
Fitness = (Dungeon Progression * Weight1) + (Damage Efficiency * Weight2) + (Level Growth * Weight3)
```

### Example Weights:
- Dungeon Progression: 50%
- Damage Efficiency: 30%
- Level Growth: 20%

These weights can be adjusted to prioritize specific traits based on gameplay goals.

## Example Calculation
1. **Hero Performance**:
   - Floors Cleared: 15
   - Damage Dealt: 1000
   - Damage Taken: 250
   - Level Reached: 5

2. **Metrics**:
   - Dungeon Progression = 15
   - Damage Efficiency = 1000 / 250 = 4.0
   - Level Growth = 5

3. **Formula Application**:
   
   ```
   Fitness = (15 * 0.5) + (4.0 * 0.3) + (5 * 0.2)
          = 7.5 + 1.2 + 1.0
          = 9.7
   ```

4. **Fitness Score**: 9.7

## Adapting the Formula
The formula can be tailored to fit different priorities:

- **Combat-Focused Heroes**: Increase the weight for Damage Efficiency.
- **Survival-Focused Heroes**: Emphasize Dungeon Progression.
- **Balanced Approach**: Maintain even weights across all criteria.

## What’s Next?
Learn about the next stage of hero evolution: **[Crossover and Mutation](3%20crossover_mutation.md)**.

