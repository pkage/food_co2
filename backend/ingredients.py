import openfoodfacts
import json
import inflect

p = inflect.engine()

with open('keywords.json') as f:
  data = json.load(f)
keywords = list()

for x in data: 
    for y in x: 
        t = y.lower().replace(" ","")
        tsingle = p.singular_noun(t)

        if (tsingle != False): 
            keywords.append(tsingle)
        else: 
            keywords.append(t)

def getingredients(barcode): 
    product = openfoodfacts.products.get_product(barcode)
    
    if(int(product['status']) == 0): 
        print(product['status_verbose'])
        return []
    else:
        product = product['product']

        try: 
            ingredients = product['ingredients_en']
        except: 
            ingredients = product['ingredients']


        ingredients = extractingredients(ingredients)
        ingredients = list(filter(filteringredients, ingredients))
        
        ingredients = remduplicates(ingredients)

        return ingredients

def extractingredients(ingredients): 
    finalingredients = list()
    
    if len(ingredients) > 1: 
        for ingredient in ingredients: 
            finalingredients.append(ingredient['text'].lower())
        
        ingredients = finalingredients
        finalingredients = list()

        for ingredient in ingredients: 
            finalingredients.append(ingredient)
            if " " in ingredient: 
                i = ingredient.split(" ")
                for x in i: 
                    finalingredients.append(x)

    elif (len(ingredients) == 1): 
        finalingredients = ingredients[0]['text'].lower().split(' ')
   
    else:
        return []
    
    ingredients = list()
    for ingredient in finalingredients: 
        translated = p.singular_noun(ingredient)
        if (translated != False): 
            ingredients.append(translated)
        else: 
            ingredients.append(ingredient)

    return ingredients

def filteringredients(ingredient): 
    return (ingredient in keywords)

def remduplicates(input): 
    result = list()

    for x in input: 
        if not (x in result): 
            result.append(x)

    return result

if(__name__== "__main__"): 
    print(getingredients("51000005"))