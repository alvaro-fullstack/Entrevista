import requests
from .config import API_URL, HEADERS

def get_problem(problem_id):
    """Obtiene los datos del problema desde la API."""
    url = f"{API_URL}/problem/{problem_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status() # Lanza error si la petición falla (4xx, 5xx)
    return response.json()

def submit_solution(problem_id, solution_data):
    """Envía la solución a la API y devuelve el resultado."""
    url = f"{API_URL}/problem/solution/{problem_id}"
    response = requests.post(url, headers=HEADERS, json=solution_data)
    
    # Retornamos el JSON directamente para ver si fue correcto o no
    return response.json()

def get_ironman_location():
    """Consulta la ubicación actual de Iron Man."""
    url = f"{API_URL}/where_is_ironman"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    # La respuesta es {"ironman_location": "Sokovia"}
    return response.json().get("ironman_location")