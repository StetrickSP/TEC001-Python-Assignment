s = input("Enter your sentence: ")

length = len(s)
mid = int(length/2)

if length % 2 == 0:
    print(f"Middle two characters: {s[mid-1:mid+1]}")
else: 
    print(f"Middle character: {s[mid]}")