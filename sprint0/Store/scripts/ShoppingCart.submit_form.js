/**
 * Created by brock on 3/6/15.
 */
$(function() {
    console.log("something is happening")

    $('#checkout_form').ajaxForm(function(data){

        $('#form_container').html(data)



})

});