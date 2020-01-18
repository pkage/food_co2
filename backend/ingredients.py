import openfoodfacts

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
            finalingredients.append(ingredient['text'])

    else: 
        finalingredients = ingredients[0]['text'].split(' ')
        
    return finalingredients

def filteringredients(ingredient): 
    #Need to filter that in the ingredient list    
    return True


if(__name__== "__main__"): 
    print(getingredients("51000005"))
    print(getingredients("5060088701942"))