import random
from typing import List
from persona import Persona
from arbol_contagio import ArbolContagio

class MatrizSimulacion:
    def __init__(self, n: int, cantidad: int):
        self.n = n
        self.personas: List[Persona] = []
        self.arbol = ArbolContagio()
        self.ronda = 0
        self.inicializar_personas(cantidad)

    def inicializar_personas(self, cantidad: int):
        for i in range(cantidad):
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            self.personas.append(Persona(f"p{i+1}", x, y))

        paciente_cero = random.choice(self.personas)
        paciente_cero.infectado = True
        self.arbol.agregar_infeccion(paciente_cero.nombre, paciente_cero.nombre)

    def mover_todos(self):
        for p in self.personas:
            p.mover(self.n)

    def procesar_infecciones(self):
        posiciones = {}
        for p in self.personas:
            posiciones.setdefault((p.x, p.y), []).append(p)

        for celda, grupo in posiciones.items():
            infectados = [p for p in grupo if p.infectado]
            if infectados:
                for p in grupo:
                    if not p.infectado:
                        p.defensa -= len(infectados)
                        if p.defensa <= 0:
                            p.infectado = True
                            self.arbol.agregar_infeccion(infectados[0].nombre, p.nombre)

    def mostrar(self):
        print(f"\n--- RONDA {self.ronda} ---")
        matriz = [[" . " for _ in range(self.n)] for _ in range(self.n)]
        for p in self.personas:
            matriz[p.y][p.x] = str(p)
        for fila in matriz:
            print(" ".join(fila))

        print("\nÁrbol de contagio:")
        self.arbol.imprimir()

    def ronda_simulacion(self):
        self.ronda += 1
        self.mover_todos()
        self.procesar_infecciones()

        # Defensa especial cada 3 rondas
        if self.ronda % 3 == 0:
            for p in self.personas:
                if not p.infectado:
                    p.defensa += 1

        self.mostrar()
