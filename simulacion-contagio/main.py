import random
from matriz import MatrizSimulacion

def main():
    random.seed(42)
    n = int(input("Tamaño de la matriz: "))
    cant = int(input("Número de personas: "))
    sim = MatrizSimulacion(n, cant)

    while True:
        sim.ronda_simulacion()
        if all(p.infectado for p in sim.personas):
            print("\n💀 Todos están infectados. Fin de la simulación.")
            break
        cont = input("\nPresiona ENTER para continuar o 'x' para salir: ")
        if cont.lower() == "x":
            break

if __name__ == "__main__":
    main()
