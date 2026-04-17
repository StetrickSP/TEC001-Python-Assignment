def convert_to_uppercase(input_file):
    with open(input_file, 'r', encoding="utf-8") as infile:
        content = infile.read()
    
    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(content.upper())

convert_to_uppercase("thinhgay.txt")