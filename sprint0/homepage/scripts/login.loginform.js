/**
 * Created by brock on 3/5/15.
 */
$(function() {
    console.log("start login.loginform.js")
    $('#loginform').ajaxForm(function(data){
        $('#login_dialog').find('.modal-body').html(data)

        })
console.log("end login.loginform.js")
})