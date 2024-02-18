import json

with open("capitals.json", "r") as my_file:
    capitals_json = my_file.read()

capitals = json.loads(capitals_json)
print(capitals["Россия"])