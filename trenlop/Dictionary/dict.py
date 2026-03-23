## Count dict
# count = dict()
# names = ['khai', 'tai', 'bao', 'gay', 'thinh', 'vinh', 'thinh']

# for name in names:
#     if name not in count: count[name] = int(1)
#     else: count[name] = count[name] + 1
#     print(count)


## words count in mbox-short.txt count
# hand = open('mbox-short.txt')

# words = dict()

# for line in hand:
#     for word in line.split():
#         if word not in words: words[word] = int(1)
#         elif word in words: words[word] += 1

# print(words)


## email counts in mbox-short.txt count
import re
hand = open('mbox-short.txt')

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails_count = dict()
count = int()

for line in hand:
    emails = re.findall(email_pattern, line)
    for email in emails:
        if email not in emails_count: emails_count[email] = int(1)
        elif email in emails_count: emails_count[email] += 1

for mail, num in emails_count.items():
    print(f'{mail} appeared {num} times')
print("Total occurances of emails:", sum(emails_count.values()))

