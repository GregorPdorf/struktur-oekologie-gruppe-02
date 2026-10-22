import json, os
meshes = json.load(open('pavillon_3d_data.json'))
co2_data = json.load(open('pavillon_members_enriched.json'))
co2_by_layer = {}
for m in co2_data:
    l = m['layer'].split('::')[-1] if '::' in m['layer'] else m['layer']
    if l not in co2_by_layer: co2_by_layer[l] = []
    co2_by_layer[l].append(m)
for layer, members in co2_by_layer.items():
    if members:
        ac = {}
        for k in ['co2_std','co2_alt','co2_c','co2_d']:
            ac[k] = sum(m[k] for m in members) / len(members)
        co2_by_layer[layer] = ac
for mesh in meshes:
    c = co2_by_layer.get(mesh['layer'], {'co2_std':0,'co2_alt':0,'co2_c':0,'co2_d':0})
    mesh.update(c)
with open('pavillon_combined.js', 'w') as f:
    f.write('var PAVILLON_MESHES = ' + json.dumps(meshes, separators=(',',':')) + ';')
sz = os.path.getsize('pavillon_combined.js')
print(f'Written {sz} bytes ({sz/1024/1024:.1f} MB) to pavillon_combined.js')
all_vals = [m[k] for m in meshes for k in ['co2_std','co2_alt','co2_c','co2_d']]
print(f'CO2 range: {min(all_vals):.1f} to {max(all_vals):.1f} kg')