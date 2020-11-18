
/*function verifyQuestion(correctAnswer){
    alert(page)
    let score = document.getElementById("score")
    const radios = document.getElementsByName('answers');
    let i = 0, length = radios.length;
    for (; i < length; i++) {
        if (radios[i].checked) {
            if(radios[i].value == answer){
                alert("correct answer")
            }
            else {
                alert("Incorrect answer")
            }
            window.open("http://127.0.0.1:8000/quizMode/page="+page);
        }
    }
    let choiceAnswer = document.querySelector('input[name=answer]:checked').value;
    document.querySelector("#response").textContent='the checked value = ' +choiceAnswer;
}*/

function answernames(correctAnswer,desc){
    //alert(correctAnswer);
    //let score = document.getElementById("score")
    answerdisplay = document.querySelector('input[name=answer]:checked').value;
    if(answerdisplay == correctAnswer){
          document.querySelector("#correct").textContent = "GOOD YOUR ANSWER IS CORRECT ";
          //score.innerText = score.innerText + 5;
    }else {
        document.querySelector("#incorrect").textContent = " YOUR ANSWER NOT CORRECT "
    }
     document.querySelector("#description").textContent = "Definition : "+ desc

}