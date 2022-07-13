# Hilfsmittel-API

API des [GKV-Spitzenverbands](https://www.gkv-spitzenverband.de/) zu allen Hilfsmitteln, die unter die Leistungspflicht der Kassen fallen

## Struktur

Das Hilfsmittelregister unterscheidet zwischen 4 Ebenen:

1. Produktgruppe (z.B. *"01 - Absauggeräte"*)
2. Anwendungsort (z.B. *"24 - Atmungsorgane"*)
3. Untergruppe (z.B. *"01 - Sekret-Absauggeräte, netzabhängig"*)
4. Produktart (z.B. *"0 - Sekret-Absauggerät mit geringer Saugleistung, netzabhängig"*)

Einer Produktart sind dann letztendlich einzelne Produkte zugeordnet.

## x-Steller

Zusätzlich zu den verschiedenen IDs (die in der Regel UUIDs sind) haben alle Knoten im Baum noch einen x-Steller:

* **Produktgruppe**: Zweisteller (z.B. `01`)
* **Anwendungsort**: Viersteller (z.B. `01.24`)
* **Untergruppe**: Sechssteller (z.B. `01.24.01`)
* **Produktart**: Siebensteller (z.B. `01.24.01.0`)
* **Produkt**: Zehnsteller (z.B. `01.24.01.0002`)