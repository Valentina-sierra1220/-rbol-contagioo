import random
from typing import Optional, List, Tuple


class Persona:
    def _init_(self, id: int, x: int, y: int) -> None:
        self.id: int = id
        self.x: int = x
        self.y: int = y
        self.infectada: bool = False
        self.defensa: int = 3
        self.infectador: Optional[int] = None
    
    def infectar(self, id_infectador: int) -> None:
        self.infectada = True
        self.infectador = id_infectador
    
    def curar(self) -> None:
        self.infectada = False
        self.infectador = None
        self.defensa = 3


    