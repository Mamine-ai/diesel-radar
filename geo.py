import math

def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def dist_to_kehl_km(lat: float, lon: float) -> float:
    from config import KEHL_LAT, KEHL_LON
    return haversine_km(KEHL_LAT, KEHL_LON, lat, lon)

def in_study_region(lat: float, lon: float) -> bool:
    from config import RADIUS_KM
    return dist_to_kehl_km(lat, lon) <= RADIUS_KM
