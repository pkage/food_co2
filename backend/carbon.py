import ingredients
import json
from pattern.en import singularize

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
        return {"min":0, "max":0}
    if len(carr) == 1:
        return {"min":carr[0], "max":carr[0],
                "mi_min": 1, "mi_max": 1}
    else:
        mm = get_min_max(carr[:-1])
        # min
        min_bound = 0.001
        max_bound = mm["min_mi"]/(1+mm["min_mi"])
        vals = [f(mm["min"], carr[-1], min_bound),
                f(mm["min"], carr[-1], max_bound)]
        v = (carr[-1] - mm["min"])
        if min_bound < v and v < max_bound:
            vals.append(f(mm["min"], carr[-1], v))
        _min = vals.sort(key = lambda v: v["y"])[0]

        # max
        min_bound = 0.001
        mix_bound = mm["max_mi"]/(1+mm["max_mi"])
        vals = [f(mm["max"], carr[-1], min_bound),
                f(mm["max"], carr[-1], max_bound)]
        v = (carr[-1] - mm["max"])
        if min_bound < v and v < max_bound:
            vals.append(f(mm["max"], carr[-1], v))
        _max = vals.sort(key = lambda v: v["y"], reverse = True)[0]

        return {"min": _min["y"], "max": _max["y"],
                "mi_min": _min["x"], "mi_max": _max["x"]}
        

def get_carbon_footprint(barcode):
    ingreds = ingredients.getingredients(barcode)
    weight = 0.025 # in kilograms TODO

    pollution_factors = [pollution[ingre] for ingre in ingreds]

    mm = get_min_max(pollution_factors)

    return {"min": mm["min"]*weight,
            "max": mm["max"]*weight}

if __name__ == "__main__":
    print(get_carbon_footprint("51000005"))
    print(get_carbon_footprint("5060088701942"))

