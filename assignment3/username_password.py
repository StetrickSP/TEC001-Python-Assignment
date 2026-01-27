user = input("Enter username: ")
pw = input("Enter password: ")

for i in range(5):
    if user != "python" or pw != "rules":
        user = input("Enter username again: ")
        pw = input("Enter password again: ")
    elif user == "python" and pw == "rules":
        print("Welcome")
        break

if user != "python" or pw != "rules": print("Access denied.")


    

    