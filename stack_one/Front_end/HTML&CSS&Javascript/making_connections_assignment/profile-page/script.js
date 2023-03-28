console.log("page loaded...");
var connectionsRequests = 0
var connections = 0

function jane(element) {
    element.innerText = "Mary J";
}

var friendRequest1 = document.querySelector("#card1");
var friendRequest2 = document.querySelector("#card2");
var acceptedFriend = document.querySelector("#connections");
var requests = 2;
var requestsElement = document.querySelector(".badge");
function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    friendRequest.innerText--;
    console.log(id);
    requests--;
    requestsElement = requests;
    // acceptedFriend.innerText++;
}
