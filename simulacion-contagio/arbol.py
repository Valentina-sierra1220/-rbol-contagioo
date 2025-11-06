from typing import Any, List, Optional

class Node:
    def __init__(self, valor: Any) -> None:
        self.valor = valor
        self.hijos: List["Node"] = []

    def __repr__(self) -> str:
        return f"{self.valor}"


class Tree:
    def __init__(self) -> None:
        self.raiz: Optional[Node] = None
    
    def agregar(self, valor: Any, padre: Optional[Any] = None) -> None:
        nuevo_nodo = Node(valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        if padre:
            nodo_padre = self._buscar(padre)
            if nodo_padre:
                nodo_padre.hijos.append(nuevo_nodo)
    
    def _buscar(self, objetivo: Any, actual: Optional[Node] = None) -> Optional[Node]:
        if actual is None:
            actual = self.raiz
        if actual is None:
            return None
        
        if objetivo == actual.valor:
            return actual
        
        for hijo in actual.hijos:
            buscado = self._buscar(objetivo, hijo)
            if buscado:
                return buscado
        
        return None

    def eliminar(self, objetivo: Any, actual: Optional[Node] = None) -> Optional[Node]:
        if actual is None:
            actual = self.raiz
        if actual is None:
            return None
        
        for i in range(len(actual.hijos)):
            if actual.hijos[i].valor == objetivo:
                nodo_objetivo = actual.hijos.pop(i)
                actual.hijos.extend(nodo_objetivo.hijos)
                return nodo_objetivo
        
        for hijo in actual.hijos:
            buscado = self.eliminar(objetivo, hijo)
            if buscado:
                return buscado
        return None

    def imprimir(self, actual: Optional[Node] = None, nivel: int = 0) -> None:
        if actual is None:
            actual = self.raiz
        if actual is None:
            print("(Árbol vacío)")
            return
        
        print("   " * nivel + f"↳ {actual.valor}")
        for hijo in actual.hijos:
            self.imprimir(hijo, nivel + 1)
            
