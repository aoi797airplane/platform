var pw = document.getElementById('id_password');
var pwCheck = document.getElementById('password-check');
pwCheck.addEventListener('change', function() {
    if(pwCheck.checked) {
        pw.setAttribute('type', 'text');
    } else {
        pw.setAttribute('type', 'password');
    }
}, );