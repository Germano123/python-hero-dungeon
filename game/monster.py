class Monster:
    def __init__(self, floor):
        """Cria um monstro com nível baseado no piso."""
        self.level = floor // 10 + random.randint(0, 5)  # O nível do monstro aumenta a cada 10 pisos.
