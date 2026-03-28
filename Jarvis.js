var fs = require('fs');
const {PythonShell} = require("python-shell");
const express = require('express');
const multer = require('multer');
const app = express()
app.use (express.json());
app.use(express.static('public'));
<<<<<<< HEAD
let newGname = "";

=======
let newGname;
>>>>>>> 12fdd2400bb9ce8b97492053b1cbe7635d5cf6e9

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
    //console.log(file)
    x = file.originalname.split(".")
<<<<<<< HEAD
    newGname = String(file.fieldname+ "-" +x[0] +"." + x[x.length-1])
    cb(null,newGname);
  },
=======
    newGname = file.fieldname+ "-" +file.originalname +"." + x[x.length-1]
    cb(null,newGname);
    fs.appendFile('games.csv', newGname + "\n", (err) => {
      if(err){
        console.log(err)
      }
    })
  }
>>>>>>> 12fdd2400bb9ce8b97492053b1cbe7635d5cf6e9
});

const upload = multer({ storage: storage })

app.post('/upload',upload.single("file"), (req,res) => {
  newGname=req.file
  console.log("lets go")
});
app.post('/api/game', (req,res) => {
  body = req.body
  console.log(body.name)
  console.log(newGname)
<<<<<<< HEAD
  fs.appendFile("game.csv", body.name + ","+ newGname + "\n", (err) => {
    if(err) {
      console.log(err);
    }else{
      console.log("success");
    }
  });
=======
  fs.appendFile('games.csv',body.name +",", (err) =>{
    if(err){
      console.log(err)
    } else {
      console.log("Game Logged!")
    }
  })
>>>>>>> 12fdd2400bb9ce8b97492053b1cbe7635d5cf6e9
});
app.listen(3000, () => {
})