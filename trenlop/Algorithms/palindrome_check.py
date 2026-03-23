def palindrome_check(word: str):
    rev = word[::-1]
    if rev == word: print(f"{word} is a palindrome")
    else: print(f"{word} is not a palindrome")

palindrome_check("racecar")
palindrome_check("gay")
palindrome_check("tenet")


