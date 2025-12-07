import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
CANDIDATE_KEY = os.getenv("CANDIDATE_KEY")

if not API_URL or not CANDIDATE_KEY:
    raise ValueError("Faltan variables de entorno (.env)")

HEADERS = {
    "candidate-key": CANDIDATE_KEY,
    "Content-Type": "application/json"
}



# Constantes del Problema 1
INFINITY_STONES = ["SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"]

# Problema 3: Penalizaciones de Clima
WEATHER_PENALTIES = {
    "Viento en contra": 1.5,
    "Lluvia": 0.2,
    "Tormenta": 2.0,
    # Cualquier otro clima asumiremos 0
}

FUEL_CONSUMPTION_BASE = 10.0
INITIAL_FUEL = 100.0