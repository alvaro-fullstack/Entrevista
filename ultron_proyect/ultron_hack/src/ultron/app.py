from . import client
from . import solvers
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'utf-8')

def run_problem_1():

    print("--- Iniciando Problema 1: Gemas del Infinito ---")
    
    try:
        # 1. Obtener datos
        problem_data = client.get_problem(1)
        print(f"Matriz recibida de tamaño: {problem_data.get('size')}")
        
        # 2. Calcular solución
        solution = solvers.solve_problem_1(problem_data)
        print(f"Solución calculada: {solution}")
        
        # 3. Enviar solución
        result = client.submit_solution(1, solution)
        print(f"Respuesta de J.A.R.V.I.S.: {result}")
        
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

def run_problem_2():
    print("\n--- Iniciando Problema 2: SQL Vengadores ---")
    try: 
        # el protocolo dice: GET problem -> POST solution
        client.get_problem(2) 
        print("Enunciado del problema 2 recibido.")
        
        # Calculamos solución (en este caso, generar las strings SQL)
        solution = solvers.solve_problem_2(None) 
        
        print("Enviando soluciones SQL...")
        result = client.submit_solution(2, solution)
        print(f"Respuesta de J.A.R.V.I.S.: {result}")
        
    except Exception as e:
        print(f"Error en Problema 2: {e}")

def run_problem_3():
    print("\n--- Iniciando Problema 3: Ruta a Iron Man ---")
    try:
        # 1. Obtener la red de satélites
        print("Obteniendo mapa de satélites...")
        problem_data = client.get_problem(3)
        
        # 2. Obtener dónde está Iron Man
        target_location = client.get_ironman_location()
        print(f"Iron Man localizado en: {target_location}")
        
        # 3. Calcular Ruta Óptima (Dijkstra)
        result_data = solvers.solve_problem_3(problem_data, target_location)
        result_data['final_fuel'] = round(result_data['final_fuel'], 2)
        
        print(f"Ruta calculada: {result_data['solution']}")
        print(f"Combustible restante: {result_data['final_fuel']}")
        
        # 4. Enviar solución
        api_response = client.submit_solution(3, result_data)
        print(f"Respuesta de J.A.R.V.I.S.: {api_response}")

    except Exception as e:
        print(f"Error crítico en la misión: {e}")
        # Importante imprimir el error completo para debuggear si falla
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_problem_1()
    run_problem_2()
    run_problem_3()
