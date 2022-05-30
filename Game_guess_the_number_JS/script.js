
    // When starting the game, a secret number between 1 and 100 is generated.
    // The game asks the user to enter a number.
    // The game will tell the user if the secret number is bigger or smaller than the guess.
    // As long as the user doesn't find the secret number, the game continues.
    // As soon as the user finds the secret number, the game stops and tells the user how many attempts it took to win. Make sure to use the right wording (attempt or attempts)
    // In case the user enters anything else than a number, the game should tell that to the user and quit gracefully.

    var RandomNumber = Math.floor(Math.random() * 100);

    function AskUserNumber(){
        answer = window.prompt("guess a number between 1 and 100 :")
        return answer
    }

    function NumberBiggerOrSmaller(number){
        if (RandomNumber > number){
            alert ("try bigger");
        } else if (RandomNumber < number){
            alert ("try smaller");
        }
    }

    var guess = null
    var attempt = 0
        
    while (RandomNumber != guess){
        guess = AskUserNumber();
        NumberBiggerOrSmaller(guess);
        attempt += 1
    }

alert("you found the number after " + attempt + " attempts")