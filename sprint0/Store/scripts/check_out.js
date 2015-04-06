/**
 * Created by brock on 3/6/15.
 */
$(function() {
    console.log("something is happening!!")
    console.log($('.submit_form'))
    $('.submit_form').on('click',function(){
        console.log("the submit form button triggered the event")
        console.log("something is happening")

    $('#checkout_form').ajaxForm(function(data){
        console.log(data)
        $('#form_container').html(data)
            })



        })




});