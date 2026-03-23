def factorial(num: int):
    res = 1
    for n in range(1,num+1): 
        res *= n
    print(res)

factorial(5)

def recurve_factorial(n: int):
    if n == 1: return 1
    else: return n * recurve_factorial(n - 1)