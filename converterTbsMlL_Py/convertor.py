# Find at least 3 conversion formulas you want to use with your multiconverter.
# Write a function for each formula.
# Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
# Display the conversion results in the browser console.
# The program should not quit as long as the user wants to continue converting values.
#  If the user chooses a conversion that is not supported, display that in the console.

def convert_tbs_to_ml(tbs):
    return tbs*17.7581630305738
def convert_ml_to_l(ml):
    return ml*0.001
def convert_grams_to_ml(grams):
    return grams*1.890359168242

def ask_continue() :
    answer = input("Do you want to convert a value ? (yes/no)")
    if answer == "yes" :
        return True
    else :
        return False

def ask_conversion():
    answer = input("Which conversion do you want to make ?(tbs to ml, ml to l, grams to ml) ")
    return answer 

def ask_value():
    answer = input("enter an value: ")
    return answer

while ask_continue():
    conversion_type = ask_conversion()
    conversion_value = ask_value()
    result_message = "the result is "
    result = 0

    if conversion_type == "tbs to ml" :
        result_message + convert_tbs_to_ml()
    elif conversion_type == "ml to l" :
        result_message + convert_ml_to_l()
    elif conversion_type == "grams to ml":
        result_message + convert_grams_to_ml()
    else :
        resultMessage = "Sorry I can't do this conversion"
    print(result_message )