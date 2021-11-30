function startgame(){
document.getElementById("btnstart").style.visibility="hidden";
document.getElementById("quiz").style.visibility="visible";
document.getElementById("btnsubmit").style.visibility="visible";
document.getElementById("btnreset").style.visibility="visible";
document.body.style.backgroundImage="url('https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg')";


// create a form with JavaScript

createForm();

}

const q1 = {
question : "What is the capital of Japan" ,
options : "Tokyo,Osaka,Nagoya" ,
answer : "Tokyo" 
};

const q2 = {
question : "What is the capital of USA" ,
options : "Washington DC,New York,Chicago" ,
answer : "Washington DC" 
};

const q3 = {
question : "What is the capital of Russia" ,
options : "Moscow,Saint Petersburg,Novosibirsk" ,
answer : "Moscow" 
};

const q4 = {
question : "What is the capital of China" ,
options : "Beijing,Shanghai,Guangzhou" ,
answer : "Beijing" 
};
    
const q5 = {
question : "What is the capital of India" ,
options : "Mumbai,New Delhi,Bangalore" ,
answer : "New Delhi" 
};

const q6 = {
question : "What is the capital of Spain" ,
options : "Madrid,Barcelona,Valencia" ,
answer : "Madrid" 
};

const q7 = {
question : "What is the capital of Italy" ,
options : "Rome,Milan,Naples" ,
answer : "Rome" 
};

const q8 = {
question : "What is the capital of France" ,
options : "Paris,Marseille,Lyon" ,
answer : "Paris" 
};

const q9 = {
question : "What is the capital of Germany" ,
options : "Berlin,Hamburg,Munich" ,
answer : "Berlin" 
};

const q10 = {
question : "What is the capital of Australia" ,
options : "Sydney,Canberra,Melbourne" ,
answer : "Canberra" 
};

var questions= new Array(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)

function createForm(){
var container=document.getElementById("quiz");
var form=document.createElement("form");
container.appendChild(form);
form.setAttribute("name","form1")


for (var i=0 ; i<questions.length ; i++){
    var qs=document.createElement("p");
   // qs.setAttribute("type","text");
    var name="question"+i ;
    qs.setAttribute("id",name);
   // qs.setAttribute("value", questions[i].question);
   //qs.setAttribute("readOnly",true);


    form.appendChild(qs);
    qs.innerText=questions[i].question;

    var br = document.createElement("br");
    var options = questions[i].options;
    var opt = options.split(",");

    for (var j=0 ; j < opt.length ; j++){
        var o=document.createElement("input");
        o.setAttribute("type","radio");
        o.setAttribute("name",name);
        o.setAttribute("value",opt[j]);
        
        form.appendChild(o);
        var lbl = document.createElement("label");
        lbl.innerText=opt[j]
        form.appendChild(lbl)
           
    }

    form.appendChild(br);

}

}

function submit(){

var score = 0
for (i=0; i<questions.length ; i++){
var name="question"+i;
var ans = document.querySelector('input[name="'+name+'"]:checked') ;
var answer = questions[i].answer ;

console.log(ans.value + " "+answer)

if (ans.value==answer) score ++ ;

}

alert("Your score="+score)

}

function reset(){
    for (i=0; i<questions.length ; i++){
var buttons=document.getElementsByName("question"+i);
for (j=0 ; j<buttons.length ; j++){
buttons[j].checked=false ;
}

}
}


// create a submit button (in html)
// 10 questions


