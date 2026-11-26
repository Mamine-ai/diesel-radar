# Entscheidungsprotokoll (Decision Log)

## 001 – Projektauftrag Version 2 freigegeben
- Datum: 24.11.2026
- Status: angenommen
- Kontext: Version 1 enthielt Tippfehler, einen Widerspruch (Kernfrage vs. H4), nicht widerlegbare Hypothesen und einen Ausgangswert aus nur einem Tag.
- Entscheidung: Projektauftrag wird als Version 2 überarbeitet und freigegeben.
- Alternativen: Version 1 behalten und Fehler später korrigieren (verworfen: Fehler hätten die Analyse verfälscht).
- Folgen: Die Pipline muss zusätzlich den Marktpreis berchnen: den ungewichteten  Ø-Dieselpreis aller Stationen im Umkreis von 30 km um Kehl, im selben Zeitraum wie der bezahlte Preis. Die Flottendaten sind fiktiv, deshalb gilt der Ausgangswert 0 ct/l als Annahme (Flotte tankt zum Marktdurchschnitt), bis echte Tankdaten vorliegen

- Wer: Auftraggeber





## 002 – KPI wird relativ zum Marktdurchschnitt gemessen
- Datum: 22.11.2026
- Status: angenommen

- Kontext: Der Dieselpreis hängt stark vom Ölpreis ab, auf den die Flotte keinen Einfluss hat. Würde man den bezahlten Preis mit einem festen früheren Wert (z. B. Oktober 2026) vergleichen, könnte ein fallender Ölpreis einen Erfolg vortäuschen und ein steigender Ölpreis einen Misserfolg.

- Entscheidung: Die Ersparnis wird als Marktpreis minus bezahlter Preis im gleichen Zeitraum gemessen (in ct/l). Marktpreis = Ø aller Stationen im Umkreis von 30 km um Kehl (ungewichtet), bezahlter Preis = Ø der Flotte (gewichtet nach Litern). Ausgangswert 0 ct/l, Erfolg ab 3 ct/l unter Markt.

- Alternativen:
  - Absoluter Preis vs. Oktober 2026: verworfen, weil Ölpreis-Schwankungen das Ergebnis verfälschen.
  - Vergleich mit dem Vormonat: verworfen, weil der Vergleichswert mitwandert und die Ersparnis mit der Zeit immer kleiner erscheint.
  - Vergleich mit dem Vorjahresmonat: verworfen, weil Ölpreis und Marktlage ein Jahr später ganz anders sein können.


  - Folgen: docs/projektauftrag.md ist die verbindliche Grundlage für alle weiteren Schritte.
- Wer: Auftraggeber
