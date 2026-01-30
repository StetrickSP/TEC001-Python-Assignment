def small_search(x: list):
    res = x[0]
    for i in x:
        if i < res: res = i
    return res

def large_search(x: list):
    res = x[0]
    for i in x:
        if i > res: res = i
    return res

def main():
    l = []

    s = input("Enter your number (type nothing to exit): ")
    if s != "":
        s = int(s)
        l.append(s)

    while s != "":
        s = input("Enter your next number (type nothing to exit): ")
        if s != "":
            s = int(s)
            l.append(s)

    print("List:", l)
    print(f'The smallest number received: {small_search(l)} \nThe largest number received: {large_search(l)}')

if __name__ == "__main__":
    main()

