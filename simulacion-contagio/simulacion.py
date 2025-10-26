import random
from typing import List, Optional, Dict, Tuple
from persona import Persona
from arbol import ArbolContagio  # 👈 nuevo import

class Simulacion:
    def __init__(self, n: int, total_personas: int, semilla: Optional[int] = None):
        if semilla is not None:
            random.seed(semilla)

        self.n = n
        self.ronda = 0
        self.arbol = ArbolContagio()
        self.personas: List[Persona] = []

        posiciones_ocupadas = set()
        while len(self.personas) < total_personas:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if (x, y) not in posiciones_ocupadas:
                nueva = Persona(f"p{len(self.personas)+1}", x, y)
                self.personas.append(nueva)
                posiciones_ocupadas.add((x, y))

        paciente_cero = random.choice(self.personas)
        paciente_cero.infectada = True
        self.arbol.padre[paciente_cero.id] = None
        self.paciente_cero = paciente_cero

    def mover_personas(self):
        for p in self.personas:
            dx, dy = random.choice(
                [(-1, 0), (1, 0), (0, -1), (0, 1),
                 (-1, -1), (-1, 1), (1, -1), (1, 1)]
            )
            p.x = (p.x + dx) % self.n
            p.y = (p.y + dy) % self.n

    def aplicar_infecciones(self):
        posiciones: Dict[Tuple[int, int], List[Persona]] = {}
        for p in self.personas:
            posiciones.setdefault((p.x, p.y), []).append(p)

        for grupo in posiciones.values():
            infectados = [p for p in grupo if p.infectada]
            sanos = [p for p in grupo if not p.infectada]
            if infectados:
                for s in sanos:
                    s.defensa -= len(infectados)
                    if s.defensa <= 0:
                        s.infectada = True
                        self.arbol.agregar_contagio(infectados[0].id, s.id)

    def curar(self, nombre: str):
        for p in self.personas:
            if p.id == nombre and p.infectada:
                p.infectada = False
                p.defensa = 3
                self.arbol.curar(nombre)

    def todas_infectadas(self) -> bool:
        return all(p.infectada for p in self.personas)
