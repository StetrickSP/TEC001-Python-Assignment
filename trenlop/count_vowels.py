def count_vowels():
    s = input("Please write a sentence: ")
    s = s.lower()

    count = 0

    for i in s:
        if i in ["a", "e", "i", "o", "u"]:
            count += 1
    print("Total vowels:", count)

count_vowels()