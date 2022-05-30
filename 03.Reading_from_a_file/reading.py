text_file = open("myfile.txt", encoding='utf-8')

for line in text_file :
    print(line)

text_file.close()