var a = document.getElementById("idi");

function clickOn(){
    a.innerHTML = Math.random().toString(36).slice(2) + Math.random().toString(36).toUpperCase().slice(2);
}