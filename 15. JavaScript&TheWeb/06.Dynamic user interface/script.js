const addButton = document.getElementById("addButton");
const removeButton = document.getElementById("removeButton");
const clearButton = document.getElementById("clearButton");
const myText = document.getElementById("myText");
const content = document.getElementById("content");


function addParagraph(){
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    newParagraph.className = "newItem";
    content.appendChild(newParagraph);
    const newItemIdx = content.children.length - 1;
    localStorage.setItem("element-"+newItemIdx, myText.value )
}

function removeLastParagraph(){
    const paragraphs = document.getElementsByClassName("newItem");
    if(paragraphs.length > 0){
        const newItemIdx = content.children.length - 1;
        localStorage.removeItem("element-"+newItemIdx)
        content.removeChild(paragraphs[paragraphs.length])

    }
}

function clearParagraph(){
    //     [...  ] = cloner le tableau pour que le total length reste le même pendant la boucle
    const paragraphs = [...document.getElementsByClassName("newItem")];
    if(paragraphs.length > 0){
        for(let i=0; i < paragraphs.length;i++){
            content.removeChild(paragraphs[i]);
        }
        localStorage.clear();   
    }
}


addButton.addEventListener("click", addParagraph);
removeButton.addEventListener("click", removeLastParagraph);
clearButton.addEventListener("click", clearParagraph);

// Exercice :
// -les textes devront apparaître dans le block gris en haut de page
// -button Add item = ajouter un nouveau text dans le block + dans le storage 
// -button Remove last item = enlever le dernier text dans le block + dans le storage + pas d'erreur si on supprime du texte alors qu'il n'y en a plus 
// -button Clear all = enlever tous les textes à l'écran et dans le storage +pas d'erreur si on supprime du texte alors qu'il n'y en a plus 
