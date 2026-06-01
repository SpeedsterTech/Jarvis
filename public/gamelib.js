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
        buttName = "CardButton"+ String(i)
        butt = document.createElement("button")
        butt.id = buttName
        node.appendChild(butt)

            let CardButton = document.getElementById(buttName)
            CardButton.addEventListener("click", function butclick() {
                name  = CardButton.children[0].children[1].children[0].innerHTML
                console.log("Card Clicked")
                console.log(name)
                let send = {}
                send.name = name
                request = new Request('api/gamesPage', {
                    method: "POST",
                    headers: {'Content-Type' : "application/json"},
                    body: JSON.stringify(send)
                })
                console.log("sent")
            })

        cl = document.createElement("div");
        cl.className = "card"
        butt.appendChild(cl)
        
        img = document.createElement("img");
        img.src = data[i][data[i].length -1]
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

        co = document.createElement("div")
        co.className = "con-container"
        cl.appendChild(co)
        if(data[i].length > 2){
            for(let j =1; j < data[i].length-1; j++){
                cons = document.createElement("div")
                cons.className = data[i][j].toLowerCase()
                co.appendChild(cons)

            }
        }
    }
  })