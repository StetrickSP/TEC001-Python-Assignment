import random

code_3 = [str(random.randint(0, 9)) for _ in range(3)]
code_4 = [str(random.randint(1, 6)) for _ in range(4)]
ans_3 = ''
ans_4 = ''

for i in code_3:
    ans_3 += i

for i in code_4:
    ans_4 += i

print("3-digit code:", ans_3)
print("4-digit code:", ans_4)
