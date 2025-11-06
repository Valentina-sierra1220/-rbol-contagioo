import random
from typing import List, Optional, Tuple
from persona import Persona
from arbol import Tree


class Simulacion:
    def _init_(self, tamano: int, cantidad: int) -> None:
        self.tamano: int = tamano
        self.personas: List[Persona] = []
        self.arbol: Tree = Tree()
        self.ronda: int = 0
        
        self.crear_personas(cantidad)
    
    def crear_personas(self, cantidad: int) -> None:
        posiciones: List[Tuple[int, int]] = []
        
        for i in range(cantidad):
            while True:
                x = random.randint(0, self.tamano - 1)
                y = random.randint(0, self.tamano - 1)
                pos = (x, y)
                
                if pos not in posiciones:
                    posiciones.append(pos)
                    p = Persona(i + 1, x, y)
                    self.personas.append(p)
                    break
        
        infectado = random.randint(0, len(self.personas) - 1)
        self.personas[infectado].infectar(0)
        self.arbol.agregar(f"p{self.personas[infectado].id}")
    
    def mover_todas(self) -> None:
        movimientos = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        for p in self.personas:
            dx, dy = random.choice(movimientos)
            nuevo_x = p.x + dx
            nuevo_y = p.y + dy
            
            if 0 <= nuevo_x < self.tamano and 0 <= nuevo_y < self.tamano:
                p.x = nuevo_x
                p.y = nuevo_y
    
    def revisar_contagios(self) -> None:
        for i in range(len(self.personas)):
            if self.personas[i].infectada:
                continue
            
            for j in range(len(self.personas)):
                if i == j:
                    continue
                
                if self.personas[j].infectada:
                    if self.personas[i].x == self.personas[j].x and self.personas[i].y == self.personas[j].y:
                        self.personas[i].defensa -= 1
                        
                        if self.personas[i].defensa == 0:
                            self.personas[i].infectar(self.personas[j].id)
                            self.arbol.agregar(f"p{self.personas[i].id}", f"p{self.personas[j].id}")
    
    def aumentar_defensas(self) -> None:
        for p in self.personas:
            if not p.infectada:
                p.defensa += 1
    
    def siguiente_ronda(self) -> None:
        self.ronda += 1
        self.mover_todas()
        self.revisar_contagios()
        
        if self.ronda % 3 == 0:
            self.aumentar_defensas()
    
    def curar(self, x: int, y: int) -> bool:
        for p in self.personas:
            if p.x == x and p.y == y and p.infectada:
                self.arbol.eliminar(f"p{p.id}")
                p.curar()
                return True
        return False
    
    def agregar_persona(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.tamano or y < 0 or y >= self.tamano:
            return False
        
        for p in self.personas:
            if p.x == x and p.y == y:
                return False
        
        nuevo_id = len(self.personas) + 1
        nueva = Persona(nuevo_id, x, y)
        self.personas.append(nueva)
        return True
    
    def todas_infectadas(self) -> bool:
        for p in self.personas:
            if not p.infectada:
                return False
        return True
    
    def mostrar_matriz(self) -> None:
        matriz = [[" " for _ in range(self.tamano)] for _ in range(self.tamano)]
        
        for p in self.personas:
            if p.infectada:
                matriz[p.x][p.y] = f"\033[91mp{p.id}\033[0m"
            else:
                matriz[p.x][p.y] = f"\033[92mp{p.id}\033[0m"
        
        print(f"\nRonda {self.ronda}")
        for fila in matriz:
            for celda in fila:
                if celda == " ":
                    print("    ", end=" ")
                else:
                    print(f"{celda:4s}", end=" ")
            print()
    
    def mostrar_sanas(self) -> None:
        print("\nSanas:")
        hay_sanas = False
        for p in self.personas:
            if not p.infectada:
                print(f"  p{p.id}: defensa={p.defensa}")
                hay_sanas = True
        if not hay_sanas:
            print("  (ninguna)")
    
    def mostrar_arbol(self) -> None:
        print("\nÁrbol de contagio:")
        self.arbol.imprimir()
