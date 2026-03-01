import re

hand = open('mbox-short.txt')

def strip_From():
    for line in hand:
        line = line.rstrip()
        print(re.search("^From ", line))

def strip_X():
    count = 0
    for line in hand:
        line = line.rstrip()
        if re.search('^X.*d', line):
            print(line)
            count += 1
    print(count)

strip_X()