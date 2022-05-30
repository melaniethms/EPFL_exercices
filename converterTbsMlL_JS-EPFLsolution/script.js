
    // Find at least 3 conversion formulas you want to use with your multiconverter.
    // Write a function for each formula.
    // Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
    // Display the conversion results in the browser console.
    // The program should not quit as long as the user wants to continue converting values.
    // If the user chooses a conversion that is not supported, display that in the console.


function convertTbsToMl (Tbs) {
    return Tbs*17.7581630305738;
}

function convertMltoL (ml) {
    return ml*0.001;
 }

 function convertGramsToMl (grams) {
    return grams*1.890359168242;
 }

 function askContinue() {
    var answer = window.prompt("Do you want to convert a value ? (yes/no)")
    if(answer == "yes"){
        return true ;
    }else {
        return false;
    }
 }

 function askConversion() {
    var answer = window.prompt("Which conversion do you want to make ?(tbs to ml, ml to l, grams to ml");
    return answer;
 }

function askValue() {
    var answer = window.prompt("enter an value: ");
    return answer;
}

while(askContinue()){
    var conversionType = askConversion();
    var conversionValue = askValue();
    var resultMessage = "the result is ";
    var result = 0;

    if (conversionType == "tbs"){
        resultMessage += convertTbsToMl(Number(conversionValue)).toString();
    }else if (conversionType == "ml"){
        resultMessage += convertMltoL(Number(conversionValue)).toString();
    }else if (conversionType == "grams"){
        resultMessage += convertGramsToMl(Number(conversionValue)).toString();
    } else {
        resultMessage = "Sorry I can't do this conversion"
    }

    alert(resultMessage)
}