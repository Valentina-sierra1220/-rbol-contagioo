###🧬 Simulación de Infección con Árbol de Contagio
**📖 Descripción**

Este proyecto implementa una simulación de contagio dentro de una matriz de tamaño N × N, donde cada persona se mueve aleatoriamente y puede contagiar a otras cuando coinciden en la misma posición.

El sistema mantiene un árbol de contagio que registra quién contagió a quién, permitiendo visualizar la cadena completa de infecciones.
Además, cada tres rondas las personas sanas recuperan 1 punto de defensa, representando su sistema inmunológico.

**🔧 Requisitos**
Python 3.10 o superior
No requiere librerías externas (solo random y typing, incluidas en Python)

**🧩 Clases principales**
🧍 Persona
Representa a cada individuo dentro de la simulación.

Atributos:
id: Identificador numérico (p1, p2, …)
x, y: Coordenadas dentro de la matriz
infectada: Estado de infección (True o False)
defensa: Nivel de resistencia (inicia en 3 por defecto)
infectador: ID de quién lo contagió (None si es paciente cero o sano)

Métodos:
infectar(id_infectador): Cambia su estado a infectado y registra quién lo contagió.
curar(): Restablece su estado a sano y reinicia su defensa.

🌳 Tree y Node
Estructura que guarda el historial de infecciones.

Atributos:
raiz: Nodo raíz (el paciente cero).
Node: Cada nodo representa una persona infectada y sus hijos, las personas que contagió.

Métodos:
agregar(valor, padre=None): Agrega un nuevo nodo (infectado) al árbol.
eliminar(valor): Elimina una persona (por ejemplo, si se cura).
imprimir(): Muestra el árbol completo en formato jerárquico.
Ejemplo de salida del árbol:

![Imagen de WhatsApp 2025-11-06 a las 19 17 09_540b39c0](https://github.com/user-attachments/assets/9ee67d87-bbad-4e67-b807-9fab708041dc)
---

###🧬 Simulacion
Clase principal que controla todo el sistema: movimiento, infección, defensas y rondas.

**Atributos:**
tamano: Tamaño de la matriz (N × N).
personas: Lista de objetos Persona.
arbol: Instancia del árbol de contagio (Tree).
ronda: Contador de rondas.

**Métodos principales:**
crear_personas(cantidad): Crea las personas y selecciona un paciente cero aleatorio.
mover_todas(): Desplaza a todas las personas una celda aleatoria (modo libre).
revisar_contagios(): Detecta contagios cuando dos personas coinciden en posición.
aumentar_defensas(): Recupera 1 punto de defensa cada 3 rondas.
siguiente_ronda(): Ejecuta una ronda completa (mover → infectar → curar si aplica).
curar(x, y): Cura a una persona infectada en una posición específica.
mostrar_matriz(): Imprime la matriz con las posiciones y colores (rojo infectado, verde sano).
mostrar_arbol(): Muestra el árbol de contagio actual.

**⚙️ Parámetros configurables**
Tamaño de la matriz (N)
Cantidad de personas
Defensa inicial (por defecto = 3)
Número de rondas a simular

Semilla aleatoria (random.seed(...)) para resultados reproducibles
---

## 🎮 Cómo ejecutar

1. **Clona o descarga** el repositorio  
   ```bash
   git clone https://github.com/Valentina-sierra1220/-rbol-contagioo.git
   cd simulacion-contagio

2. **Ejecuta el programa principal**
python main.py



