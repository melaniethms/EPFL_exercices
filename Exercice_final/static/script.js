// /index page :


function SaveUserName(){
    if(localStorage.getItem('User Name') == null) {
        UserName = window.prompt("Quel est votre prénom ? ");
        localStorage.setItem ("User Name", UserName);
        alert("welcome " + UserName);
    } 
}

function UseUserName(){
    var UserNameStored = localStorage.getItem('User Name');
    const element = document.getElementById('welcome');
    element.innerHTML = "welcome back " + UserNameStored;
}

SaveUserName();

UseUserName();



