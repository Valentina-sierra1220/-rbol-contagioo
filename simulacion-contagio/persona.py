from typing import Optional

class Persona:
    def _init_(self, id: str, x: int, y: int, defensa: int = 3):
        self.id = id
        self.x = x
        self.y = y
        self.defensa = defensa
        self.infectada = False
        self.infectador: Optional[str] = None

    def _repr_(self):
        estado = "rojo" if self.infectada else "verde"
        return f"{estado}{self.id}"