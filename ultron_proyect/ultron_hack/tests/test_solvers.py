import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ultron import solvers

# -------------------------------------------------------------------------
# TEST PROBLEMA 1: GEMAS DEL INFINITO
# -------------------------------------------------------------------------
def test_solve_problem_1_finds_stones():
    """Verifica que el algoritmo encuentra palabras en horizontal y vertical."""
    
    # Creamos una matriz falsa de prueba pequeña (3x3)
    # Escondemos "MIND" en horizontal y "SOUL" en vertical (cortado para el ejemplo)
    # Pero usemos algo que coincida con tu config.
    # Vamos a forzar una matriz donde sepamos qué hay.
    
    # Matriz simulada:
    # S P A C E  (Horizontal: SPACE)
    # O X X X X
    # U X X X X
    # L X X X X  (Vertical: SOUL)
    
    fake_data = {
        "size": 4,
        "matrix": [
            ["S", "P", "A", "C", "E"],
            ["O", "A", "B", "C", "D"],
            ["U", "E", "F", "G", "H"],
            ["L", "I", "J", "K", "L"],
        ]
    }
    
    result = solvers.solve_problem_1(fake_data)
    
    # Comprobaciones (Asserts)
    assert "SPACE" in result['solution'], "Debería encontrar SPACE en horizontal"
    assert "SOUL" in result['solution'], "Debería encontrar SOUL en vertical"
    assert len(result['solution']) >= 2


# -------------------------------------------------------------------------
# TEST PROBLEMA 2: SQL
# -------------------------------------------------------------------------
def test_solve_problem_2_returns_sql():
    """Verifica que devuelve 3 sentencias SQL y que son strings."""
    
    # No necesitamos datos de entrada reales
    result = solvers.solve_problem_2(None)
    
    solutions = result['solution']
    
    assert len(solutions) == 3, "Debe devolver exactamente 3 queries"
    assert "SELECT" in solutions[0], "La query A debe ser un SELECT"
    assert "HAVING" in solutions[1], "La query B debe tener un HAVING"
    assert "UPDATE" in solutions[2], "La query C debe ser un UPDATE"


# -------------------------------------------------------------------------
# TEST PROBLEMA 3: DIJKSTRA (RUTAS)
# -------------------------------------------------------------------------
def test_solve_problem_3_dijkstra_logic():
    """
    Verifica que el algoritmo elige la ruta más barata, no la más corta.
    Creamos un grafo triangular simple:
    Start -> A -> End (Camino largo pero barato)
    Start -> B -> End (Camino corto pero con Tormenta/Caro)
    """
    
    fake_satellites = {
        "satellites": [
            # NODO INICIO
            {"id": 1, "location": "Home", "weather": "Despejado", "nearest_sats": [2, 3]},
            
            # CAMINO A (Barato): Clima bueno. Coste = 10 (Base)
            {"id": 2, "location": "CaminoBarato", "weather": "Despejado", "nearest_sats": [4]},
            
            # CAMINO B (Caro): Tormenta (+2u). Coste = 10 + 2 = 12
            {"id": 3, "location": "CaminoCaro", "weather": "Tormenta", "nearest_sats": [4]},
            
            # NODO FIN
            {"id": 4, "location": "Target", "weather": "Despejado", "nearest_sats": []},
        ]
    }
    
    # Ejecutamos el solver
    result = solvers.solve_problem_3(fake_satellites, target_name="Target", start_name="Home")
    
    ruta = result['solution']
    fuel = result['final_fuel']
    
    # ANALISIS DE LA RUTA ESPERADA:
    # Home -> CaminoBarato -> Target
    # Coste: Home->Barato (10) + Barato->Target (10) = 20u de gasto.
    # Combustible final: 100 - 20 = 80u.
    
    # Si fuera por CaminoCaro: Home->Caro (12) + Caro->Target (10) = 22u de gasto.
    
    assert ruta == ["Home", "CaminoBarato", "Target"], "Dijkstra falló: No eligió la ruta más barata"
    assert fuel == 80.0, f"El combustible debería ser 80, calculado: {fuel}"