import requests
import sys
import solvers
import io
import os
from dotenv import load_dotenv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()

API_URL = os.getenv("API_URL")
CANDIDATE_KEY = os.getenv("CANDIDATE_KEY")

if not API_URL or not CANDIDATE_KEY:
    print("Error: No se encontraron las variables en el archivo .env")
    sys.exit(1)

HEADERS = {
    "candidate-key": CANDIDATE_KEY,
    "Content-Type": "application/json"
}

# API
def get_data(endpoint):
    try:
        resp = requests.get(f"{API_URL}/{endpoint}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"   [Error API] GET {endpoint}: {e}")
        return {}

def post_solution(endpoint, payload):
    try:
        url = f"{API_URL}/{endpoint}"
        resp = requests.post(url, headers=HEADERS, json=payload)
        return resp.json()
    except Exception as e:
        print(f"   [Error API] POST {endpoint}: {e}")
        return {}

def run():
    print(">>> Iniciando Protocolo Vengadores <<<\n")

    # --- PROBLEMA 1 ---
    print("1. Resolviendo Sopa de Letras...")
    data_p1 = get_data("problem/1")
    if data_p1:
        result_p1 = solvers.solve_word_search(data_p1)
        
        print(f"   -> Gemas encontradas: {result_p1['solution']}")
        
        api_resp = post_solution("problem/solution/1", result_p1)
        print(f"   Status: {api_resp}\n")

    # --- PROBLEMA 2 ---
    print("2. Generando Queries SQL...")
    get_data("problem/2")
    result_p2 = solvers.solve_sql_queries(None)
    api_resp = post_solution("problem/solution/2", result_p2)
    print(f"   Status: {api_resp}\n")

    # --- PROBLEMA 3 ---
    print("3. Calculando ruta de satélites...")
    map_data = get_data("problem/3")
    ironman_data = get_data("where_is_ironman")
    
    target_loc = ironman_data.get("ironman_location")
    
    if map_data and target_loc:
        print(f"   Destino: {target_loc}")
        
        result_p3 = solvers.solve_route(map_data, target_loc)
        
        if result_p3:
            fuel = result_p3['final_fuel']
            print(f"   -> Combustible final calculado: {fuel}")
            
            # Si el combustible es menor que 30, NO LLEGA
            if fuel < 30:
                print("   [!] COMBUSTIBLE INSUFICIENTE (Mínimo requerido: 30). No se puede realizar el viaje.")
            else:
                print("   [OK] Combustible suficiente. Iniciando viaje.")
                
            api_resp = post_solution("problem/solution/3", result_p3)
            print(f"   Status: {api_resp}")
        else:
            print("   [!] No se encontró ninguna ruta al destino.")
            
    else:
        print("   [Error] No se pudieron obtener datos del mapa o de Iron Man.")

if __name__ == "__main__":
    run()