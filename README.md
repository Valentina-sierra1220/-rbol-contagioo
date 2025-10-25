# Simulación de Infección con Árbol de Contagio 🦠

## Descripción
Este proyecto simula la propagación de una infección en una matriz de tamaño NxN.  
Cada persona puede moverse aleatoriamente, perder defensa si se cruza con infectados, y contagiarse.  
Además, se lleva un *árbol de contagio* para registrar quién contagió a quién.  
Se pueden curar personas, agregar nuevas y visualizar el avance por rondas.

---

## 🔧 Requisitos
- Python 3.10 o superior
- No requiere librerías externas (solo random y typing)

---

## 🧩 Clases principales
### Persona
Representa a cada individuo del sistema.  
Atributos:
- id: Identificador único (p1, p2, …)  
- x, y: Posición actual en la matriz  
- defensa: Valor de resistencia  
- infectada: True si está infectada  
- infectador: Id del que lo contagió (o None)

### Simulacion
Controla la matriz, las rondas y las reglas.  
Atributos:
- N: Tamaño de la matriz  
- personas: Lista de objetos Persona  
- arbol: Diccionario {infectador: [infectados]}  
- ronda: Contador de rondas  

Funciones principales:
- agregar_persona(id, x, y)
- mover_personas()
- procesar_infeccion()
- curar(x, y)
- visualizar()

---

## ⚙️ Parámetros configurables
- Tamaño de la matriz N
- Defensa inicial (ej. 3)
- Regla de borde: “rebotar” o “toroide”
- Semilla aleatoria (random.seed(...))

---

## 🎮 Cómo ejecutar
1. Clona este repositorio  
   ```bash
   git clone https://github.com/tuusuario/simulacion-contagio.git
   cd simulacion-contagio
