import openfoodfacts
import json

# Util functions, all take barcodes


def getname(barcode):
    product = openfoodfacts.products.get_product(barcode)
    if(int(product['status']) == 0):
        print(product['status_verbose'])
        return []
    else:
        product = product['product']
        try:
            return product['product_name_en']
        except:
            return product['product_name']


def containspalm(barcode):
    product = openfoodfacts.products.get_product(barcode)
    if(int(product['status']) == 0):
        print(product['status_verbose'])
        return False
    else:
        palmoil = 0
        try:
            product = product['product']
            palmoil += product['ingredients_from_or_that_may_be_from_palm_oil_n']
            palmoil += product['ingredients_from_palm_oil_n']
        except:
            pass
        return (palmoil > 0)


def printfields(barcode):
    product = openfoodfacts.products.get_product(barcode)
    if(int(product['status']) == 0):
        print(product['status_verbose'])
        return []
    else:
        product = product['product']
        for x in product:
            print(x)


if(__name__ == "__main__"):
    barcode = "20675615"
