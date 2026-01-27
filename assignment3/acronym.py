s = input("Enter your phrase: ").upper().split(" ")
res = ""

for i in s:
    res += i[0]
print(res)