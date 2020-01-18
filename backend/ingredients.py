import openfoodfacts
import json
from pattern.en import singularize

with open('keywords.json') as f:
  data = json.load(f)
keywords = list()

for x in data: 
    for y in x: 
        keywords.append(singularize(y.lower()))


def getingredients(barcode): 
    product = openfoodfacts.products.get_product(barcode)
    
    #Don't have the product 
    if(int(product['status']) == 0): 
        print(product['status_verbose'])
        return []
    else:
        product = product['product']

        ingredients = product['ingredients']

        ingredients = extractingredients(ingredients)

        ingredients = list(filter(filteringredients, ingredients))
        
        return ingredients

def extractingredients(ingredients): 
    finalingredients = list()
    if len(ingredients) > 1: 
        for ingredient in ingredients: 
            finalingredients.append(ingredient['text'].lower())

    else: 
        finalingredients = ingredients[0]['text'].lower().split(' ')
   
    ingredients = list()

    for x in finalingredients: 
        ingredients.append(singularize(x))

    return ingredients

def filteringredients(ingredient): 
    return (ingredient in keywords)


if(__name__== "__main__"): 
    print(getingredients("51000005"))
    print(getingredients("51000001"))
    print(getingredients("5060088701942"))
