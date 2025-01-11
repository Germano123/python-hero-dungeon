class Dungeon:
    def __init__(self):
        self.floor = 1
        self.hero = None
        self.failed_heroes = []  # Lista para armazenar heróis derrotados

    def enter_dungeon(self, hero):
        """Faz o herói entrar na dungeon e lutar contra os monstros."""
        self.hero = hero
        print(f"{hero.name} entrou na dungeon!")

        while True:
            # Criar o monstro com base no nível do piso
            monster = Monster(self.floor)
            print(f"\nPiso {self.floor}: Um monstro de nível {monster.level} apareceu!")
            
            # Luta
            if not hero.fight(monster):
                # Se o herói perder, registramos os dados dele
                self.failed_heroes.append({
                    'hero_name': hero.name,
                    'level': hero.level,
                    'max_floor': hero.max_floor
                })
                print(f"{hero.name} foi derrotado no piso {self.floor}.")
                break

            # Se o herói vencer, sobe para o próximo piso
            hero.max_floor = self.floor
            self.floor += 1
