#Given in km convert to kg
def calctrainfromdistance(distance): 
    return 0.041 * distance

if(__name__== "__main__"): 
    print(calctrainfromdistance(400))