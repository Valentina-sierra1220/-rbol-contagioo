import random
from typing import Tuple

class Persona:
    def __init__(self, nombre: str, x: int, y: int, infectado: bool = False, defensa: int = 3):
        self.nombre: str = nombre
        self.x: int = x
        self.y: int = y
        self.infectado: bool = infectado
        self.defensa: int = defensa

    def mover(self, n: int) -> None:
        """Mueve a la persona una posición aleatoria (modo toroide)."""
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x = (self.x + dx) % n
        self.y = (self.y + dy) % n

    def __repr__(self) -> str:
        color = "🟥" if self.infectado else "🟩"
        return f"{color}{self.nombre}({self.defensa})"


    