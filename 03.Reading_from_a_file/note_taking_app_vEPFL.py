# I enter the programme 
# I get a message that let me choose between 2 options : 
#     option one : adding a note 
#     option two : searching for a note
# if I write "1" :
#   I get a message "Enter your note :" under which I can write a note. 
#     when clicking "enter" it saves the note in my text file "notes.txt" under some specials characteres "---" 
#     then either the programme quit or I get asked again what option I want (I can choose while writing the programme)
# if I select write "2" :
#   I get a message "Enter the text to search :" under which I can write a word to search.
#     when clicking "enter", the programme looks for this specific word in my notes and print notes (with their special characters) in which it did find the word
#     then quit or replay

# Create a note
def write_note(text):
    file = open("noteapp.txt", "a")
    file.write("----\n")
    file.write(text + "\n")
    file.close()

# Search through notes 
def search(text):
    file = open("noteapp.txt")
    content = file.read()
    file.close()
    result = ""
    notes = content.split("----")

    for note in notes:
        if note.find(text) != -1:
            result += "\n----" + note

    if result == "":
        print("Nothing found!")
    else:
        print(result)

# Display menu
print("What do you want to do?")
print("Press 1 for adding a note")
print("Press 2 for searching your notes")
answer = input(": ")

# Execute task based on menu input
if answer == "1":
    print("Enter your note:")
    note = input().strip()
    write_note(note)
elif answer == "2":
    print("Enter the text to search:")
    text = input().strip()
    search(text)
else:
    print("Sorry! I didn't understand that")
    
    
    

