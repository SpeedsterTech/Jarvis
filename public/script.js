const textBtn = document.getElementById("txtBtn")
const voiceBtn = document.getElementById("voiceBtn")
const submit = document.getElementById("submit")
const newUseBtn = document.getElementById("NewUserBtn")
const LoginBtn = document.getElementById("Login")
const userLabel = document.getElementById("userLabel")
const passLabel = document.getElementById("passLabel")
let user = document.getElementById("User")
let pass = document.getElementById("Pass")
let query = document.getElementById("query")
let log = document.getElementById("response")
let send = {}
textBtn.style.display = "none"
voiceBtn.style.display = "none"
query.style.display = "none"
submit.style.display = "none"
label.style.display = "none"
newUseBtn.style.display = "none"


LoginBtn.addEventListener("click", function Login() {
  login = {}
  login.actionType = "login"
  login.user = user.value;
  login.pass = pass.value;
  request = new Request("/api/action", {
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(login)
  })
  const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
  })
     
  LoginBtn.style.display = "none"
  userLabel.style.display = "none"
  passLabel.style.display = "none"
  user.style.display = "none"
  pass.style.display = "none"
  textBtn.style.display = "inline"
  voiceBtn.style.display = "inline"
})

textBtn.addEventListener("click", function Text() {
  textBtn.style.display = "none"
  voiceBtn.style.display = "none"
  query.style.display = "block"
  submit.style.display = "block"
  label.style.display = "block"
})

voiceBtn.addEventListener("click", function Voice(){
  textBtn.style.display = "none"
  voiceBtn.style.display = "none"
  getLocalStream()
})

submit.addEventListener("click", function Query(){
  send.actionType = "query"
  console.log(query.value)
  log.innerHTML += "USER: " + query.value + "<br>";
  send.query = query.value;
  request = new Request("/api/action", { // remember to update port
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(send),
  });
  const response = fetch(request).then((responce) => responce.json()).then(data => {
    console.log(data);
    log.innerHTML += "JARVIS: " + data +"<br>"
  })
})

function getLocalStream() {
  navigator.mediaDevices
    .getUserMedia({ video: false, audio: true })
    .then((stream) => {
      window.localStream = stream; // A
      window.localAudio.srcObject = stream; // B
      window.localAudio.autoplay = true; // C
    })
    .catch((err) => {
      console.error(`you got an error: ${err}`);
    });
}

