import openfoodfacts
import json
# from pattern.en import singularize

with open('/Users/findlaysmith/Documents/food_co2/backend/keywords.json') as f:
    data = json.load(f)
keywords = data

# for x in data:
#     for y in x:
#         keywords.append(singularize(y.lower().replace(" ", "")))


def getingredients(barcode):
    product = openfoodfacts.products.get_product(barcode)

    if(int(product['status']) == 0):
        print(product['status_verbose'])
        return []
    else:
        product = product['product']

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

    # ingredients = list()
    # for ingredient in finalingredients:
    #     ingredients.append(singularize(ingredient))

    return finalingredients


def filteringredients(ingredient):
    return (ingredient in keywords)


def remduplicates(input):
    result = list()

    for x in input:
        if not (x in result):
            result.append(x)

    return result


if(__name__ == "__main__"):
    print(getingredients("51000005"))
