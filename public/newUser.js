const submit = document.getElementById("submit")
let username = document.getElementById("name")
let user = document.getElementById("user")
let pass = document.getElementById("pass")


submit.addEventListener("click", function NewUse() {
    userInfo = {}
    userInfo.actionType == 'newUser'
    userInfo.name = username.value;
    userInfo.user = user.value;
    userInfo.pass = pass.value;
    request = new Request("/api/action", {
    method: "POST",
    headers: {'Content-Type' : "application/json"},
    body: JSON.stringify(userInfo)
  })
  const response = fetch(request);
})