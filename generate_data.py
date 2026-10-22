import json

# Load member geometry
with open('pavillon_members.json') as f:
    members = json.load(f)

# Profile data
profiles = {
    "Flat Bar 275/12": {"vol_total": 0.128528, "count": 70, "mat": "steel"},
    "Flat Bar 275/20": {"vol_total": 0.132748, "count": 41, "mat": "steel"},
    "Flat Bar 225/12": {"vol_total": 0.070743, "count": 35, "mat": "steel"},
    "Flat Bar 225/20": {"vol_total": 0.077480, "count": 23, "mat": "steel"},
    "Flat Bar 175/12": {"vol_total": 0.052990, "count": 35, "mat": "steel"},
    "Flat Bar 175/20": {"vol_total": 0.057567, "count": 23, "mat": "steel"},
    "Flat Bar 237.5/12": {"vol_total": 0.035680, "count": 35, "mat": "steel"},
    "Flat Bar 237.5/20": {"vol_total": 0.030583, "count": 18, "mat": "steel"},
    "Flat Bar 200/12": {"vol_total": 0.029563, "count": 35, "mat": "steel"},
    "Flat Bar 200/20": {"vol_total": 0.025340, "count": 18, "mat": "steel"},
    "Flat Bar 162.5/12": {"vol_total": 0.023405, "count": 35, "mat": "steel"},
    "Flat Bar 162.5/20": {"vol_total": 0.019567, "count": 18, "mat": "steel"},
    "Flat Bar 33.3/20": {"vol_total": 0.001510, "count": 116, "mat": "steel"},
    "Rectangle 500/500": {"vol_total": 11.738228, "count": 47, "mat": "concrete"},
    "RO 139.7x8.0 | EN 10210-2:2006": {"vol_total": 0.629460, "count": 12, "mat": "steel"},
    "RD 12": {"vol_total": 0.021, "count": 175, "mat": "steel"}
}

# GWP: steel kg CO2e/kg, concrete kg CO2e/m3
gwp = {
    "steel": {"std_A1A3": 2.2, "alt_A1A3": 0.52, "C": 0.05, "D": -0.41},
    "concrete": {"std_A1A3": 135.0, "alt_A1A3": 105.0, "C": 10.0, "D": -20.0}
}

for m in members:
    name = m["layer"].split("::")[-1] if "::" in m["layer"] else m["layer"]
    p = profiles.get(name, None)
    if p is None:
        for k in profiles:
            if k in name or name in k:
                p = profiles[k]; break
    
    if p and p["count"] > 0:
        v = p["vol_total"] / p["count"]
        g = gwp[p["mat"]]
        factor = v * 7850 if p["mat"] == "steel" else v
        m["co2_std"] = round(factor * g["std_A1A3"], 3)
        m["co2_alt"] = round(factor * g["alt_A1A3"], 3)
        m["co2_c"] = round(factor * g["C"], 3)
        m["co2_d"] = round(factor * g["D"], 3)
        m["g"] = p["mat"]
    else:
        m["co2_std"] = m["co2_alt"] = m["co2_c"] = m["co2_d"] = 0
        m["g"] = "?"

with open('pavillon_members_enriched.json', 'w') as f:
    json.dump(members, f, indent=2)

# Calculate totals
total_std = sum(m["co2_std"] for m in members)
total_alt = sum(m["co2_alt"] for m in members)
print(f"Members: {len(members)}")
print(f"Total CO2 standard: {total_std:.1f} kg")
print(f"Total CO2 alternative: {total_alt:.1f} kg")
print(f"Savings: {(total_std-total_alt)/total_std*100:.1f}%")
print("Data saved to pavillon_members_enriched.json")