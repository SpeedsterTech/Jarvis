let send = {}
let node = document.getElementById("cc")
send.mess = "Girl idk"
request = new Request("/api/gamelib",{
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(send)
})

const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
    for(let i =0; i< data.length; i++){
        cl = document.createElement("div");
        cl.className = "card"
        node.appendChild(cl)

        img = document.createElement("img");
        img.src = data[i][1]
        img.width = 200;
        img.height = 200;
        cl.appendChild(img)

        cd = document.createElement("div");
        cd.className = "card-Desc"
        node.appendChild(cd)

        desc = document.createElement("h4");
        desc.innerHTML = data[i][0]
        cd.append(desc)

        cl.appendChild(cd)
        if(data[i].length > 2){
            for(let j =2; j < data[i].length; j++){
                cons = document.createElement("div")
                cons.className = data[i][j].toLowerCase()
                cl.appendChild(cons)

            }
        }
    }
  })