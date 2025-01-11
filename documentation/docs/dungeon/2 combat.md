# Dungeon Combat

Combat in the dungeon is a straightforward yet critical aspect of the gameplay, providing heroes with the opportunity to showcase their attributes and gain valuable experience. Each battle pits a hero against an enemy creature, with turns alternating based on agility.

## Combat Mechanics

### Turn Order
- Turn order is determined by the **Agility** attribute of both the hero and the enemy.
- The combatant with the higher agility takes the first turn.
- In the case of a tie, the hero always goes first.

### Attacking
- On their turn, the combatant (hero or enemy) deals damage to their opponent.
- The damage dealt is based on the **Strength** attribute:

  ```
  Damage = Strength
  ```

### Health Management
- Both the hero and the enemy have a **Health** attribute.
- Each attack reduces the opponent's health by the damage amount calculated.
- Combat ends when one combatant's health reaches zero or below.

## Victory and Defeat

### Victory
- If the hero defeats the enemy:
  - The hero earns experience points (XP) equal to the enemy's level.
  - The hero progresses to the next dungeon floor to face a stronger enemy.

### Defeat
- If the enemy defeats the hero:
  - The hero's progress is recorded, including their fitness score and the floor they reached.
  - The hero's data is used to refine the evolution algorithm for future generations.

## Simplified Example

1. **Hero vs. Enemy:**
   - Hero: Health = 50, Strength = 12, Agility = 8
   - Enemy: Health = 40, Strength = 10, Agility = 6

2. **Turn Order:**
   - The hero attacks first (Agility = 8 > 6).

3. **Combat Flow:**
   - Turn 1: Hero deals 12 damage to the enemy (Enemy Health = 28).
   - Turn 2: Enemy deals 10 damage to the hero (Hero Health = 40).
   - Repeat until one combatant's health is zero or below.

4. **Outcome:**
   - If the hero wins, they advance to the next floor.
   - If defeated, their progress is logged.

## What’s Next?

Learn about the heroes' progression systems in the **[Evolution Intro](../evolution/1%20intro.md)** section or revisit the mechanics of the dungeon in the **[Dungeon Mechanics](1%20mechanics.md)**.

