let send = {}
send.mess = "Girl idk"
request = new Request("/api/gamelib",{
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(send)
})

const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
  })