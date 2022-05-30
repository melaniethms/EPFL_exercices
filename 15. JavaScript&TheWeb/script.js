const title = document.getElementById("title");
const myButton = document.getElementById("myButton");
const myText = document.getElementById("myText");

function changeTitle() {
    title.innerText = myText.value;
}

myButton.addEventListener("click", changeTitle);