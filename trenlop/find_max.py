a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def findMax(a, b, c):
    if a < b: a = b
    if a < c: a = c
    return a

print(findMax(a,b,c))
