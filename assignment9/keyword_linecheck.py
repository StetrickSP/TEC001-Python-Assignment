def find_keyword_lines(filename, keyword):
    result = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                result.append(i)
    return result

print(find_keyword_lines("mbox-short.txt", "From"))