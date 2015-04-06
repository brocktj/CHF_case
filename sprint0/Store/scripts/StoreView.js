/**
 * Created by brock on 3/6/15.
 */
$(function () {

    $("#filter").keyup(function(){

        // Retrieve the input field text and reset the count to zero
        var filter = $(this).val(), count = 0;

        // Loop through the comment list
        $("table td").each(function(){

            // If the list item does not contain the text phrase fade it out
            if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).fadeOut();

            // Show the list item if the phrase matches and increase the count by 1
            } else {
                $(this).show();
                count++;
            }
        });

    });

       $('.add_button').on('click', function() {
           console.log("button clicked!!!")

           var pid = $(this).attr('data-pid');
           console.log(pid);
           var thingy = "#qty" + pid;
           var qty = $(thingy).val();
           console.log(qty);


           $.loadmodal({
               url: '/Store/ShoppingCart.add_bulk_to_cart/' + pid + '/' + qty,
               title: "Shopping Cart",
               width: '700px',
               buttons: {
                   "Checkout": function() {
                        window.location.href = "/Store/ShoppingCart.view_cart";



                   }


               }



           })

       })
        $('.add_button_rental').on('click', function() {
           console.log("button clicked!!!")

           var pid = $(this).attr('data-pid');
           console.log(pid);



           $.loadmodal({
               url: '/Store/ShoppingCart.add_rental_to_cart/' + pid + '/',
               title: "Shopping Cart",
               width: '700px',
               buttons: {
                   "Checkout": function() {
                        window.location.href = "/Store/ShoppingCart.view_cart";



                   }


               }



           })

       })




})