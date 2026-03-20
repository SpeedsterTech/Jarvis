const submit = document.getElementById("submit")
let gname = document.getElementById("GName")
let send = {}

submit.addEventListener("click", function newGame(){
 send.gName = gname.value;
 request = new Request("/api/game", {
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(send)
 })
 const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
  })
})