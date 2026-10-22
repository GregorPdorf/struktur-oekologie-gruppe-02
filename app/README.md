# Embodied Carbon Visualisierung - Pavillon Stockerau

Interaktive 3D-Visualisierung der CO₂-Emissionen des Pavillon-Modells.

## Quick Start

```bash
cd app
python3 -m http.server 8080
```

Dann im Browser öffnen: **http://localhost:8080**

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `index.html` | Hauptanwendung (Three.js + UI) |
| `data.json` | Modell-Daten aus Rhino (~3.8 MB) |

## Datenquelle

Das 3D-Modell stammt aus der Rhino-Datei:
**Stockerau Rhino Export from RFEM.3dm**

561 BREP-Objekte (Volumenkörper) + 175 RD 12 Linien via Rhino MCP übertragen.

## Aktualisierung

Bei Änderungen am Rhino-Modell:
1. Mesh-Daten neu exportieren
2. `python3 app/create_data_json.py` ausführen
3. Seite im Browser aktualisieren

## Funktionen

- Materialvariante: Standard / Alternative umschalten
- Lebenszyklusmodul: A1-A3, C, D, Gesamt auswählen
- CO₂-Farbskala: Grün → Gelb → Orange → Rot (+ Lila für negative Werte)
- Klick auf Stab: Detailansicht mit CO₂-Werten
- Interaktives 3D: Drehen, Zoomen, Verschieben
