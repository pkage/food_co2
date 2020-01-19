# Takes minutes and spits out kg of C02
# Based on the UK government
# 2.7 is due to "Radiative forcing"


def calcflightfromdistance(distance):
    return distance * 0.158 * 2.7

# Given in minutes and returns kg, based on uk gov figures


def calcflightfromtime(time):
    return (float(time)/60.0) * 134 * 2.7
