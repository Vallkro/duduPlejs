import json

with open('temp.json', 'r') as inFile:
    data = json.load(inFile)

print(data)