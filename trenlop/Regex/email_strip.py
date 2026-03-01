import os

try:
    script_dir = os.path.dirname(__file__)
    fh_path = os.path.join(script_dir, "mbox-short.txt")
    fh = open(fh_path, "r")
    print("Success")
except:
    print("File cannot be opened:", "mbox-short.txt")
    quit()

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
fh.close()
