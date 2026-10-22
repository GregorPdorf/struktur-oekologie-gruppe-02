import json, os

# Read mesh data + embed inline
with open('pavillon_combined.js', 'r', encoding='utf-8') as f:
    raw = f.read()
start = raw.find('[')
end = raw.rfind('];') + 1
mesh_json = raw[start:end]
print(f"Mesh JSON: {len(mesh_json)} bytes, sample: {mesh_json[:120]}")

# Verify structure
data = json.loads(mesh_json)
print("Members:", len(data))
print("First member keys:", list(data[0].keys()))
print("verts[0][:5]:", data[0]['verts'][:5])
print("faces[0][:3]:", data[0]['faces'][:3])

# Save a copy of just the mesh array for inlining
with open('mesh_array.json', 'w') as f:
    f.write(mesh_json)
print("mesh_array.json written")