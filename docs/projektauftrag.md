# Projektauftrag: Diesel-Radar Oberrhein
Stand: 22.11.2026  · Version 2  · Ansprechpartner: Mohammed Laabidi
Änderungen V2: kernfrage (Umwege), Umwegkosten, Hypothesen widerlegbar, Ausgangswert, FR-Quelle


## Flotte (fiktive Beispieldaten aus Startkarte 1.1)
- 40 Lkw, je 120.000 km/Jahr, Verbrauch 33 l/100 km
- Diesel pro Lkw: 39.600 l/Jahr, Flotte gesamt: 1.584.000 l/Jahr
- Hebel: 1 ct/l Ersparnis = 15.840 €/Jahr

## Szenarien (Ersparnis pro Jahr, Hebel 15.840 € je ct/l)
- vorsichtig:  1 ct/l → 15.840 €
- Ziel:        3 ct/l → 47.520 €
- optimistisch: 5 ct/l → 79.200 €


## Kernfrage (ein Satz)
Wann und wo sollen unsere LKW im Raum Kehl/Strasbourg tanken, damit die Dieselkosten sinken, wobei ein Umweg nur erlaubt ist, wenn die Ersparnis größer ist als die Umwegkosten?

## Entscheidung, die besser werden soll
Tankregel für Fahrer und Disposition: an welchen Tankstellen (DE/FR) und zu welcher Zeit getankt werden soll



## KPI

- Hauptkennzahl: Ersparnis ggü. Markt (ct/l) = Marktpreis − bezahlter Preis

- Marktpreis: Ø Dieselpreis aller Stationen im Umkreis von 30 km um Kehl, im gleichen Zeitraum, ungewichtet

- Bezahlter Preis: Ø Dieselpreis der Flotte, gewichtet nach getankten Litern

- Ausgangswert: 0 ct/l (Annahme: Die Flotte tankt heute zum Marktdurchschnitt, fiktiv)

- Zusatzinfo: absoluter Ø-Preis Oktober 2026 (ca. 210 ct/l, historische Tankerkönig-Daten, Wert in M2)

- Messung: automatisch über die Pipeline (DuckDB → dbt), täglich aktualisiert




## Erfolg / Abbruch
- Erfolg: ≥ 3 ct/l Ersparnis unter Marktpreis, entspricht ≥ 47.520 €/Jahr (Szenario "Ziel")
- Abbruch: Datenabdeckung < 80 % oder Ersparnis < Umwegkosten
- Umwegkosten: 1 km Umweg ≈ 0,33 l ≈ 0,69 € Diesel (zzgl. Fahrerzeit)

## Scope
- Enthalten: Region 30 km um Kehl + Bas-Rhin, Diesel, 2025–2026
- Nicht enthalten: Routenplanung, Echtzeit-Alarm, andere Kraftstoffe

## Hypothesen (vorläufig)
- H1 (entscheidungsrelevant): Diesel ist abends (ca. 18–22 Uhr) günstiger als morgens → Tankzeit
- H2 (nachrangig): Diesel ist an bestimmten Wochentagen günstiger
- H3 (entscheidungsrelevant): Freie Tankstellen sind günstiger als große Marken → Stationswahl
- H4 (entscheidungsrelevant): Tanken in FR spart trotz Umweg → Land/Station

## Annahmen und Risiken
- Fahrer dürfen Tankstelle wählen: teilweise (nur Stationen nahe der Route); bei "nein" ist die Tankregel nicht umsetzbar
- Tankkarten-Rabatt: unbekannt, angenommen 0 ct/l (fiktiv); Risiko: Rabatt nur bei bestimmten Marken könnte die Ersparnis aufheben
- Datenquelle: Tankerkönig liefert nur DE-Preise; für H4 wird eine eigene Open-Data-Quelle für FR benötigt
- Säulenpreise ≠ bezahlte Preise (Rabatte, Rechnungsstellung)

## Termine
Durchstich: 13.12.2026 · Entscheidungsrunde: 24.01.2027 · Pilotende: 28.03.2027
