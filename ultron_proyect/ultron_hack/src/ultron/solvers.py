from .config import INFINITY_STONES
from .config import WEATHER_PENALTIES, FUEL_CONSUMPTION_BASE, INITIAL_FUEL
import heapq

def solve_problem_1(data):
    """
    Resuelve el problema de la Sopa de Letras.
    Recibe: data (dict con 'matrix' y 'size')
    Retorna: dict con la solución formateada
    """
    matrix = data.get('matrix', [])
    found_stones = []
    
    # 1. Esto nos permite buscar palabras completas sin iterar celda por celda
    rows = ["".join(row) for row in matrix]
    
    # 2. Preparar las columnas: Transponemos la matriz
    cols = ["".join(col) for col in zip(*matrix)]
    
    # Unificamos todas las líneas de búsqueda
    all_lines = rows + cols
    
    # 3. Búsqueda eficiente
    for stone in INFINITY_STONES:
        # Verificamos si la gema está en alguna de las líneas
        # any() detiene la búsqueda en cuanto encuentra un True
        if any(stone in line for line in all_lines):
            found_stones.append(stone)
            
    return {"solution": found_stones}

def solve_problem_2(data):
    """
    Resuelve el problema de SQL.
    Aunque recibimos 'data' de la API, el enunciado nos pide queries estáticas
    basadas en el esquema proporcionado.
    """
    
    # Query A: Ubicaciones actuales con JOIN explícito
    query_a = (
        "SELECT l.name "
        "FROM avenger a "
        "JOIN location l ON a.current_location_id = l.id"
    )

    # Query B: Histórico > 3 veces usando GROUP BY y HAVING
    query_b = (
        "SELECT l.name "
        "FROM avenger_location_log log "
        "JOIN location l ON log.location_id = l.id "
        "GROUP BY log.avenger_id, l.name "
        "HAVING COUNT(*) > 3"
    )

    # Query C: Update masivo con subquery (evita hacer loops en código)
    query_c = (
        "UPDATE stark_satellite "
        "SET in_maintenance = 1 "
        "WHERE location_id IN (SELECT current_location_id FROM avenger)"
    )
    
    return {
        "solution": [query_a, query_b, query_c]
    }

def solve_problem_3(satellites_data, target_name, start_name="New York"):
    """
    Calcula la ruta óptima usando el algoritmo de Dijkstra.
    """
    satellites = satellites_data.get('satellites', [])
    
    # 1. Preprocesamiento: Crear mapas para acceso rápido O(1)
    id_map = {sat['id']: sat for sat in satellites}
    name_to_id = {sat['location']: sat['id'] for sat in satellites}
    
    start_id = name_to_id.get(start_name)
    target_id = name_to_id.get(target_name)
    
    if start_id is None or target_id is None:
        raise ValueError("Origen o Destino no encontrados en la red de satélites")

    
    # Iniciamos en el origen con coste 0
    pq = [(0.0, start_id, [start_name])]
    
    # visited guarda el menor coste conocido para llegar a un nodo
    visited_costs = {start_id: 0.0}
    
    final_path = []
    total_cost = 0.0
    
    while pq:
        current_cost, current_id, path = heapq.heappop(pq)
        
        # Si llegamos al destino, hemos encontrado la ruta más barata
        if current_id == target_id:
            final_path = path
            total_cost = current_cost
            break
            
        current_node = id_map[current_id]
        
        # Explorar vecinos
        for neighbor_id in current_node.get('nearest_sats', []):
            neighbor_node = id_map.get(neighbor_id)
            if not neighbor_node:
                continue
            
            # Cálculo del coste: Base + Clima del destino
            # Usamos .get() con default 0 para evitar IFs si el clima no está en la lista
            weather = neighbor_node.get('weather', '')
            penalty = WEATHER_PENALTIES.get(weather, 0.0)
            move_cost = FUEL_CONSUMPTION_BASE + penalty
            
            new_cost = current_cost + move_cost
            
            # Si encontramos un camino más barato, lo añado
            if neighbor_id not in visited_costs or new_cost < visited_costs[neighbor_id]:
                visited_costs[neighbor_id] = new_cost
                new_path = path + [neighbor_node['location']]
                heapq.heappush(pq, (new_cost, neighbor_id, new_path))
    
    # 3. Calcular combustible final
    final_fuel = INITIAL_FUEL - total_cost
    
    return {
        "solution": final_path,
        "final_fuel": final_fuel
    }