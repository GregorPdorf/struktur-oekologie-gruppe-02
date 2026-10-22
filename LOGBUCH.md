# Logbuch

Pro Etappe ein Eintrag. Kurz reicht. Das Logbuch ist Teil der Abgabe und Grundlage eurer Demo.
One entry per stage. Short is fine. The log is part of the submission and the basis for your demo.

## Etappe 0

- **Was wir gemacht haben:**
  - Repository und Projektstruktur geprüft
  - Virtuelle Umgebung aktiviert und Python-Setup validiert
  - `check_setup.py` ausgeführt; Python, Pakete, Git, VS Code-Integration, `.env` und API-Key geprüft
  - Umgebung als startklar bestätigt; keine fachlichen Modell- oder Rechenfehler in dieser Phase festgestellt
- **Wichtigste Prompts** (wörtlich kopieren):
  - `python .\.venv\Scripts\python.exe .\check_setup.py`
- **Was schiefging und woran wir es gemerkt haben:**
  - Keine größeren Probleme in der Setup-Phase. Die Umgebung war bereits vorbereitet; die Validierung hat bestätigt, dass `.env` und API-Key korrekt gesetzt sind.
- **Was wir selbst geprüft haben** (von Hand, im Plan, im Modell):
  - Python 3.14.8 aktiv
  - 7 Python-Pakete vorhanden
  - Git und VS Code Terminal-Integration funktionieren
  - `.gitignore` schützt `.env`
  - API-Key funktioniert mit openrouter, Kreditlimit 10 $

---

# Sprint 1: Carbon-Inventur Pavillon Stockerau

## Etappe 1: Modell lesen

**Test:** Wie viele Stäbe hat der Pavillon? Prüft die Zahl am Modell nach.
Insg. 736 Stäbe, 561 mit 3D Volumenkörper. 176 als Linie.


**Learning oder Besonderheit: ---------


## Etappe 2: Querschnitte verstehen

**Test:** Rechnet einen Stab, dessen Querschnitt sich über die Länge ändert, von Hand nach und vergleicht mit eurem Programm.


**Learning oder Besonderheit: Top Funktioniert.


## Etappe 3: Material zuordnen

**Test:** Sind die Materialangaben, die schon im Modell stehen, plausibel? Zeigt an einem Stab, wie ihr das geprüft habt.


**Learning oder Besonderheit: Konkrete Infos im Prompt einbauen, lieber zu viel schreiben als zu wenig um es richtig auszuführen und für den Agenten zu beschreiben


## Etappe 4: Embodied Carbon aus der ÖKOBAUDAT

**Test:** Rechnet einen Stab von seiner Länge bis zu kg CO₂e (A1–A3) von Hand nach.


**Learning oder Besonderheit: Der KI Agent hat alles top ausgeführt, auch die Frage nach einer zu generierenden PDF kam gut an und dauerte nicht allzu lang.


## Etappe 5: Web-App

**Test:** Schaltet beim Stahl auf die Alternative um. Was erwartet ihr vorher, was passiert, und warum?


**Learning oder Besonderheit:**


## Zum Schluss

Wie habt ihr mit dem Agenten gearbeitet, und was würdet ihr der nächsten Gruppe mitgeben?


Ich saß nun 6 Stunden daran die App zu erstellen, er will auf Teufel komm raus nicht die 3D VErsion des Modells importieren... keine Ahnung woran es liegt.




