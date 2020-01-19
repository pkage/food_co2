import json

with open('backend/pollution.json') as f:
    data = json.load(f)

current = dict()

#Will return a dictonary of suggestions
def getsuggestions(ingredients): 
    responses = dict()
    responses['ingredients'] = list()

    for ingredient in ingredients: 
        current = {}
        current['co2'] = getco2(ingredient)
        current['ingredient'] = ingredient
        categories = getcategories(ingredient)
        suggestions = mostsimilar(categories, current['co2'])

        current['suggestions'] = suggestions
        responses['ingredients'].append(current)
    
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

# Will return the dictonary for similar better items
def mostsimilar(categories, co2):
    mostsim = 0.0
    currentsim = list()

    for item in data:
        if item['co2'] < co2:
            try:
                sim = similar(categories, item['categories']) 
                if (sim > 0.5):  
                    if sim > mostsim: 
                        currentsim = []
                        mostsim = sim
                    #    currentsim = item['keywords']
                    #    mostsim = sim
                    #elif sim == mostsim: 
                    #    currentsim = currentsim + item['keywords']
                    
                    #for i in item['keywords']: 
                    #    curr = dict()
                    #    curr['co2'] = item['co2']
                    #    curr['suggestion'] = i
                    #    currentsim.append(curr)
                    
                    curr = dict()
                    curr['co2'] = item['co2']
                    curr['suggestion'] = item['keywords'][0]
                    currentsim.append(curr)

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