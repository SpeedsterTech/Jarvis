const submit = document.getElementById("submit")
let gname = document.getElementById("GName")
let gpic = document.getElementById("file")

submit.addEventListener("click", function newGame(){
   let send = {}
   send.name = gname.value
 const request = new Request("/api/game", {
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(send)
 })
 const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
  })
})