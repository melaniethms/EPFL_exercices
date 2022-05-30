var day = 3; 

// if(day === 1){
//   console.log("Monday");
// }else if(day === 2){
//   console.log("Tuesday");
// }else if(day === 3){
//   console.log("Wednesday");
// }else if(day === 4){
//   console.log("Thursday");
// }else if(day === 5){
//   console.log("Friday");
// }else{
//   console.log("It's the weekend!");
// }


// if(day === 1 || day === 2 || day === 3 || day === 4 || day === 5){
//   console.log("Week day");
// }else if(day === 6 || day === 7){
//   console.log("Weekend");
// }else{
//   console.log("Not a valid day");
// }

switch (day) {
    case 1 : 
        console.log("Monday");
        break;
    case 2 : 
        console.log("Tuesday");
        break;
    case 3 : 
        console.log("Wednesday");
        break;
    case 4 : 
        console.log("Thursday");
        break;
    case 5 : 
        console.log("Friday");
        break;
    default : 
        console.log("Weekend");
        break;
}

switch (day){
    case 1 :
    case 2 : 
    case 3 : 
    case 4 : 
    case 5 : 
        console.log("Week day");
        break;
    case 6 :
    case 7 : 
        console.log("Weekend");
        break;
    default : 
    console.log("Not a valid day");
    break;
}