#Takes minutes and spits out kg of C02
#Based on the UK government 
# 2.7 is due to "Radiative forcing"
def calcflightfromdistance(distance):
    return (distance * 0.254)

if(__name__== "__main__"): 
    print(calcflightfromdistance(400))