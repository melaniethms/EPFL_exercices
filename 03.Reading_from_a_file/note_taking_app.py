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


first_choice = input("What do you want to do ?\nPress 1 for adding a note\nPress 2 for searching your notes\n")

    
if first_choice == "1" :
    note = input("Enter your note :\n")
    file = open("notes.txt", "a")
    file.write("----\n" + note + "\n")
    file.close()
elif first_choice == "2" : 
    search = input("Enter the text to search :\n")
    file = open("notes.txt")
    content = file.read() 
    file.close()
    notes = content.replace("\n", "").split("----") #transform each note into elements of an array (seperated with ----)
    for line in notes :
        if search in line :
            print(line)
else :
    print("I can not opperate this commande")
    
    
    


