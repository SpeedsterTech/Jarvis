var fs = require('fs');
const {PythonShell} = require("python-shell");
const express = require('express');
const multer = require('multer');
const app = express()
app.use (express.json());
app.use(express.static('public'));
app.use(express.static('uploads'));
let newGname;

app.post('/api/action', (req,res) => {
  const body = req.body;
  if(body.actionType == 'login'){
    message ="Username: " +  body.user + ", Password: " + body.pass + "\n";
    console.log(body);
    res.json("yippie");
  }else if(body.actionType == "query"){

    message = body.query + "\n";
    console.log(body.query);
    let options = {
    args:[body.query]
    };
    PythonShell.run("webJar.py",options, (err, res) => {
        if(err) {
            console.log(err);
            console.log('failure');
        }else if (res){
            console.log(res);
            console.log('success');
        }
    });
    while(unchanged){
      unchanged = true
      x = fs.readFile('answer.txt', (err,data) => {
        if(String(data) != prevR && String(data) != ''){
          prevQ = body.query
          prevR = data
          res.json(String(data));
          unchanged = false
      }
      });
  }
  } 
  
})

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads");
  },
  filename: function (req, file, cb) {
    console.log(file)
    x = file.originalname.split(".")
    newGname = file.fieldname+ "-" +file.originalname +"." + x[x.length-1]
    cb(null,newGname);
    fs.appendFile('games.csv', newGname + "\n", (err) => {
      if(err){
        console.log(err)
      }
    })
  }
});

const upload = multer({ storage: storage })

app.post('/upload',upload.single("file"), (req,res) => {
  newGname=req.file
  console.log("lets go")
  res.redirect('gameLib.html')
});
app.post('/api/game', (req,res) => {
  body = req.body
  console.log(body)
  console.log(newGname)
  fs.appendFile('games.csv',body.name +",", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("Name Logged!")
    }
  })
  if (body.PS){
    fs.appendFile('games.csv',"Playstation,", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("PS Logged!")
    }
    })
  }
  if(body.X){
    fs.appendFile('games.csv',"Xbox,", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("Xbox Logged!")
    }
    })
  }
  if(body.NS){
    fs.appendFile('games.csv',"Nintendo,", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("Switch Logged!")
    }
    })
  }
  if(body.S){
    fs.appendFile('games.csv',"Steam,", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("Steam Logged!")
    }
  })
  }
});

app.post('/api/gamelib', (req,res) => {
  const body = req.body
  let games = [];
  fs.readFile('games.csv', 'utf8', (er, data) => {
    x = data.split("\n")
    for (let i = 0; i < x.length-1; i++) {
      let c = x[i].split(",");
        games.push(c);
    }
    res.json(games)
  })
});

app.post('/api/gamesPage', (req,res) => {
  console.log("recieved a thing for a game page")
  const body = req.body
  console.log(req.body)
});

app.listen(3000, () => {
   const addressInfo = app.address();
    console.log(`Server is running on port: ${addressInfo.port}`);
    console.log(`Bound Address: ${addressInfo.address}`); 
})