import openfoodfacts

#Util functions, all take barcodes

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
if(__name__== "__main__"): 
    print(getname("5010044002378"))