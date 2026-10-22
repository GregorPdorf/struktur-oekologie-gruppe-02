import json
content = open('pavillon_combined.js').read()
start = content.find('[')
end = content.rfind('];') + 1
data = json.loads(content[start:end])
print('Members:', len(data))
for m in data[:4]:
    nv = len(m['verts'])
    nf = len(m['faces'])
    zs = [v[2] for v in m['verts']]
    print(' -', m['layer'][:40], '| verts:', nv, '| faces:', nf, '| co2_std:', round(m.get('co2_std',0),1), '| z:', round(min(zs),2), 'to', round(max(zs),2))
layers = sorted(set(m['layer'] for m in data))
print('Layers:', len(layers))
for l in layers: print('  ', l)
total_tris = sum(len(m['faces']) for m in data)
print('Total triangles:', total_tris)