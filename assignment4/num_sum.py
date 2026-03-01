import re

def num_sum(sen: str):
    nums = re.findall(r"([0-9]+)", sen)
    return sum(int(num) for num in nums)

## test cases 
cases = ["Today is January 16, 2025. The temperature is 11 degrees Celsius.", "I have 20 apples, 5 bananas and 2 pineapples."]

for case in cases:
    print(num_sum(case))