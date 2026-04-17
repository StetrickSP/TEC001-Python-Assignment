def calc_avg_score(filename):
    total = 0
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            total += float(score)
            count += 1
    
    if count == 0:
        return 0
    
    return total / count

print(calc_avg_score("info.txt"))