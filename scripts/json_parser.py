import json

with open("pollution.json", "r") as infile:
    file = infile.read()
    data = json.loads(file)

keywords = []
for el in data:
    keywords.append(el["keywords"])

with open("keywords.json", "w+") as outfile:
    outfile.write(json.dumps(keywords))
print(keywords)
