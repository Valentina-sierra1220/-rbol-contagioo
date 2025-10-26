from typing import Dict, List, Optional

class ArbolContagio:
    def __init__(self):
        self.padre: Dict[str, Optional[str]] = {}  
        self.hijos: Dict[str, List[str]] = {}      

    def agregar_contagio(self, infectador: str, nuevo: str):
        self.padre[nuevo] = infectador
        if infectador not in self.hijos:
            self.hijos[infectador] = []
        self.hijos[infectador].append(nuevo)

    def curar(self, persona: str):
        if persona not in self.padre:
            return
        infectador = self.padre[persona]
        for hijo in self.hijos.get(persona, []):
            self.padre[hijo] = infectador
            if infectador:
                self.hijos[infectador].append(hijo)
        self.hijos.pop(persona, None)
        self.padre.pop(persona, None)

    def mostrar(self):
        print("🧾 Árbol de contagio:")
        if not self.padre:
            print("(Vacío)")
            return

        def mostrar_rama(nombre: str, prefijo: str = ""):
            print(prefijo + nombre)
            for hijo in self.hijos.get(nombre, []):
                mostrar_rama(hijo, prefijo + "  ")

        for r in self.padre:
            if self.padre[r] is None:
                mostrar_rama(r)
