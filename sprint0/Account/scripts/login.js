/**
 * Created by brock on 3/5/15.
 */
$(function() {
    $('#login_dialog').modal({
        show:false,
    })

    $('.show_modal').on('click',function(){
         $('#login_dialog').modal('show');
        $.ajax({
            url:'/Account/login.loginform',
            success: function(data) {


                $('#login_dialog').find('.modal-body').html(data)
            }



        })


    })
});