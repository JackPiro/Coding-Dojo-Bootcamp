console.log("javascript loaded")
var likes = [0,0,0]
var likesElement1 = document.querySelector("#like-counter1");
var likesElement2 = document.querySelector("#like-counter2");
var likesElement3 = document.querySelector("#like-counter3");

function addOne1() {
    likes[0]++;
    likesElement1.innerText = likes[0] + " Like(s)";
}

function addOne2() {
    likes[1]++;
    likesElement2.innerText = likes[1] + " Like(s)";
}

function addOne3() {
    likes[2]++;
    likesElement3.innerText = likes[2] + " Like(s)";
}


// function addOne(id) {
//     var likesElement = document.querySelector(id);
//     console.log(id);
//     console.log(likesElement);
//     console.log(likesElement.innerText);
//     console.log(parseInt(likesElement.innerText))
//     var likes = parseInt(likesElement.innerText);
//     likes++;
//     likesElement.innerText = likes + " Like(s)";
//     // likes[0]++;
//     console.log(likes);
//     // likesElement.innerText = likes[0] + "Like(s)";
// }