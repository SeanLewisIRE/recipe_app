
function createList(arr) {
    let list = "<ul>"
    for (let i = 0; i < arr.length - 1; i++) {
        list += `<li>${arr[i]}</li>`
    }
    list += "</ul>"
    return list
}

let ingredientsArr = ingredientsTotal.split('.');
let instructionsArr = instructionsTotal.split('.');
document.querySelector(".ingredients").innerHTML = createList(ingredientsArr);
document.querySelector(".instructions").innerHTML = createList(instructionsArr);
