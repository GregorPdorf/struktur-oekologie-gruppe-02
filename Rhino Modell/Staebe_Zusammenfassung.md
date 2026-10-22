# Zusammenfassung der Stäbe – Pavillon Stockerau

**Quelle:** `Stockerau Rhino Export from RFEM.3dm`
**Layer-Pfad:** `2__B+G::03_3D::RFEM_Export_260915::`
**Detaillierte Einzelliste:** siehe [`Staebe_Liste.csv`](./Staebe_Liste.csv)

---

## Darstellung im Modell

Jeder Stab liegt (sofern vorhanden) in **zwei Darstellungen** vor:

| Darstellung | Objekttyp | Layer-Gruppe | Bedeutung |
|---|:---:|---|---|
| Stabachse | `LINE` | `MemberAxes` | Achse aus der statischen Berechnung (RFEM) |
| Volumenkörper | `BREP` | `Members` | Reale 3D-Geometrie mit Querschnittsprofil |

---

## Übersicht nach Profil

| # | Profil | Anzahl Stäbe | Anteil | Mit Brep-Volumenkörper |
|---:|---|---:|---:|:---:|
| 1 | RD 12 | 175 | 23,8 % | ❌ nein (nur Achse) |
| 2 | Flat Bar 33.3/20 | 116 | 15,8 % | ✅ ja |
| 3 | Flat Bar 275/12 | 70 | 9,5 % | ✅ ja |
| 4 | Rectangle 500/500 | 47 | 6,4 % | ✅ ja |
| 5 | Flat Bar 275/20 | 41 | 5,6 % | ✅ ja |
| 6 | Flat Bar 162.5/12 | 35 | 4,8 % | ✅ ja |
| 7 | Flat Bar 175/12 | 35 | 4,8 % | ✅ ja |
| 8 | Flat Bar 200/12 | 35 | 4,8 % | ✅ ja |
| 9 | Flat Bar 225/12 | 35 | 4,8 % | ✅ ja |
| 10 | Flat Bar 237.5/12 | 35 | 4,8 % | ✅ ja |
| 11 | Flat Bar 175/20 | 23 | 3,1 % | ✅ ja |
| 12 | Flat Bar 225/20 | 23 | 3,1 % | ✅ ja |
| 13 | Flat Bar 162.5/20 | 18 | 2,4 % | ✅ ja |
| 14 | Flat Bar 200/20 | 18 | 2,4 % | ✅ ja |
| 15 | Flat Bar 237.5/20 | 18 | 2,4 % | ✅ ja |
| 16 | RO 139.7×8.0 \| EN 10210-2:2006 | 12 | 1,6 % | ✅ ja |
| | **Gesamt** | **736** | **100 %** | **561 mit Brep** |

---

## Übersicht nach Profilkategorie

| Kategorie | Profile enthalten | Anzahl Stäbe | Anteil |
|---|---|---:|---:|
| Flachstähle | alle "Flat Bar ..." (10 Varianten) | 502 | 68,2 % |
| Rundstahl (Zugstäbe) | RD 12 | 175 | 23,8 % |
| Rechteckhohlprofil | Rectangle 500/500 | 47 | 6,4 % |
| Rundrohr | RO 139.7×8.0 | 12 | 1,6 % |
| **Gesamt** | | **736** | **100 %** |

---

## Kernaussagen

- Insgesamt **736 Stäbe** im Modell (gezählt über die Achslinien in `MemberAxes`).
- **561 Stäbe** besitzen zusätzlich einen 3D-Volumenkörper (`BREP`) mit realem Querschnitt in `Members`.
- **175 Stäbe** (ausschließlich Profil **RD 12**) liegen **nur als Achslinie** vor – für dieses Profil existiert im Modell kein `Members`-Unterlayer mit Brep-Geometrie (vermutlich Zugstäbe/Seilelemente, die im Statikmodell oft nur als Linienelement benötigt werden).
- Mit Abstand am häufigsten sind **Flachstahl-Profile** (502 Stäbe, rund zwei Drittel aller Stäbe), gefolgt vom Rundstahl RD 12.
- Die Zuordnung Achse ↔ Brep in der Detailliste erfolgte über den nächstgelegenen Volumen-Schwerpunkt zum Achsmittelpunkt (Toleranz 1 m); alle 561 Breps konnten eindeutig zugeordnet werden.
