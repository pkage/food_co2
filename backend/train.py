#Given in km convert to kg
def calctrainfromdistance(distance): 
    return 0.041 * distance

#Time given in minutes returned in kg
def calctrainfromtime(time): 
    return 0.041 * (time / 60.0) * 100.0