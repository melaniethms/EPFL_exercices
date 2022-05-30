
    # Use Python to count the words in this text file and to display the count in the terminal. Hint: You will first need to get rid of all the special characters.
    # Replace every occurence of the word is with should be.
    # Transform the new text into UPPER CASE.
    # Display the result of your modifications in the terminal. The punctuation and special characters have to be there as well!


text_file = open("Zen_of_python.txt", mode = "r", encoding='utf-8')
content =text_file.read()

word_count = content.replace("-","").replace(".", "").replace("!", "").replace("'", " ").replace("*", "").replace(",", "").replace("\n", " ").replace("  ", " ").split(" ")

print(len(word_count))

new_text= content.replace("is", "should be").upper()
print(new_text)

text_file.close()
