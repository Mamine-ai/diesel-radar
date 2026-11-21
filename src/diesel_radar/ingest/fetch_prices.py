"""Phase 2.2 – Live-Dieselpreise von der Tankerkönig-API abrufen."""

import json
from datetime import datetime
from pathlib import Path

import httpx

from diesel_radar.config import RAW, get_secret

BASE_URL = "https://creativecommons.tankerkoenig.de/json"
CHUNK_SIZE = 10  # Die API erlaubt max. 10 Stations-IDs pro Anfrage


def load_station_ids(stations_file: Path) -> list[str]:
    """Liest die Stations-IDs aus stations.json."""
    with stations_file.open(encoding="utf-8") as f:
        data = json.load(f)

    # stations.json kann eine Liste sein oder ein Dict mit Schlüssel "stations"
    if isinstance(data, dict):
        data = data.get("stations", [])

    return [station["id"] for station in data]


def fetch_prices(station_ids: list[str], api_key: str) -> dict:
    """Fragt die aktuellen Preise ab – in Paketen à 10 IDs."""
    all_prices = {}

    for i in range(0, len(station_ids), CHUNK_SIZE):
        chunk = station_ids[i : i + CHUNK_SIZE]
        params = {"ids": ",".join(chunk), "apikey": api_key}

        response = httpx.get(f"{BASE_URL}/prices.php", params=params, timeout=10)
        response.raise_for_status()
        result = response.json()

        if result.get("ok"):
            all_prices.update(result.get("prices", {}))
        else:
            print(f"⚠️  Paket {i // CHUNK_SIZE + 1}: {result.get('message')}")

    return all_prices


def save_prices(prices: dict) -> Path:
    """Speichert die Rohdaten mit Zeitstempel (Datum + Uhrzeit)."""
    now = datetime.now()
    output_file = RAW / f"prices_{now:%Y-%m-%dT%H-%M}.json"

    payload = {
        "fetched_at": now.isoformat(timespec="seconds"),
        "station_count": len(prices),
        "prices": prices,
    }

    RAW.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_file


def main() -> None:
    api_key = get_secret("TANKERKOENIG_API_KEY")

    stations_file = RAW / "stations.json"
    if not stations_file.exists():
        raise SystemExit(f"❌ {stations_file} fehlt – zuerst fetch_stations ausführen")

    station_ids = load_station_ids(stations_file)
    print(f"📍 {len(station_ids)} Stationen geladen")

    prices = fetch_prices(station_ids, api_key)
    output_file = save_prices(prices)
    print(f"✅ {len(prices)} Preise gespeichert → {output_file}")


if __name__ == "__main__":
    main()
