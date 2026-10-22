import json
with open('pavillon_combined.js') as f:
    raw = f.read()
start = raw.find('[')
end = raw.rfind('];') + 1
data = raw[start:end]
with open('mesh_array.json', 'w') as f:
    f.write(data)
print(f"mesh_array.json created: {len(data)} bytes, members: {len(json.loads(data))}")