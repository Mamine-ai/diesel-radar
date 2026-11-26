# Projektauftrag: Diesel-Radar Oberrhein
Stand: 26.11.2026  · Version 2  · Ansprechpartner: Mohammed Laabidi
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
- Umwegkosten = 2 × Umweg-km × 0,33 l × Dieselpreis + Umwegzeit × Fahrer-Stundensatz (35 €/h, fiktiv)
- Beispiel Strasbourg: 5 km Umweg → 10 km × 0,33 l × 2,10 € = 6,93 € + 15 min × 35 €/h = 8,75 € → 15,68 € pro Tankstopp
- Break-even: 15,68 € ÷ 500 l ≈ 3,1 ct/l (ab diesem Preisvorteil lohnt sich der Umweg)

## Scope
- Enthalten: Region 30 km um Kehl + Bas-Rhin, Diesel, 2025–2026
- Nicht enthalten: Routenplanung, Echtzeit-Alarm, andere Kraftstoffe

## Hypothesen (vorläufig)
- H1 (entscheidungsrelevant → Tankzeit): Es gibt eine Tageszeit, zu der Diesel im Ø mind. 3 ct/l günstiger ist als der Tagesdurchschnitt. Widerlegt, wenn der größte Unterschied < 3 ct/l.
- H2 (nachrangig): An bestimmten Wochentagen ist Diesel im Ø mind. 2 ct/l günstiger. Widerlegt, wenn der Unterschied zwischen Wochentagen < 2 ct/l.
- H3 (entscheidungsrelevant → Stationswahl): Freie Tankstellen sind im Ø mind. 2 ct/l günstiger als Markentankstellen. Widerlegt, wenn der Unterschied < 2 ct/l.
- H4 (entscheidungsrelevant → Land/Station): Tanken in FR (Strasbourg) lohnt sich trotz Umweg. Widerlegt, wenn der Ø-Preisvorteil FR kleiner ist als der Break-even (≈ 3,1 ct/l).

## Annahmen und Risiken
- Fahrer dürfen Tankstelle wählen: teilweise (nur Stationen nahe der Route); bei "nein" ist die Tankregel nicht umsetzbar
- Tankkarten-Rabatt: unbekannt, angenommen 0 ct/l (fiktiv); Risiko: Rabatt nur bei bestimmten Marken könnte die Ersparnis aufheben
- Datenquelle DE: Tankerkönig (Live-API + historische Daten)
- Datenquelle FR: Prix des carburants (offene Daten der franz. Regierung), Lizenz: Licence Ouverte 2.0
- Fahrer-Stundensatz: 35 €/h (fiktiv, Annahme)
- Säulenpreise ≠ bezahlte Preise (Rabatte, Rechnungsstellung)
- 500 l pro Tankstopp
## Termine
Durchstich: 13.12.2026 · Entscheidungsrunde: 24.01.2027 · Pilotende: 28.03.2027
