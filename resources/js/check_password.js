$(document).ready(function() {
    function checkPassword() {
        var password = $('#password');
        var confirmPassword = $('#confirm-password');
        var message = '';
        if (password.val() != confirmPassword.val()) {
            message = '两次输入的密码不匹配';
        }
        confirmPassword[0].setCustomValidity(message);
    }
    $('#password').change(checkPassword);
    $('#confirm-password').keyup(checkPassword);
});
