const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

const USER = "jason123";
const PASS = "1420"

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === USER && password === PASS) {
        window.location.href = "login-success.html";
        // location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})