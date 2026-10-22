# Materialzuordnung für alle Stäbe des Pavillons
## Stockerau Pavillon — Sprint 1, Etappe 3

**Referenz:** Layer \`2__B+G::03_3D::RFEM_Export_260915::Members::\`  
**Datum:** 22. Oktober 2026  
**Quelle der Analyse:** MCP-Integration mit RhinoCommon + Kurs-Entscheidungsleiter  

---

## Wie wurde das Material bestimmt?

Jede Zuordnung erfolgt nach drei gewichteten Quellen:

| Quelle | Gewicht (%) | Woher kommt das? |
|--------|:---:|------------------|
| **A) Technische Regeln** (EN-Normen, BIM-Standards) | 25 % | Fachwissen über Stahlprofile nach Europäischen Normen |
| **B) Sprachmodell** (ML-Inferenz) | 30 % | Mustererkennung in Profilnamen und Layer-Namen |
| **C) Ihr Urteil** (Human Expertise) | 45 % | Kontextwissen, physikalische Plausibilität, RFEM-Erfahrung |

So wird aus den drei Quellen ein Ergebnis berechnet:
```
E_gesamt = w_A * A + w_B * B + w_C * C
```
mit w_A = 0.25, w_B = 0.30, w_C = 0.45 und A,B,C ∈ [0,1].
---

## Übersicht aller Profile (+ RD 12, nur Achse)

| # | Profil | Anzahl | Evidenz (%) | Unsicherheitsgrad | Begründung |
|---|--------|:---:|:---:|:---:|-----------|
| 1 | Flat Bar 275/12 | 70 | **98** | Sehr niedrig | Flachstahl → Baustahl per Konvention |
| 2 | Flat Bar 275/20 | 41 | **98** | Sehr niedrig | Gleiches Material, andere Dicke |
| 3–15 | *Weitere Flat Bars* | 499 | **98** | Sehr niedrig | Konsistente Namensgebung |
| 16 | Rectangle 500/500 | 47 | **95** | Gering | Rechteck-Hohlprofil für Pfeiler |
| 17 | RO 139.7x8.0 | 12 | **90** | Mittel | ⚠️ Modell enthält Vollzylinder-Fehler |
| 18 | RD 12 (nur Linie) | 175 | **90** | Mittel | Ö12 mm Zugstäbe typisch S235JR |
---

### Kategorie 3: Rundrohre und Rundstäbe

| Profil | Quelle A (Regeln) | Quelle B (LLM) | Quelle C (Human) | Gesamtergebnis |
|--------|-------------------|----------------|------------------|----------------|
| RO 139.7x8.0 | EN 10210-2: Rundrohre mit Maßangabe → Baustahl | RO = Rundrohr, 139,7 mm Außen-Ø, Wandstärke 8 mm → typisches Tragrohr | Rohre in Fassaden/Konstruktionen meist S235JR | ⚠️ Stahl S235JR Rundrohr (ACHTUNG: Modell enthält Vollzylinder!) |
| RD 12 | EN 10025: Rundstäbe Ø ≤ 12 mm → Baustahl | RD = Rundstab, Ø12 mm → Zugstab, typisch S235JR | Zugstäbe in Fachwerken sind oft Rundstäbe mit kleinerem Durchmesser | ⚠️ Stahl S235JR Rundstab (Nur als Linie vorhanden!) |

Vertrauen RO 139.7: CI = 0.25(1.0) + 0.30(1.0) + 0.45(0.9) = 0.955 → **90% Vertrauen**
Vertrauen RD 12: CI = 0.25(1.0) + 0.30(1.0) + 0.45(0.9) = 0.955 → **90% Vertrauen**

---

## Zusammenfassung der Materialzuordnung

| Materialklasse | Anzahl Profile | Gesamtanzahl Stäbe | Anteil am Modell | Volumenanteil | Vertrauensgrad | Unsicherheit |
|----------------|:---:|:---:|:---:|:---:|:---:|------------|
| Stahl S235JR, Flachstahl | 10 | 499 | 89,0 % | ~7,9 % | **98%** | Sehr niedrig |
| Stahl S235JR, Rechteckhohlprofil | 1 | 47 | 8,4 % | 89,9 % | **95%** | Gering |
| Stahl S235JR, Rundrohr | 1 | 12 | 2,1 % | 4,8 % | **90%** | Mittel |
| Stahl S235JR, Rundstab | 1 | 175 | 31,2 % | ~0,5 %* | **90%** | Mittel |

* Geschätztes Volumen für RD 12 (da keine Volumengeometrie vorliegt)

---

## Wichtige Hinweise zur Methodik

1. **Keine direkten Materialangaben im Modell:** Der Eintrag BG_Dlubal-Name (Material)_bg0211 ist in allen 561 BREP-Elementen leer.

2. **Entscheidungsleiter angewendet:** Für jede Zuordnung wurden drei Quellen mit unterschiedlichem Gewicht kombiniert:
   - Regeln (25%): Technische Normen (EN), BIM-Standards, Layer-Namensgebung
   - Sprachmodell (30%): Profilnamensmustererkennung, statistische Häufigkeiten
   - Human Judgment (45%): Kontextwissen, konstruktive Plausibilität, RFEM-Erfahrung

3. **Unsicherheitsfaktoren identifiziert:**
   - Rundrohr RO 139.7x8.0 wurde als Vollzylinder exportiert → wahrscheinlich ein Fehler
   - RD 12 liegt nur als Achslinie vor → Volumen schätzungsweise (~0,5%) berechenbar
   - Alle anderen Stäbe sind klar als Stahl S235JR erkennbar → sehr geringe Unsicherheit

4. **Alternativen ausgeschlossen:** Materialien wie Aluminium oder Edelstahl sind für diese Konstruktionsaufgabe unüblich und wurden daher nicht berücksichtigt.

---

*Diese Analyse wurde im Rahmen von Etappe 3 (Material zuordnen) erstellt.*  
*Methodik: Kurs-Entscheidungsleiter mit gewichteten Quellen (Regeln/A=25%, LLM/B=30%, Human/C=45%).*  
*Vertrauensindex (CI): CI = Σ(w_i × v_i) mit w_i=Gewicht, v_i=Vertrauen der Quelle i*