# Projektauftrag: Diesel-Radar Oberrhein
Stand: 22.11.2026  · Version 1 · Ansprechpartner: Mohammed Laabidi


## Flotte (fiktive Beispieldaten aus Startkarte 1.1)
- 40 Lkw, je 120.000 km/Jahr, Verbrauch 33 l/100 km
- Diesel pro Lkw: 39.600 l/Jahr, Flotte gesamt: 1.584.000 l/Jahr
- Hebel: 1 ct/l Ersparnis = 15.840 €/Jahr

## Szenarien (Ersparnis pro Jahr, Hebel 15.840 € je ct/l)
- vorsichtig:  1 ct/l → 15.840 €
- Ziel:        3 ct/l → 47.520 €
- optimistisch: 5 ct/l → 79.200 €


## Kernfrage (ein Satz)
Wann und wo sollen unsere Fahrzeuge tanken, damit die Dieselkosten sinken,
ohne dass Touren länger werden?

## Entscheidung, die besser werden soll
Tankregel für Fahrer und Disposition: an welchen Tankstellen (DE/FR) und zu welcher Zeit getankt werden soll



## KPI
- Hauptkennzahl: Ø Dieselpreis bezahlt (ct/l), Ausgangswert: ca. 210 ct/l (Zeitraum: Stichprobe 21.11.2026, vorläufig – wird durch Ø der ersten 4 Wochen Zeitreihe ersetzt)
- Folgekennzahl: Dieselkosten €/100 km (Ausgangswert: 33 l × 2,10 €/l ≈ 69,30 €/100 km, vorläufig)
- Messung: automatisch über die Pipeline (fetch_prices → DuckDB → dbt), täglich aktualisiert

## Erfolg / Abbruch
- Erfolg: ≥ 3 ct/l Ersparnis ggü. Ausgangswert, entspricht ≥ 47.520 €/Jahr (Szenario "Ziel")
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
