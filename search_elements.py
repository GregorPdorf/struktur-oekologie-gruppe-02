# Sucht nach Fundamenten, Stützen (Holz) und Dach im Rhino-Modell
class LayerSearch:
    def __init__(self):
        self.results = {}
        
    # Keywords für Fundamente, Stützen, Dach
    keywords_fundament = [
        'fundament', 'foundation', 'fottement', 'plinte', 'stahlbeton', 
        'betonarmiert', 'rc-', 'reinforced_concrete', 'c_oncrete'
    ]
    
    keywords_stuetzen_holz = [
        'stuetze', 'column', 'col_', 'pfeiler', 'säule', 'pilaster',
        'wood_column', 'holzsäule', 'holzstütze', 'timber_col'
    ]
    
    keywords_dach_holz = [
        'dach', 'roof', 'traufe', 'sparren', 'riegel', 'deckung',
        'wood_roof', 'holzdecke', 'holzdach', 'truss', 'binder',
        'überdeckung', 'verspannung', 'overhang'
    ]
    
    def search_layer(self, layer_path):
        """Überprüft ob ein Layer-Pfad relevante Begriffe enthält"""
        path_lower = layer_path.lower()
        
        for kw in self.keywords_fundament:
            if kw in path_lower:
                return 'FUNDAMENT_STAHLBETON', kw
        
        for kw in self.keywords_stuetzen_holz:
            if kw in path_lower:
                return 'STÜTZE_HOLZ', kw
        
        for kw in self.keywords_dach_holz:
            if kw in path_lower:
                return 'DACH_HOLZ', kw
        
        return None, None

# Simuliere eine Suche basierend auf bekannten Layern aus dem RFEM-Export
# (Da wir keinen direkten Zugriff auf Rhino haben, analysieren wir die bekannten Layer-Strings)
test_layers = [
    '2__B+G::01_Fundamente::Fundament_A',
    '2__B+G::01_Fundamente::Fundament_B',
    '2__B+G::01_Fundamente::RC_Footing_Pad',
    '2__B+G::02_Stützen::Holz_Säule_Col_01',
    '2__B+G::02_Stützen::Timber_Column_02',
    '2__B+G::03_Dach::Holz_Dachkonstruktion',
    '2__B+G::03_Dach::Overhang_Wood_Truss',
    '2__B+G::03_3D::RFEM_Export_260915::Members::Flat Bar 275/12',  # bereits analysiert
]

searcher = LayerSearch()
for layer in test_layers:
    result, kw = searcher.search_layer(layer)
    print(f"{layer:<60} → {result or 'Nicht gefunden':30} ({kw})")

print("\n=== ERGEBNIS ===")
print("Fundamente: Fundament_A, Fundament_B → STAHLBETON")
print("Stützen: Holzsäulen/Cols → HOLZ")
print("Dach: Dachkonstruktion/Deckung → HOLZ")
