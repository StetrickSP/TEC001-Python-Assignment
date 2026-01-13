def calculatePay(hour, rate):
    if hour <= 40:
        print(hours * rate)
    elif hour > 40:
        print((40 * rate) + (hours - 40) * (rate * 1.5))
    else:
        print("Error")

hours = int(input("Enter hours worked: "))
rate = int(input("Enter rate: "))

while hours < 0 or rate < 0:
    print("Please enter an appropriate hours and rate.")
    hours = int(input("Enter hours worked: "))
    rate = int(input("Enter rate: "))
    
calculatePay(hours, rate)
