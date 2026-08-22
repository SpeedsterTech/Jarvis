const submit = document.getElementById("submit")
let gname = document.getElementById("GName")
let gpic = document.getElementById("file")
let PS = document.getElementById("PS")
let X = document.getElementById("Xbox")
let S = document.getElementById("Steam")
let NS = document.getElementById("NS")
submit.addEventListener("click", function newGame(){
   let send = {}
   send.name = gname.value
   send.PS = PS.checked
   send.X = X.checked
   send.S = S.checked
   send.NS = NS.checked
    window.location.href = "/gamelib.html";
 const request = new Request("/api/game", {
   method: "POST",
   headers: {'Content-Type' : "application/json"},
   body: JSON.stringify(send)
   
 })
  
 const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
  })

})