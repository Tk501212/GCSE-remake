function checkQ1() {
    //get the user's answer
    var userAnswer = document.getElementById("q1-answer").value

    //check it against the correct answer
    if (userAnswer == "40"){
     //if correct answer box colour green
        document.getElementById("q1-answer").style.backgroundColor = "green"
    } else {
     //if wrong colour box colour red
        document.getElementById("q1-answer").style.backgroundColor = "red"
    }
}