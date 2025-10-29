class ArbolContagio:
    def __init__(self):
        self.arbol = {}   # infectador → lista de infectados
        self.raiz = None  # paciente cero

    def agregar_infeccion(self, infectador: str, infectado: str) -> None:
        if self.raiz is None:
            self.raiz = infectador

        if infectador not in self.arbol:
            self.arbol[infectador] = []
        if infectado not in self.arbol:
            self.arbol[infectado] = []

        self.arbol[infectador].append(infectado)

    def imprimir(self, persona: str = None, nivel: int = 0) -> None:
        if self.raiz is None:
            print("(Árbol vacío)")
            return
        if persona is None:
            persona = self.raiz

        print("   " * nivel + f"↳ {persona}")
        for hijo in self.arbol.get(persona, []):
            self.imprimir(hijo, nivel + 1)
