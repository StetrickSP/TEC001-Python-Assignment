import re

def hashtag_find(text:str): 
    return re.findall(r"#(\w+)", text)

def email_find(text:str): 
    return re.findall(r"\w+@\w+.com", text)

posts = ["Learning with stetrick@gmail.com!", "Eating #apples to keep the footdocdana@gmail.com away!", "Top 10 most common #fallacies"]

for post in posts:
    print(hashtag_find(post))

for post in posts:
    print(email_find(post))
