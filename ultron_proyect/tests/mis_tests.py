# tests
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import solvers 

class TestVengadores(unittest.TestCase):

    # --- TEST EJERCICIO 1: SOPA DE LETRAS ---
    def test_problem_1_word_search(self):
        print("\nProbando Ejercicio 1: Sopa de Letras...")
        
        # Simulamos una matriz pequeña donde sabemos qué hay
        # 'SPACE' está en la fila 0
        # 'SOUL' está en la columna 0 (vertical)
        mock_data = {
            "matrix": [
                ["S", "P", "A", "C", "E"],
                ["O", "X", "X", "X", "X"],
                ["U", "X", "X", "X", "X"],
                ["L", "X", "X", "X", "X"]
            ]
        }
        
        result = solvers.solve_word_search(mock_data)
        found = result.get('solution', [])
        
        # Verificaciones
        self.assertIn("SPACE", found, "Debería encontrar SPACE (horizontal)")
        self.assertIn("SOUL", found, "Debería encontrar SOUL (vertical)")
        self.assertNotIn("REALITY", found, "No debería encontrar gemas que no están")
        print("   [OK] Sopa de letras verificada.")

    # --- TEST EJERCICIO 2: SQL ---
    def test_problem_2_sql(self):
        print("Probando Ejercicio 2: Queries SQL...")
        
        result = solvers.solve_sql_queries(None)
        queries = result.get('solution', [])
        
        # Verificamos que hay 3 queries
        self.assertEqual(len(queries), 3, "Deben devolverse exactamente 3 queries")
        
        # Verificamos palabras clave obligatorias
        self.assertIn("JOIN", queries[0].upper(), "La Query 1 debe tener un JOIN")
        self.assertIn("HAVING", queries[1].upper(), "La Query 2 debe usar HAVING")
        self.assertIn("UPDATE", queries[2].upper(), "La Query 3 debe ser un UPDATE")
        print("   [OK] Estructura SQL verificada.")

    # --- TEST EJERCICIO 3: RUTA (DIJKSTRA) ---
    def test_problem_3_dijkstra(self):
        print("Probando Ejercicio 3: Algoritmo de Ruta...")
        
        # Creamos un mapa falso muy simple:
        # New York -> Paris (Clima normal) -> Sokovia (Destino)
        # Coste base: 10. Clima normal: 0 penalización.
        # Ruta esperada: New York -> Paris -> Sokovia
        # Coste total: 10 (a Paris) + 10 (a Sokovia) = 20
        # Combustible final esperado: 100 - 20 = 80.0
        
        mock_map = {
            "satellites": [
                {
                    "id": 1, "location": "New York", 
                    "nearest_sats": [2], "weather": "Soleado"
                },
                {
                    "id": 2, "location": "Paris", 
                    "nearest_sats": [3], "weather": "Soleado" # Sin penalización
                },
                {
                    "id": 3, "location": "Sokovia", 
                    "nearest_sats": [], "weather": "Soleado"
                }
            ]
        }
        
        target = "Sokovia"
        
        result = solvers.solve_route(mock_map, target)
        
        # 1. Verificar ruta
        expected_path = ["New York", "Paris", "Sokovia"]
        self.assertEqual(result['solution'], expected_path, "La ruta calculada no es la óptima")
        
        # 2. Verificar combustible
        # Si tu código usa el round(..., 2) que pusimos, debería dar 80.0 exacto
        self.assertEqual(result['final_fuel'], 80.0, f"El combustible debería ser 80.0, dio {result['final_fuel']}")
        print("   [OK] Ruta y combustible verificados.")

    def test_problem_3_insufficient_fuel(self):
        print("Probando Ejercicio 3: Caso imposible...")
        
        # Caso donde el destino está inalcanzable (sin conexiones)
        mock_map_broken = {
            "satellites": [
                {"id": 1, "location": "New York", "nearest_sats": []}, # Sin vecinos
                {"id": 99, "location": "Mars", "nearest_sats": []}
            ]
        }
        
        # Debería devolver la ruta vacía, None, o combustible original, depende de tu lógica.
        # Según tu código actual, si no hay ruta, devuelve un dict vacío o la lista vacía.
        # Asumiremos que tu lógica de Dijkstra no crashea.
        try:
            solvers.solve_route(mock_map_broken, "Mars")
            print("   [OK] Manejo de ruta inalcanzable correcto (no crashea).")
        except Exception as e:
            self.fail(f"El código falló buscando una ruta imposible: {e}")

if __name__ == '__main__':
    unittest.main()