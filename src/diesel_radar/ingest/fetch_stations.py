import json

import httpx

from diesel_radar.config import RAW, get_secret


def fetch_stations() -> list[dict]:
    """Tankstellen im Umkreis von Kehl abrufen."""
    api_key = get_secret("TANKERKOENIG_API_KEY")
    url = (
        "https://creativecommons.tankerkoenig.de/json/list.php"
        f"?lat=48.57&lng=7.81&rad=30&sort=dist&type=all&apikey={api_key}"
    )
    response = httpx.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    stations = data.get("stations", [])
    print(f"✅ {len(stations)} Tankstellen gefunden")
    return stations


if __name__ == "__main__":
    RAW.mkdir(parents=True, exist_ok=True)
    stations = fetch_stations()
    out = RAW / "stations.json"
    out.write_text(json.dumps(stations, indent=2, ensure_ascii=False))
    print(f"💾 Gespeichert: {out}")
