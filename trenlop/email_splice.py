s = input("Enter email address: ")

if s.count("@") == 1:
    at = s.find("@")
    username = s[0:at]
    domain = s[at:len(s)]
    print(f"User {username} is logged in from {domain}")
else: print("Error, inappropriate email.")