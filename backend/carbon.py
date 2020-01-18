import ingredients
import json
from pattern.en import singularize
import sys

with open('pollution.json') as f:
    __data = json.load(f)
pollution = dict()

for x in __data:
    for p in x["keywords"]:
        pollution[singularize(p.lower())] = x["co2"]

def f(prevsum, curr, x):
    return {"y": (1-x)*prevsum + x*curr, "x":x}

def get_min_max(carr):
    if len(carr) == 0:
        return {"min":0, "max":0,
                "min_mi": 1, "max_mi": 1}
    if len(carr) == 1:
        return {"min":carr[0], "max":carr[0],
                "min_mi": 1.0, "max_mi": 1.0}
    else:
        mm = get_min_max(carr[:-1])
        # min
        min_bound = 0.001
        max_bound = mm["min_mi"]/(1.0+mm["min_mi"])
        vals = [f(mm["min"], carr[-1], min_bound),
                f(mm["min"], carr[-1], max_bound)]
        v = (carr[-1] - mm["min"])
        if min_bound < v and v < max_bound:
            vals.append(f(mm["min"], carr[-1], v))
        vals.sort(key = lambda v: v["y"])
        _min = vals[0]

        # max
        min_bound = 0.001
        mix_bound = mm["max_mi"]/(1+mm["max_mi"])
        vals = [f(mm["max"], carr[-1], min_bound),
                f(mm["max"], carr[-1], max_bound)]
        v = (carr[-1] - mm["max"])
        if min_bound < v and v < max_bound:
            vals.append(f(mm["max"], carr[-1], v))
        vals.sort(key = lambda v: v["y"], reverse = True)
        _max = vals[0]

        return {"min": _min["y"], "max": _max["y"],
                "min_mi": _min["x"], "max_mi": _max["x"]}
        

def splitshit(quantity):
    firstnonnum = 0
    for i in range(len(quantity)):
        if quantity[i].isdigit():
            firstnonnum = i;
    firstnonnum += 1
    units = firstnonnum
    if quantity[units] == ' ':
        units += 1
    
    return [quantity[:firstnonnum], quantity[units:]]

def get_carbon_footprint(barcode):
    _ingreds = ingredients.getingredientswithquantity(barcode)
    ingreds = _ingreds["ingredients"]
    quantity = splitshit(_ingreds["quantity"])
    scale = 1
    print (quantity)
    if (quantity[1] == "ml" or quantity[1] == "g"):
        scale = 0.001
    if (quantity[1] == "cl" or quantity[1] == "dag"):
        scale = 0.01

    weight = int(quantity[0]) * scale

    pollution_factors = [pollution[ingre] for ingre in ingreds]

    mm = get_min_max(pollution_factors)

    return {"min": mm["min"]*weight,
            "max": mm["max"]*weight}

if __name__ == "__main__":
    print(get_carbon_footprint("51000005"))
    #print(get_carbon_footprint("5060088701942"))
    print(get_carbon_footprint("4251097403083")) # beef jerky

