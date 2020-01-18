import ingredients
import json
from pattern.en import singularize

with open('pollution.json') as f:
    __data = json.load(f)
pollution = dict()

for x in __data:
    for p in x["keywords"]:
        pollution[singularize(p.lower())] = x["co2"]

def get_carbon_footprint(barcode):
    ingreds = ingredients.getingredients(barcode)
    weight = 0.025 # in kilograms TODO

    i = ingreds[:3]

    co2 = 0
    for ingre in i:
        if ingre in pollution:
            co2 += weight / len(i) * pollution[ingre]
        else:
            return {"success": False, 
                    "reason": "ingredient: \"" + ingre + "\" not recognized"}
    
    return {"success": True,
            "result": str(co2) + "kg of co2"}

if __name__ == "__main__":
    print(get_carbon_footprint("51000005"))
    print(get_carbon_footprint("5060088701942"))

