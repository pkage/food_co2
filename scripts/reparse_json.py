import json


with open("backend/cars.json", "r") as infile:
    data = json.load(infile)

new_data = list(data.keys())

with open("backend/cars_options.json", "w") as outfile:
    outfile.write(json.dumps(new_data))
