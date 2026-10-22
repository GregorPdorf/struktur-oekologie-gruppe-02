#!/usr/bin/env python3
import csv, math
from collections import defaultdict

data = open("/tmp/members_data.txt").readlines()
members = []
for line in data:
    # Profile names can contain "|", so we parse carefully:
    # First token is always the UUID. After profile, comes min_coords(3 vals separated by commas),
    # max_coords(3 vals), volume(1 val), then 6 area values.
    # A coordinate/numeric field either starts with a digit or a minus sign.
    parts_raw = line.strip().split("|")
    obj_id = parts_raw[0]
    # Search from position 2 onward for the FIRST field that looks like coordinates
    coord_start = None
    for i in range(2, len(parts_raw)):
        t = parts_raw[i].strip()
        if t and (t[0].isdigit() or (len(t)>1 and t[0]=='-' and t[1].isdigit())):
            coord_start = i
            break
    if coord_start is None: continue
    prof = "|".join(parts_raw[1:coord_start])
    numeric_parts = parts_raw[coord_start:]
    bm = list(map(float, numeric_parts[0].split(",")))
    bM = list(map(float, numeric_parts[1].split(",")))
    vol = float(numeric_parts[2])
    ar = [float(x) for x in numeric_parts[3:]]
    bi, bs = 0, 0
    for i in range(0, 6, 2):
        s = ar[i]+ar[i+1]
        if s > bs: bs, bi = s, i//2
    dims = [bM[j]-bm[j] for j in range(3)]
    members.append(dict(id=obj_id, prof=prof, vol=vol,
                        areas=(ar[bi*2], ar[bi*2+1]),
                        dims=dims))

pg = defaultdict(list)
for m in members: pg[m["prof"]].append(m)

rows = []
tv_all = tc_all = 0
for prf, grp in sorted(pg.items(), key=lambda x: -sum(m["vol"] for m in x[1])):
    n = len(grp)
    tv = sum(m["vol"] for m in grp)
    aa, dd = [], []
    for m in grp:
        a0,a1 = m["areas"]
        if a0>1e-9: aa.append(a0)
        if a1>1e-9: aa.append(a1)
        if a0>1e-9 and a1>1e-9: dd.append(abs(a0-a1)/min(a0,a1))
    mA = sum(aa)/len(aa)*1e6 if aa else 0
    mna = min(aa)*1e6 if aa else 0
    mxA = max(aa)*1e6 if aa else 0
    taper = any(d>0.02 for d in dd) if dd else False
    adp = sum(dd)/len(dd)*100 if dd else 0
    rows.append((prf, n, tv, mA, mna, mxA, "Voute" if taper else "Konstant", adp))
    tv_all += tv; tc_all += n

path = "/Users/nick/struktur-oekologie-gruppe-02/Staebe_Querschnittsflaeche_Volumen.csv"
with open(path,"w",newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["Profil","Anzahl_Staebe","Volumen_gesamt_m3","Mittlere_QFl_mm2","Min_QFl_mm2","Max_QFl_mm2","Typ","Flaechenunterschied_%"])
    for r in rows:
        w.writerow([r[0],r[1],f"{r[2]:.6f}",f"{r[3]:.1f}",f"{r[4]:.1f}",f"{r[5]:.1f}",r[6],f"{r[7]:.1f}%" if r[7]>0 else "---"])

print(f"Wrote {path}")
print()
print(f'{"Profil":<40} {"Anz":>4} {"Vol(m3)":>12} {"A_mean(mm2)":>12} {"Min(mm2)":>10} {"Max(mm2)":>10} {"Typ":>8}')
print("-"*100)
for r in rows:
    print(f'{r[0]:<40} {r[1]:>4} {r[2]:>12.6f} {r[3]:>12.1f} {r[4]:>10.1f} {r[5]:>10.1f} {r[6]:>8}')
print(f"\nGESAMT: {tc_all} Staerbe, {tv_all:.6f} m3")

rd12_cnt = 175
rd12_area = math.pi * 6**2
rd12_est_len = rd12_cnt * 3.0
rd12_vol = rd12_area * 1e-6 * rd12_est_len
print(f"\nRD 12 (Rundstahl Ø12mm):")
print(f"  Anzahl: {rd12_cnt} | QFläche: π*6² = {rd12_area:.1f} mm²")
print(f"  Gsch. Volumen: ~{rd12_vol:.6f} m³ (theoretisch)")
