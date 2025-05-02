function updateGrid(event){    
    
     if (event.target.innerHTML === ""){
        event.target.innerHTML = turn 
        if (turn === "0"){
             turn = "X"
        } else {
             turn = "0"

        }
    }

}

function checkwin(){
    var topLeft = document.getElementById("top-left").innerHTML 
    var topMid = document.getElementById("top-mid").innerHTML
    var topRight = document.getElementById("top-right").innerHTML

    var centreLeft = document.getElementById("centre-left").innerHTML 
    var centreMid = document.getElementById("centre-mid").innerHTML
    var centreRight = document.getElementById("centre-right").innerHTML

    var bottomLeft = document.getElementById("bottom-left").innerHTML 
    var bottomMid = document.getElementById("bottom-mid").innerHTML
    var bottomRight = document.getElementById("bottom-right").innerHTML

    if (topLeft === topMid === topRight === turn0){
        console.log("win!")
        
    }
}

var turn = "0"




