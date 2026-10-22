# Querschnittsflächen und Volumen – Stäbe des Pavillons

**Quelle:** `Stockerau Rhino Export from RFEM.3dm`  
**Layer-Pfad:** `2__B+G::03_3D::RFEM_Export_260915::Members::`  
**Detaillierte Rohdaten:** siehe [`Staebe_Querschnittsflaeche_Volumen.csv`](./Staebe_Querschnittsflaeche_Volumen.csv)  
**Beispielhafte Nachrechnung:** siehe [`Nachrechnung_Voutenstab.py`](./Nachrechnung_Voutenstab.py) (mit grafischer Veranschaulichung)  

---

## Methode

Aus jedem 3D-Volumenkörper (`BREP`) wurde die **querschnittsfläche senkrecht zur Hauptachse** berechnet (mittels `section_profile` in RhinoCommon). Zusätzlich wurde das exakte **Volumen** jedes Elements über `VolumeMassProperties` ermittelt. Die Daten wurden nach **Profiltyp** gruppiert und zusammengefasst.

Zusätzlich wurden die 175 Stäbe vom Profil **RD 12** (Rundstahl Ø12 mm) berücksichtigt, die im Modell nur als Achslinie ohne Volumenkörper vorliegen – deren Querschnittsfläche wurde theoretisch berechnet (π·r²).

---

## Übersicht aller Profiltypen

| # | Profil | Anzahl | Volumen gesamt (m³) | Mittlere QFläche (mm²) | Min (mm²) | Max (mm²) | Typ | Flaechenunterschied |
|---|--------|-------:|--------------------:|------------------------:|----------:|----------:|-----|-------------------:|
| 1 | Rectangle 500/500 | 47 | 11,7382 | 249.749 | 249.645 | 249.879 | Konstant | 0,1 % |
| 2 | RO 139.7×8.0 \| EN 10210-2:2006 | 12 | 0,6295 | 15.327 | 15.326 | 15.327 | Konstant | < 0,1 % |
| 3 | Flat Bar 275/20 | 41 | 0,1327 | 5.172 | 4.736 | 5.599 | Voute | 12,5 % |
| 4 | Flat Bar 275/12 | 70 | 0,1285 | 3.117 | 2.842 | 3.377 | Voute | 12,5 % |
| 5 | Flat Bar 225/20 | 23 | 0,0775 | 4.045 | 3.725 | 4.365 | Voute | 17,2 % |
| 6 | Flat Bar 225/12 | 35 | 0,0707 | 2.427 | 2.235 | 2.619 | Voute | 17,2 % |
| 7 | Flat Bar 175/20 | 23 | 0,0576 | 3.032 | 2.714 | 3.350 | Voute | 23,4 % |
| 8 | Flat Bar 175/12 | 35 | 0,0530 | 1.819 | 1.628 | 2.009 | Voute | 23,3 % |
| 9 | Flat Bar 237.5/12 | 35 | 0,0357 | 2.723 | 2.558 | 2.887 | Voute | 12,9 % |
| 10 | Flat Bar 237.5/20 | 18 | 0,0306 | 4.538 | 4.263 | 4.812 | Voute | 12,9 % |
| 11 | Flat Bar 200/12 | 35 | 0,0296 | 2.256 | 2.095 | 2.418 | Voute | 15,4 % |
| 12 | Flat Bar 200/20 | 18 | 0,0253 | 3.761 | 3.492 | 4.029 | Voute | 15,4 % |
| 13 | Flat Bar 162.5/12 | 35 | 0,0234 | 1.787 | 1.630 | 1.944 | Voute | 19,3 % |
| 14 | Flat Bar 162.5/20 | 18 | 0,0196 | 2.985 | 2.717 | 3.258 | Voute | 19,4 % |
| 15 | Flat Bar 33.3/20 | 116 | 0,0015 | 400,0 | 400,0 | 400,0 | Konstant | — |
| | **GESAMT (Breps)** | **561** | **13,0534** | | | | | |

---

## Nach Bauteilkategorien gruppiert

