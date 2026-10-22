#!/usr/bin/env python3
import json, os

# Load existing data
with open('app/mesh_array.json') as f:
    meshes = json.load(f)
with open('app/pavillon_members_enriched.json') as f:
    members = json.load(f)

# RD 12 line calculations (from Rhino LINE objects)
rd12_area_m2 = 113.1 / 1e6
rd12_length = 2.5
rd12_vol = rd12_area_m2 * rd12_length
rd12_mass = rd12_vol * 7850
rd12_co2_std = rd12_mass * 2.2
rd12_co2_alt = rd12_mass * 0.52
rd12_co2_c = rd12_mass * 0.05
rd12_co2_d = rd12_mass * (-0.41)

brep_count = len([m for m in members if m.get('type') == 'BREP'])

total_std = sum(m.get('co2_std', 0) for m in members) + 175 * rd12_co2_std
total_alt = sum(m.get('co2_alt', 0) for m in members) + 175 * rd12_co2_alt

output = {
    "model_info": {
        "source": "Stockerau Rhino Export from RFEM.3dm",
        "date_modified": "2026-10-21T12:24:00",
        "units": "Meters",
        "total_members": brep_count + 175,
        "brep_count": brep_count,
        "line_count": 175,
    },
    "profiles": {
        "Flat Bar 275/12": {"mat": "steel", "w": 275, "t": 12, "density": 7850},
        "Flat Bar 275/20": {"mat": "steel", "w": 275, "t": 20, "density": 7850},
        "Flat Bar 225/12": {"mat": "steel", "w": 225, "t": 12, "density": 7850},
        "Flat Bar 225/20": {"mat": "steel", "w": 225, "t": 20, "density": 7850},
        "Flat Bar 175/12": {"mat": "steel", "w": 175, "t": 12, "density": 7850},
        "Flat Bar 175/20": {"mat": "steel", "w": 175, "t": 20, "density": 7850},
        "Flat Bar 237.5/12": {"mat": "steel", "w": 237.5, "t": 12, "density": 7850},
        "Flat Bar 237.5/20": {"mat": "steel", "w": 237.5, "t": 20, "density": 7850},
        "Flat Bar 200/12": {"mat": "steel", "w": 200, "t": 12, "density": 7850},
        "Flat Bar 200/20": {"mat": "steel", "w": 200, "t": 20, "density": 7850},
        "Flat Bar 162.5/12": {"mat": "steel", "w": 162.5, "t": 12, "density": 7850},
        "Flat Bar 162.5/20": {"mat": "steel", "w": 162.5, "t": 20, "density": 7850},
        "Flat Bar 33.3/20": {"mat": "steel", "w": 33.3, "t": 20, "density": 7850},
        "Rectangle 500/500": {"mat": "concrete", "outer_w": 500, "wall_t": 50, "density_concrete": 2400},
        "RO 139.7x8.0 | EN 10210-2:2006": {"mat": "steel", "od": 139.7, "t": 8.0, "density": 7850},
        "RD 12": {"mat": "steel", "diameter_mm": 12, "area_mm2": 113.1, "density": 7850, "length_per_stab_m": rd12_length},
    },
    "materials": {
        "standard": {
            "steel_A1A3": 2.2, "steel_C": 0.05, "steel_D": -0.41,
            "concrete_A1A3": 135.0, "concrete_C": 10.0, "concrete_D": -20.0,
            "description": "Hochofen-Stahl / Normbeton"
        },
        "alternative": {
            "steel_A1A3": 0.52, "steel_C": 0.05, "steel_D": -0.41,
            "concrete_A1A3": 105.0, "concrete_C": 10.0, "concrete_D": -20.0,
            "description": "EAF-Stahl / EcoPact-Beton"
        }
    },
    "lifecycle_modules": [
        {"id": "A1A3", "label": "A1-A3", "full": "Rohstoffbereitstellung, Transport, Herstellung"},
        {"id": "C", "label": "C", "full": "Ende des Lebenszyklus"},
        {"id": "D", "label": "D", "full": "Potenzielle Vorteile (Recycling)"},
        {"id": "TOTAL", "label": "Gesamt", "full": "A1-A3 + C + D"}
    ],
    "members": members,
    "rd12_stub": {
        "count": 175,
        "mass_per_stab_kg": round(rd12_mass, 4),
        "co2_std": round(rd12_co2_std, 4),
        "co2_alt": round(rd12_co2_alt, 4),
        "co2_c": round(rd12_co2_c, 4),
        "co2_d": round(rd12_co2_d, 4),
    },
    "totals": {
        "total_std_kg": round(total_std, 1),
        "total_alt_kg": round(total_alt, 1),
        "savings_kg": round(total_std - total_alt, 1),
        "savings_pct": round((total_std - total_alt) / total_std * 100, 1),
    }
}

# Build member lookup by layer index
member_layer_indices = {}
for i, m in enumerate(members):
    layer = m['layer']
    if layer not in member_layer_indices:
        member_layer_indices[layer] = []
    member_layer_indices[layer].append(i)

# Add IDs to meshes and link them to members
mesh_output = []
used_members = set()
for mesh in meshes:
    layer = mesh['layer']
    indices = member_layer_indices.get(layer, [])
    # Assign next unused member index for this layer
    idx = None
    for ii in indices:
        if ii not in used_members:
            idx = ii
            break
    if idx is None and indices:
        idx = indices[0]
    
    mesh_entry = {
        'layer': layer,
        'verts': mesh['verts'],
        'faces': mesh['faces'],
        'member_id': members[idx]['id'] if idx is not None else None,
        'co2_std': mesh.get('co2_std', 0),
        'co2_alt': mesh.get('co2_alt', 0),
        'co2_c': mesh.get('co2_c', 0),
        'co2_d': mesh.get('co2_d', 0),
    }
    mesh_output.append(mesh_entry)
    if idx is not None:
        used_members.add(idx)

output['meshes'] = mesh_output

with open('app/data.json', 'w') as f:
    json.dump(output, f)

print(f"Wrote app/data.json ({len(mesh_output)} meshes, {len(used_members)} unique members linked)")
print(f"Total Standard: {total_std:.1f} kg CO2e")
print(f"Total Alternative: {total_alt:.1f} kg CO2e")
print(f"Savings: {(total_std-total_alt)/total_std*100:.1f}%")

