import random
from persona import Persona

def crear_matriz(n):
    return [[" . " for _ in range(n)] for _ in range(n)]

def mostrar_matriz(matriz):
    for fila in matriz:
        print("".join(fila))

def mover_persona(persona, n):
    direcciones = [
        (-1, 0), 
        (1, 0),   
        (0, -1), 
        (0, 1)    
    ]

    dx, dy = random.choice(direcciones)
    nueva_x = persona.x + dx
    nueva_y = persona.y + dy

    if 0 <= nueva_x < n and 0 <= nueva_y < n:
        persona.x = nueva_x
        persona.y = nueva_y

def colocar_persona_en_matriz(matriz, persona):
  
    matriz[persona.x][persona.y] = f"🟥{persona.id}" if persona.infectada else f"🟩{persona.id}"


if __name__ == "__main__":
    n = int(input("Tamaño de la matriz: "))


    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    persona = Persona("p1", x, y)

    print("\n➡️ Estado inicial:")
    matriz = crear_matriz(n)
    colocar_persona_en_matriz(matriz, persona)
    mostrar_matriz(matriz)

  
    mover_persona(persona, n)

    print("\n➡️ Después de moverse:")
    matriz = crear_matriz(n)
    colocar_persona_en_matriz(matriz, persona)
    mostrar_matriz(matriz)
