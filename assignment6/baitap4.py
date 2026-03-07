# Write a function that will determine the frequency of a word (i.e. how many times does a word appears) in a given piece of text. Hint: Use the dictionary data structure.

def word_frequency(word, text):
    words = text.split()
    freq = 0

    for i in words:
        i = i.lower()
        if i == word:
            freq += 1

    return freq

word = 'i'
text = input("Enter text: ")
result = word_frequency(word, text)

print(result)