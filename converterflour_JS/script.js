
    // Find at least 3 conversion formulas you want to use with your multiconverter.
    // Write a function for each formula.
    // Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
    // Display the conversion results in the browser console.
    // The program should not quit as long as the user wants to continue converting values.
    // If the user chooses a conversion that is not supported, display that in the console.


function convertTbsToMl () {
   var Tbs = window.prompt("how many tablespoon do you want to concert to ml? :")
   return Tbs + " Tablespoons equal " + (Tbs*17.7581630305738) + " ml";
}

function convertMltoL () {
    var ml = window.prompt("how many Milliliters do you want to concert to Liters? :")
    return ml + " Milliliters equal " + (ml*0.001) + " Liters";
 }

 function convertGramsToMl () {
    var grams = window.prompt("how many grams do you want to concert to mililiters? :")
    return grams + " grams equal " + (grams*1.890359168242) + " Milliliters";
 }
 var firstQuestion = 0

 while ( firstQuestion != "No" ){
    firstQuestion = window.prompt("Do you want to convert value, Yes or No ?");
    if (firstQuestion == "No")
        break;
    var secondQuestion = window.prompt("What do you want to convert : tbs to ml, ml to l or grams to ml ?");
     if (secondQuestion == "tbs to ml"){
         alert(convertTbsToMl());
     }else if (secondQuestion == "ml to l"){
         alert(convertMltoL());
     }else if (secondQuestion == "grams to ml"){
         alert(convertGramsToMl());
     }else{
         alert("your answer don't match our propositions")
     }
 }

