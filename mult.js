app.post('/api/games', function(req,res) {
  console.log("Beginning of the post")
  const storage = multer.diskStorage({
    destination: function(req, file,cb) {
      cb(null,"uploads")
    },
    filename: function (req,file,cb) {
      console.log(req.body + "\n")
      console.log(file)
      x = file.originalname.split(".")
      cb(null,req.body.gName + "." + x[x.length-1]);
    }
  });
  
  const upload = multer({storage: storage})
  upload.single("file")
  console.log("End of post")

})