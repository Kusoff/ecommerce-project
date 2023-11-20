const repeatPassword = document.querySelector('#id_0-password2');
const helpText = document.querySelector('.helptext');

// Repeat password margin + show texthelp
repeatPassword.addEventListener ('focus', function () {
    this.style.marginTop = '50px';
    helpText.style.opacity = 100;
});

repeatPassword.addEventListener('blur', function () {
    this.style.margin = '10px';
    helpText.style.opacity = 0;
});
