# 🧬 Simulación de Infección con Árbol de Contagio

## 📖 Descripción
Este proyecto simula la propagación de una infección dentro de una matriz de tamaño **N × N**.  
Cada persona se mueve aleatoriamente en una de las 8 direcciones posibles (incluyendo diagonales).  
Cuando una persona infectada se cruza con una sana, la sana **pierde defensa** y, si su defensa llega a 0, **se contagia**.  

El sistema mantiene un **árbol de contagio** que registra **quién contagió a quién**, actualizándose en cada ronda.  
Cada tres rondas, las personas sanas **recuperan 1 punto de defensa**.

---

## 🔧 Requisitos
- Python **3.10 o superior**
- No requiere librerías externas  
  (solo `random` y `typing`, incluidas en Python)

---

## 🧩 Clases principales

### 🧍 Persona
Representa a cada individuo dentro de la simulación.  
**Atributos:**
- `nombre`: Identificador (p1, p2, …)  
- `x`, `y`: Coordenadas dentro de la matriz  
- `infectado`: Estado actual (True/False)  
- `defensa`: Nivel de resistencia (inicia en 3 por defecto)

**Métodos:**
- `mover(n)`: Se desplaza aleatoriamente una celda (modo toroide)  
- `__repr__()`: Muestra su estado con color (ROJO: infectado, VERDE: sano)

---

### 🌳 ArbolContagio
Estructura que guarda la historia de infección.  
**Atributos:**
- `raiz`: Paciente cero (primer infectado)  
- `arbol`: Diccionario con la forma `{infectador: [infectados]}`  

**Métodos:**
- `agregar_infeccion(infectador, infectado)`: Añade una conexión en el árbol  
- `imprimir()`: Muestra el árbol en formato jerárquico  


---

### 🧬 MatrizSimulacion
Controla toda la simulación (movimiento, infección y defensa).  
**Atributos:**
- `n`: Tamaño de la matriz  
- `personas`: Lista con todos los objetos `Persona`  
- `arbol`: Instancia del árbol de contagio  
- `ronda`: Contador de rondas

**Métodos:**
- `inicializar_personas(cantidad)`: Crea las personas y selecciona un paciente cero  
- `mover_todos()`: Desplaza a todas las personas en direcciones aleatorias  
- `procesar_infecciones()`: Revisa quién contagia a quién y actualiza el árbol  
- `ronda_simulacion()`: Ejecuta una ronda completa (mover, infectar, mostrar)  
- `mostrar()`: Imprime la matriz y el árbol de contagio actual

---

## ⚙️ Parámetros configurables
- Tamaño de la matriz (`N`)
- Cantidad de personas
- Defensa inicial (por defecto = 3)
- Regla de movimiento (modo *toroide*)
- Semilla aleatoria (`random.seed(...)`) para reproducir los resultados

---

## 🎮 Cómo ejecutar

1. **Clona o descarga** el repositorio  
   ```bash
   git clone https://github.com/Valentina-sierra1220/-rbol-contagioo.git
   cd simulacion-contagio

2. **Ejecuta el programa principal**
python main.py



