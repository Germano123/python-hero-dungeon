"""Realiza a luta contra um monstro."""
def fight(self, monster):
    print(f"{self.name} lutando contra o monstro de nível {monster.level}...")
    if self.level >= monster.level:
        exp_gained = monster.level
        print(f"{self.name} derrotou o monstro e ganhou {exp_gained} pontos de experiência!")
        self.gain_exp(exp_gained)
        return True
    else:
        print(f"{self.name} perdeu para o monstro!")
        return False
