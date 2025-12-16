import heapq

# Constantes
INFINITY_STONES = ["SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"]
FUEL_BASE = 10.0
INITIAL_FUEL = 100.0

def solve_word_search(data):
    matrix = data.get('matrix', [])
    found = []
    
    rows = ["".join(r) for r in matrix]
    cols = ["".join(c) for c in zip(*matrix)]
    search_space = rows + cols
    
    for stone in INFINITY_STONES:
        for line in search_space:
            if stone in line:
                found.append(stone)
                break
            
    return {"solution": found}

def solve_sql_queries(_):
    q1 = "SELECT l.name FROM avenger a JOIN location l ON a.current_location_id = l.id"
    q2 = """
    SELECT l.name 
    FROM avenger_location_log log 
    JOIN location l ON log.location_id = l.id 
    GROUP BY log.avenger_id, l.name 
    HAVING COUNT(*) > 3
    """
    q3 = "UPDATE stark_satellite SET in_maintenance = 1 WHERE location_id IN (SELECT current_location_id FROM avenger)"
    return {"solution": [q1, q2.strip(), q3]}

def solve_route(data, target_node):
    satellites = data.get('satellites', [])
    start_node = "New York"
    
    sats_by_id = {s['id']: s for s in satellites}
    id_by_name = {s['location']: s['id'] for s in satellites}
    
    start_id = id_by_name.get(start_node)
    target_id = id_by_name.get(target_node)
    
    if not start_id or not target_id:
        return None

    # Dijkstra
    pq = [(0.0, start_id, [start_node])]
    visited = {} 
    
    weather_penalties = {
        "Viento en contra": 1.5,
        "Lluvia": 0.2,
        "Tormenta": 2.0
    }

    final_path = []
    total_cost = 0.0

    while pq:
        cost, u_id, path = heapq.heappop(pq)
        
        if u_id in visited and visited[u_id] <= cost:
            continue
        visited[u_id] = cost

        if u_id == target_id:
            final_path = path
            total_cost = cost
            break
        
        u_node = sats_by_id[u_id]
        for v_id in u_node.get('nearest_sats', []):
            v_node = sats_by_id.get(v_id)
            if not v_node: continue
            
            w_penalty = weather_penalties.get(v_node.get('weather'), 0.0)
            edge_weight = FUEL_BASE + w_penalty
            
            # Redondeamos 
            new_cost = round(cost + edge_weight, 2)
            
            if v_id not in visited or new_cost < visited[v_id]:
                heapq.heappush(pq, (new_cost, v_id, path + [v_node['location']]))

    # Cálculo final
    remaining_fuel = INITIAL_FUEL - total_cost
    
    return {
        "solution": final_path,
        "final_fuel": round(remaining_fuel, 2) # Forzamos 2 decimales
    }