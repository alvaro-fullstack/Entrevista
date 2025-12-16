🤖 Project Ultron: J.A.R.V.I.S. Access Protocol

Este repositorio contiene la solución técnica para la prueba de acceso al sistema J.A.R.V.I.S. El proyecto ha sido estructurado siguiendo principios de **Clean Code**, **Modularidad** y **Seguridad**.

El objetivo es resolver tres desafíos algorítmicos y de gestión de datos interactuando con una API REST externa.

## 📋 Requisitos Previos

* **Python 3.8+**
* **Git**

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto desde cero en tu máquina local.

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ultron_proyect
   ```

2. **Crear entorno virtual**
   - Para **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Para **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   Edita el archivo `.env` con la `API_URL` y tu `CANDIDATE_KEY`.
   ```env
   API_URL=xxxxx.com
   CANDIDATE_KEY=xxxxx
   ```

5. **Ejecutar código y pruebas (Testing)**
   ```bash
   python main.py
   python tests/mis_tests.py
   ```
   El resultado esperado debería ser similar a este:
   Probando Ejercicio 1: Sopa de Letras...
   [OK] Sopa de letras verificada.
.Probando Ejercicio 2: Queries SQL...
   [OK] Estructura SQL verificada.
.Probando Ejercicio 3: Algoritmo de Ruta...
   [OK] Ruta y combustible verificados.
.Probando Ejercicio 3: Caso imposible...
   [OK] Manejo de ruta inalcanzable correcto (no crashea).
.
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

Autor: Álvaro Muñoz Álvarez

Stack: Python, Requests, REST API, SQL, Dijkstra Algorithm.