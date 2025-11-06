import random
from simulacion import Simulacion


def main() -> None:
    print("=== Resident Evil UDEM ===\n")
    
    tamano = int(input("Tamaño matriz: "))
    cantidad = int(input("Número personas: "))
    
    usar_semilla = input("¿Usar semilla? (s/n): ")
    if usar_semilla.lower() == 's':
        semilla = int(input("Semilla: "))
        random.seed(semilla)
    
    sim = Simulacion(tamano, cantidad)
    
    while True:
        sim.mostrar_matriz()
        sim.mostrar_sanas()
        sim.mostrar_arbol()
        
        if sim.todas_infectadas():
            print("\n¡Todas infectadas! Fin.")
            break
        
        print("\n1. Siguiente ronda")
        print("2. Curar (x,y)")
        print("3. Agregar persona (x,y)")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            sim.siguiente_ronda()
        elif opcion == "2":
            x = int(input("x: "))
            y = int(input("y: "))
            if sim.curar(x, y):
                print("Curada!")
            else:
                print("No hay infectada ahí")
        elif opcion == "3":
            x = int(input("x: "))
            y = int(input("y: "))
            if sim.agregar_persona(x, y):
                print("Agregada!")
            else:
                print("No se puede")
        elif opcion == "4":
            break


if _name_ == "_main_":
    main()