import json

data = {
    "name": "Ashutosh",
    "role": "AI Engineer"
}

json_data = json.dumps(data)

print(json_data)