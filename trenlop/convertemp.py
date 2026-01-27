def calcFTemp(CTemp):
    tempF = (CTemp * 9/5) + 32
    print("Temperature in Fahranheit: ", tempF)
    if tempF >= 90: print("It is a hot day!") 
    elif tempF <= 32: print("It is freezing!")
    else: print("It is a pleasant day.")

temp = int(input("Enter the Celsius temperature: "))

calcFTemp(temp)

