
def checkHemo(gender, hemo):
    if gender == "M":
        if hemo < 117: print("Too low for an adult male.")
        elif hemo >= 117 and hemo <= 155: print("Fine.")
        else: print("Too high for an adult male.")
    elif gender == "F":
        if hemo < 134: print("Too low for an adult female.")
        elif hemo >= 134 and hemo <= 167: print("Fine.")
        else: print("Too high for an adult female.")
    else: print("Error.")

a = input('Enter gender (M/F):')
b = int(input('Enter hemoglobin value:'))

checkHemo(a,b)

