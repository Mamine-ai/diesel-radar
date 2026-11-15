from pathlib import Path
from dotenv import load_dotenv
import os

ROOT = Path(__file__).parent
DATA = ROOT / "data"
RAW = DATA / "raw"
BRONZE = DATA / "bronze"
WAREHOUSE = ROOT / "warehouse.duckdb"

KEHL_LAT = 48.57
KEHL_LON = 7.81
RADIUS_KM = 30

START_DATE = "2025-01-01"

load_dotenv()

def get_secret(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise ValueError(f"Missing secret: {name}")
    return val
