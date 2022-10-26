console.log("javascript loaded...")
var likes = [0,0,0]
var likesElement1 = document.querySelector("#like-counter1");
var likesElement2 = document.querySelector("#like-counter2");
var likesElement3 = document.querySelector("#like-counter3");

function addOne1() {
    likes[0]++;
    likesElement1.innerText = likes[0] + " Petting(s)";
}

function addOne2() {
    likes[1]++;
    likesElement2.innerText = likes[1] + " Petting(s)";
}

function addOne3() {
    likes[2]++;
    likesElement3.innerText = likes[2] + " Petting(s)";
}

function hideBtn(element) {
    element.remove();
}


function alertFunction1(element){
    if(element == 0)
        alert("You have selected all pets.");
        console.log(element);
}

function alertFunction2(select) {
    alert(select.options[select.selectedIndex].text);
    }