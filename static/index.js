function onButtonClick() {
    const textbox = document.getElementById("name");
    const theText = textbox.value;
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(theText));
    ul.appendChild(li);
}