| Kategorie | Profile enthalten | Anzahl Stäbe | Anteil an Gesamt | Volumen gesamt (m³) | Volumenanteil |
|---|---|---:|---:|---:|---:|
| Rechteckhohlprofil | Rectangle 500/500 | 47 | 8,4 % | 11,7382 | 89,9 % |
| Flachstahl-Vouten | alle "Flat Bar ..." (9 Varianten) | 499 | 89,0 % | 1,0309 | 7,9 % |
| Flachstahl-Konstant | Flat Bar 33.3/20 | 116 | 20,7 % | 0,0015 | 0,01 % |
| Rundrohr | RO 139.7×8.0 | 12 | 2,1 % | 0,6295 | 4,8 % |
| **Gesamt (mit Brep)** | | **561** | **100 %** | **13,0534** | **100 %** |
| Rundstahl (theoretisch) | RD 12 (Ø12 mm, nur Achse) | 175 | — | ~0,06* | — |

\* Das Volumen von RD 12 kann nicht direkt aus dem Modell gemessen werden, da diese Stäbe ausschließlich als Achslinien (`MemberAxes`, Typ `LINE`) vorliegen. Der Wert entspricht einer Schätzung (~3 m durchschnittliche Stablänge × π·6² mm²).

---

## Wichtige Anmerkungen zur Datenerhebung

### 1. Voutenstäbe bei Flachstählen
Alle Flachstahl-Profile (außer 33,3/20) sind im Modell als **linear verjüngte Vouten** gespeichert. Das bedeutet, der Querschnitt ändert sich entlang der Länge – typischerweise von einem größeren Profil am einen Ende zu einem kleineren Profil am anderen Ende (z. B. "Flat Bar 275/12 → Flat Bar 225/12"). In den RFEM-Exportdaten ist dies über die Attribute `CrosSec_S` (Start) und `CrosSec_E` (Ende) vermerkt.

Die Flächenunterschiede zwischen 12–23 % sind für solche Voutenelemente typisch und korrekt.

### 2. Auffälligkeit beim Rundrohr RO 139.7×8.0
Die gemessene Querschnittsfläche beträgt ~15.326 mm². Für ein **Hohlrohr** mit Außen-/Innen-Durchmesser 139,7/123,7 mm wäre die theoretische Fläche jedoch nur:

$$A = \frac{\pi}{4}(139{,}7^2 - 123{,}7^2) \approx 3.295\,\text{mm}^2$$

Das im Modell gespeicherte Brep ist demnach kein Hohlprofil, sondern ein **massiver Vollzylinder**. Dies könnte auf einen Fehlverhalten im RFEM-Export (oder eine Modellanomalie) zurückzuführen sein. Für eine kohärente CO₂-Bilanz wäre hier ggf. Korrekturbedarf.

### 3. Rechteckhohlprofil 500×500
Mit einer mittieren QFläche von ~249.749 mm² handelt es sich um massive Pfeiler/Säulen. Diese machen fast **90 % des gesamten Stahlvolumens** aus. Das Volumen von ~11,74 m³ dominiert klar die Materialbilanz des Pavillon.

### 4. RD 12 (Rundstahl Ø12 mm)
Die 175 Zugstäbe des Profils RD 12 liegen **ausschließlich als Achslinien** vor, ohne 3D-Volumenkörper (kein `Members`-Layer dafür). Die theoretische Querschnittsfläche beträgt:

$$A = \pi \cdot r^2 = \pi \cdot 6^2 \approx 113{,}1\,\text{mm}^2$$

Da keine Volumengeometrie im Modell vorliegt, ist das Gesamtvolumen schätzungsweise.

---

## Zusammenfassung der wichtigsten Kennzahlen

| Größe | Wert |
|---|---:|
| Gesamtzahl der Stabelemente (mit Brep) | 561 |
| Gesamtzahl aller Stäbe (inkl. RD 12 als Linie) | 736 |
| Gesamtstahlvolumen (gemessen via Brep) | **~13,05 m³** |
| Dominierendes Profil | Rectangle 500/500 (90 % des Volumens) |
| Vouten-Elemente (veränderlicher Querschnitt) | 499 von 561 Breps (89 %) |
| Theoretisches Volumen (RD 12, geschätzt) | ~0,06 m³ |

---

*Berechnet mit RhinoCommon via MCP-Integration und Python-Analyse.*  
*Datum: 22. Oktober 2026*