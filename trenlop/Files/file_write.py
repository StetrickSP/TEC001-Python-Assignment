filename = "mbox-short.txt"

with open(filename, 'w', encoding="UTF-8") as file:
    file.write("Thịnh Gầy Béo Ốm Chỉ hông tới Racist Nigga Nigga bucu Hết lớp \n"*7)

with open(filename, "r", encoding="UTF-8") as file:
    content = file.read()
    print(content)