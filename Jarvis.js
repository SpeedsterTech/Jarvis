var fs = require('fs');
const {PythonShell} = require("python-shell");
const express = require('express');
const multer = require('multer');
const app = express()
app.use (express.json());
app.use(express.static('public'));


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
    cb(null,file.fieldname+ "-" +file.originalname +"." + x[x.length-1]);
  },
});

const upload = multer({ storage: storage });

app.post('/upload',upload.single("file"), (req,res) => {
  console.log("lets go")
  res.json("yippie")
});
app.post('/api/game', (req,res) => {
  fs.readdir('uploads', (err,files) => {
    files.forEach(file => {
      console.log(file);
    });
  })
});
app.listen(3000, () => {
})