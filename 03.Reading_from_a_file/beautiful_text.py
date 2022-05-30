import io
text_file = io.open("ugly_text.txt", mode = "r", encoding='utf-8')

phrases = text_file.split(".")
print(phrases)

text_file.close()