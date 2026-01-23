import json

# Extract formatting from an existing JSON structure
original_json = {'saldo': 90, 'varer': ['Kiwi']}
original_json_str = json.dumps(original_json, separators=(',', ':'))  # Ensures no extra spaces
print(f"Original JSON: {original_json_str} ({len(original_json_str)} bytes)")

# Create the new forged JSON with identical formatting
forged_json = {'saldo':  7, 'varer': ['Flagg']}
forged_json_str = json.dumps(forged_json, separators=(',', ':'))  # Same formatting
print(f"Forged JSON: {forged_json_str} ({len(forged_json_str)} bytes)")

# Ensure both lengths are exactly the same!
assert len(forged_json_str) == len(original_json_str), "Length mismatch!"
