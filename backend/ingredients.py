import openfoodfacts
import json
import inflect

p = inflect.engine()

with open('backend/keywords.json') as f:
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
        
        #keywords.append(t)

def __getingredients(barcode): 
    product = openfoodfacts.products.get_product(barcode)

    if(int(product['status']) == 0):
        print(product['status_verbose'])
        return {"ingredients":[], "quantity": "0 g"}
    else:
        product = product['product']

        ingredients = product['ingredients']

        ingredients = extractingredients(ingredients)

        ingredients = list(filter(filteringredients, ingredients))

        ingredients = remduplicates(ingredients)

        if not ("quantity" in product):
            product["quantity"] = "1 kg"

        return {"ingredients": ingredients, "quantity": product["quantity"]}

def getingredients(barcode):
    return __getingredients(barcode)["ingredients"]

def getingredientswithquantity(barcode):
    return __getingredients(barcode)


def extractingredients(ingredients):
    finalingredients = list()
    
    #print(ingredients)

    if len(ingredients) > 1: 
        for ingredient in ingredients: 
            finalingredients.append(ingredient['id'][3:].replace("-"," ").lower())
        
        ingredients = finalingredients
        finalingredients = list()

        for ingredient in ingredients:
            finalingredients.append(ingredient)
            if " " in ingredient:
                i = ingredient.split(" ")
                for x in i:
                    finalingredients.append(x)

    elif (len(ingredients) == 1): 
        finalingredients = ingredients[0]['id'][3:].lower().split(' ').replace("-"," ")
   
    else:
        return []
    
    ingredients = list()
    for ingredient in finalingredients: 
        translated = p.singular_noun(ingredient)
        if (translated != False): 
            ingredients.append(translated)
        else: 
            ingredients.append(ingredient)
        #ingredients.append(ingredient)

    # ingredients = list()
    # for ingredient in finalingredients:
    #     ingredients.append(singularize(ingredient))

    return finalingredients


def filteringredients(ingredient):
    ingredient = ingredient.replace(" ","")
    return (ingredient in keywords)


def remduplicates(input):
    result = list()

    for x in input:
        if not (x in result):
            result.append(x)

    return result

if(__name__== "__main__"): 
    print(__getingredients("00819060"))
