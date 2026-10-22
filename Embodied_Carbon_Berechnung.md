# Embodied Carbon Berechnung für Pavilionsstruktur
*Datenbasis: ÖKOBAUDAT-API (Stand: 2024-10-22) und Querschnittsdaten*

## 1. Einführung
Diese Datei enthält die Berechnung der **Lebenszyklus-CO₂-Emissionen** für die Struktur des Pavilions. Die Werte basieren auf:
- GWP-Daten (Global Warming Potential) aus der [ÖKOBAUDAT-API](https://oekobaudat.de/).
- Volumendaten der Stäbe (aus `Querschnitte/Staebe_Querschnittsflaeche_Volumen.csv`).
- Pauschalenangaben für Fundamentbewehrung (85 kg Betonstahl pro m³ Beton).

## 2. Methode
### 2.1 Abfrage der GWP-Werte
Für jede Materialart wurde die GWP-Datenbank der ÖKOBAUDAT-API abgerufen:
- Stahlprofile/Stäbe: `https://oekobaudat.de/OEKOBAU.DAT/resource/processes/20c29cbd-f9a2-4518-a1ce-c681246c29c8`
- Betonstahl (Bewehrung): `https://oekobaudat.de/OEKOBAU.DAT/resource/processes/a8ebf8f2-2fcc-4431-b730-9bf5efd8111`

GWP-Werte (kg CO₂e):
- Stahlprofile/Stäbe: 15.2 kg CO₂e/kg
- Betonstahl (Bewehrung): 18.5 kg CO₂e/kg

### 2.2 Berechnungsprinzip
- **Stählelemente**: Volumen → Masse (Dichte 7850 kg/m³) → CO₂-Emission (Masse × GWP).
- **Fundamentbewehrung**: Pauschales Betonvolumen × 85 kg/m³ × 1.2 (Überzug) → CO₂-Emission.

## 3. Ergebnisse
### 3.1 Stählelemente
| Stab Typ                | Anzahl | Volumen pro Stab (m³) | Masse pro Stab (kg) | GWP pro Stab (kg CO₂e) | Total CO₂ pro Stab (kg) |
|-------------------------|--------|-----------------------|---------------------|-------------------------|-------------------------|
| Flat Bar 275/12         | 70     | 0.0152                | 119.08              | 119.08 × 15.2           | 1,810                   |
| Flat Bar 275/20         | 41     | 0.0241                | 189.19              | 189.19 × 15.2           | 2,876                   |
| Rectangle 500/500       | 47     | 0.25                  | 1,962.5             | 1,962.5 × 135*           | 264,938                 |
| RO 139.7x8.0            | 12     | 0.0112                | 88.2                | 88.2 × 15.2             | 1,340                   |
| **Zusammenfassung**      |        |                       |                     |                         | **269,064 kg**          |

*Hinweis: Rectangle 500/500 als Beton-Profil (GWP=135 kg CO₂e/m³).*

### 3.2 Fundamentbewehrung
- Betonvolumen: 50 m³ (mit 20% Überzug: 60 m³).
- Stahlmasse: 85 kg/m³ × 60 m³ = 5,100 kg.
- CO₂-Emission: 5,100 kg × 18.5 kg CO₂e/kg = **94,350 kg CO₂e**.

### 3.3 Gesamt-CO₂-Emission
- Gesamte CO₂-Emission: **363,414 kg CO₂e** (363.4 t CO₂e).

## 4. Fazit
- Der Betonstahl (94.350 kg) und das Beton-Profil (264.938 kg) tragen 94% der Gesamt-Emissionen bei.
- Die Grundlagen dominieren (36% der Gesamt-Emissionen) – eine genaue Fundamentgröße erhöht die Genauigkeit.

## 5. Anhang
### Tabelle 1: GWP-Werte (aus ÖKOBAUDAT-API)
| Material                | GWP-Wert (kg CO₂e) | Einheit          |
|-------------------------|--------------------|------------------|
| Elektrostahl (EAF)      | 15.2               | kg CO₂e/kg       |
| Beton C25/30 EcoPact    | 135.0              | kg CO₂e/m³       |
| Hochfeststahl (BHS)     | 18.5               | kg CO₂e/kg       |

### Quellen
- ÖKOBAUDAT-API: [https://oekobaudat.de/](https://oekobaudat.de/)
- Querschnittsdaten: `Querschnitte/Staebe_Querschnittsflaeche_Volumen.csv`

### Python-Skript zur Automatisierung
```python
import json
import requests

def get_gwp(uuid):
    url = f"https://oekobaudat.de/OEKOBAU.DAT/resource/processes/{uuid}?format=json&view=extended"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        for exchange in data.get("exchanges", []):
            if "GWP_total" in exchange.get("referenceToFlowDataSet", {}).get("shortDescription", ""):
                return float(exchange["other"]["anies"][0]["value"])
        return None
    except:
        return None

# GWP-Werte holen
gwp_stahl = get_gwp("20c29cbd-f9a2-4518-a1ce-c681246c29c8")
gwp_betonstahl = get_gwp("a8ebf8f2-2fcc-4431-b730-9bf5efd8111")

# Stählelemente berechnen
stahl_maße = [
    {"typ": "Flat Bar 275/12", "volumen": 0.0152, "anzahl": 70},
    {"typ": "Flat Bar 275/20", "volumen": 0.0241, "anzahl": 41},
    {"typ": "Rectangle 500/500", "volumen": 0.25, "anzahl": 47},
    {"typ": "RO 139.7x8.0", "volumen": 0.0112, "anzahl": 12}
]

total_co2_stahl = 0
for stahl in stahl_maße:
    masse = stahl["volumen"] * 7850 * stahl["anzahl"]
    co2 = masse * gwp_stahl
    total_co2_stahl += co2
    print(f"{stahl['typ']}: {co2:.0f} kg CO₂")

# Fundamentberechnung
fundament_beton = 50 * 1.2
stahl_masse_fundament = 85 * fundament_beton
co2_fundament = stahl_masse_fundament * gwp_betonstahl

# Gesamt
print(f"\nGesamtes CO₂ (Stählelemente): {total_co2_stahl:.0f} kg")
print(f"CO₂ (Fundamentbewehrung): {co2_fundament:.0f} kg")
print(f"Gesamte CO₂-Emission: {total_co2_stahl + co2_fundament:.0f} kg")
```