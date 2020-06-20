import json

with open('gostbook.json') as f:
    filename = json.load(f)

print(filename)