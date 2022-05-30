# Find at least 3 conversion formulas you want to use with your multiconverter.
# Write a function for each formula.
# Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
# Display the conversion results in the browser console.
# The program should not quit as long as the user wants to continue converting values.
#  If the user chooses a conversion that is not supported, display that in the console.

tbs = 0
ml = 0
grams = 0


def convert_tbs_to_ml():
    print("the result " + str(int(question_trois)*17.7581630305738) + " ml")
def convert_ml_to_l():
    print("the result is " + str(int(question_trois)*0.001) + " l")
def convert_grams_to_ml():
    print("the result is " + str(int(question_trois)*1.890359168242) + " ml")
question_one = 0

while(question_one != "no"):
    question_one = input("Do you want to convert value, (yes/no) ?")
    if question_one == "no" :
        quit()
    question_deux = input("What do you want to convert : tbs, ml or grams ?")
    question_trois = input("What value do you whant to convert ")
    if question_deux == "tbs" :
        str(convert_tbs_to_ml())
    elif question_deux == "ml":
        str(convert_ml_to_l())
    elif question_deux == "grams" :
        str(convert_grams_to_ml())
    else :
        print("Sorry I can not convert this value")