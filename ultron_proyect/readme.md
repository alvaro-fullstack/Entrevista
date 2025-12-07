# 🤖 Project Ultron: J.A.R.V.I.S. Access Protocol

Este repositorio contiene la solución técnica para la prueba de acceso al sistema J.A.R.V.I.S. El proyecto ha sido estructurado siguiendo principios de **Clean Code**, **Modularidad** y **Seguridad**.

El objetivo es resolver tres desafíos algorítmicos y de gestión de datos interactuando con una API REST externa.

## 📋 Requisitos Previos

* **Python 3.8+**
* **Git**

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto desde cero en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd ultron_hack

### 2. Crear entorno virtual
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Crear dependencias
pip install -r requirements.txt

### 4. Editar el .env con la API_URL Y CANDIDATE_KEY
API_URL=[xxxxx.com)
CANDIDATE_KEY=xxxxx

### 5. Ejecución
python main.py

### Finalmete dejo una estructura del proyecto
ultron_hack/
│
├── main.py           # Punto de entrada. Orquesta la ejecución de los problemas.
├── config.py         # Gestión de configuración y variables de entorno.
├── client.py         # Capa de infraestructura. Maneja la comunicación HTTP con la API.
├── solvers.py        # Capa de lógica de negocio. Contiene los algoritmos de resolución.
├── .env              # (Ignorado por Git) Variables sensibles.
├── .gitignore        # Archivos excluidos del control de versiones.
└── requirements.txt  # Dependencias del proyecto.

### problemas enunciados
Problema 1: Búsqueda en Matriz (Gemas del Infinito)
Optimización: Se evitó el uso de bucles for anidados complejos mediante la transposición de la matriz (zip(*matrix)) y comprensión de listas.

Complejidad: Reducida al tratar filas y columnas como cadenas de texto continuas.

Problema 2: Consultas SQL (Vengadores)
Integridad: Se utilizaron JOIN explícitos en lugar de subconsultas en el SELECT.

Filtrado: Uso correcto de HAVING para filtrar datos agregados.

Seguridad en Updates: Uso de subconsultas en el WHERE para asegurar que solo se actualizan los registros correctos sin bucles externos.

Problema 3: Algoritmo de Rutas (Iron Man)
Algoritmo: Implementación de Dijkstra utilizando una cola de prioridad (heapq). Esto garantiza matemáticamente encontrar la ruta de menor coste de combustible.

Eficiencia: Uso de Hash Maps (Diccionarios) para convertir la búsqueda de nodos de O(n) a O(1).

Escalabilidad: Las penalizaciones climáticas se gestionan mediante un diccionario de configuración, eliminando estructuras condicionales anidadas (if/elif).

Autor: Álvaro Muñoz Álvarez

Stack: Python, Requests, REST API, SQL, Dijkstra Algorithm.