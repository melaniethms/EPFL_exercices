function call(msgBefore, msgAfter, fn){
    console.log(msgBefore);
        fn();
        console.log(msgAfter);
}

function display(){
    console.log("called inside the function!");
}

call("Before", "After", display)

// call("Before", "After", function(){
//     console.log("called inside the function");
// });