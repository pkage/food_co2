import json

with open('backend/pollution.json') as f:
    data = json.load(f)


# Will return a list of (original,[suggestions])
def getsuggestions(ingredients):
    responses = list()

    for ingredient in ingredients:
        co2 = getco2(ingredient)
        categories = getcategories(ingredient)
        suggestions = mostsimilar(categories, co2)
        responses.append((ingredient, suggestions))

    return responses


def getcategories(name):
    for group in data:
        if name in group['keywords']:
            return group['categories']
    return []


def getco2(name):
    for group in data:
        if name in group['keywords']:
            return group['co2']

# Will return the set of names for the most similar


def mostsimilar(categories, co2):
    mostsim = 0.0
    currentsim = []

    for item in data:
        if item['co2'] < co2:
            try:
                sim = similar(categories, item['categories'])
                if (sim > 0.5):
                    if sim > mostsim:
                        currentsim = item['keywords']
                        mostsim = sim
                    elif sim == mostsim:
                        currentsim = currentsim + item['keywords']

            except:
                pass

    return currentsim


def similar(original, new):
    hit = 0.0
    miss = 0.0

    for x in original:
        if x in new:
            hit += 1.0
        else:
            miss += 1.0

    for x in new:
        if x in original:
            hit += 1.0
        else:
            miss += 1.0

    return hit / (hit + miss)


if(__name__ == "__main__"):
    print(getsuggestions(["Asparagus", "Sunflower Seed Oil", "Walnuts", "Mashed Potato"]))
