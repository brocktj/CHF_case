__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from collections import Counter
from datetime import timedelta
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail
import requests

templater = get_renderer('Store')

@view_function
def process_request(request):
    params = {}
    return templater.render_to_response(request, 'ShoppingCart.html', params)

@view_function
@login_required(login_url='/Account/login')
def check_out(request):
    print("this method is getting run")
    params = {}
    form = card_form()
    form1 = address_form()
    params['form'] = form
    params['form1'] = form1
    params['total'] = request.urlparams[0]
    return templater.render_to_response(request, 'check_out.html', params)

@view_function
def confirmation(request):
    #in theory some sort of transaction ID would be generated in the sumbit_form method
    #but for the sake of this sprint, we won't deal with the logic of getting that information
    #we assume that everything is good
    params = {}
    if 'shopping_cart' in request.session:
        list = request.session['shopping_cart']
        request.session['shopping_cart'] = list
        x = Counter(list)
        del request.session['shopping_cart']

    else:
        x = {}

    if 'rental_shopping_cart' in request.session:
        rental_list = request.session['rental_shopping_cart']
        del request.session['rental_shopping_cart']
    else:
        rental_list = []


    params['y'] = rental_list
    params['x'] = x

    email_text = 'Thank you for your order of:\r\r'
    for k in x:
        item = hmod.BulkProduct.objects.get(id=k)
        qty = x.get(k)
        email_text += str(qty) + ' ' + item.name + '\r'
    for i in rental_list:
        email_text +='and your rentals of: \r'
        item = hmod.WardrobeItem.objects.get(id=i)
        email_text += item.name
        email_text += '\rthese items will be due one week from today\r'
    email_text += 'Your credit card will be charged $%s\r' % (request.urlparams[0]) + 'Sincerely,\r\r The Colonial Heritage Foundation'



    send_mail('Your Order from the Colonial Heritage Foundation', email_text,
              'brock@chfoundation.us', ['short1inslo@gmail.com'], fail_silently=True)






    return templater.render_to_response(request, 'ShoppingCart.order_confirmation.html', params)

@view_function
def submit_form(request):
    params = {}
    if request.method == 'POST':
        print("the method is post")
        form = card_form(request.POST)
        if form.is_valid():
            #charge the API


            #If the transaction is successful do the following
            #make the transaction
            trans = hmod.Transaction()
            trans.customer = request.user
            trans.date = datetime.datetime.now()
            trans.date_paid = datetime.datetime.now()
            trans.payment_id = form.ID
            trans.save()

            print(trans.payment_id)

            ids= trans.id
            print(ids)

            if 'rental_shopping_cart' in request.session:
                #create the rental line items tying each one to the user
                now = datetime.datetime.now()
                rentalItems = request.session['rental_shopping_cart']
                for i in rentalItems:
                    #get the wardrobe item
                    wdbItem = hmod.WardrobeItem.objects.get(id=i)
                    #change its its available for rental status
                    wdbItem.is_available_for_rental = False
                    #save the item
                    wdbItem.save()
                    rentalItem = hmod.RentedLineItem()
                    rentalItem.wardrobe_item_ID = wdbItem
                    rentalItem.date_out = now
                    print('dateout assigned')
                    date_due = now + datetime.timedelta(days=7)
                    print(date_due)
                    rentalItem.date_due = now + datetime.timedelta(days=7)
                    print("date_due assigned")
                    rentalItem.transaction_ID = hmod.Transaction.objects.get(id=ids)
                    print('transaction assigned')
                    rentalItem.save()
                    print('made it to the return statement')

            email_text = ''



            return HttpResponse(
                '''
                <script>
                    window.location.href = "/Store/ShoppingCart.confirmation/%s"
                </script>


            '''% (request.urlparams[0]))

    params['warnings'] = ''
    params['form'] = form
    print("end of method reached")
    return templater.render_to_response(request, 'ShoppingCart.submit_form.html', params)

@view_function
def delete_item(request):
    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
    params = {}
    #make a list that is the shoppin cart
    list1 = request.session['shopping_cart']
    #look through and remove all instances on the ID within the shopping cart
    while int(request.urlparams[0]) in list1:
        list1.remove(int(request.urlparams[0]))

    #set the shopping cart to the new list object
    request.session['shopping_cart'] = list1
    request.session.modified = True
    #make the new dictionary for the template
    x = Counter(list1)
    #make the list for the for the rental shopping cart
    list2 = request.session['rental_shopping_cart']
    params['y'] = list2
    params['x'] = x
    params['current_cart'] = request.session['shopping_cart']

    return templater.render_to_response(request, 'ShoppingCartView.html', params)

@view_function
def delete_rental_item(request):
    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
    params = {}
    #get a list that is the current rental shopping cart
    list1 = request.session['rental_shopping_cart']
    #remove all instances of the item selected
    while int(request.urlparams[0]) in list1:
        list1.remove(int(request.urlparams[0]))
    #set the rental shopping cart equal to the edited list
    request.session['rental_shopping_cart'] = list1
    #save the session object so that changes are persistent
    request.session.modified = True
    #pass through all the parameters
    x = Counter(request.session['shopping_cart'])
    params['y'] = request.session['rental_shopping_cart']
    params['x'] = x
    params['current_cart'] = request.session['shopping_cart']
    print(list)

    return templater.render_to_response(request, 'ShoppingCartView.html', params)


@view_function
def view_cart(request):
    if request.user.is_active:
        print("user is anonymous")
        HttpResponseRedirect('/Account/login')
    else:
        print("this method is getting run")
    params = {}
    if 'shopping_cart' in request.session:
        list1 = request.session['shopping_cart']
        x = Counter(list1)

    else:
        x = {}

    if 'rental_shopping_cart' in request.session:
        rental_list = request.session['rental_shopping_cart']

    else:
        rental_list = []

    params['y'] = rental_list
    params['x'] = x
    return templater.render_to_response(request, 'ShoppingCartView.html', params)

@view_function
def add_bulk_to_cart(request):
    print("method is intialized!!")

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = []
        print("a shopping cart was created")
    print('there is a shopping cart')

    if 'rental_shopping_cart' not in request.session:
        request.session['rental_shopping_cart'] = []
        print("a rental shopping cart was created")
    print('there is rental a shopping cart')

    pid = request.urlparams[0]
    print(pid)
    qty = request.urlparams[1]
    print(qty)

    for i in range(0, int(qty)):
        request.session['shopping_cart'].append(int(pid))
    print(request.session['shopping_cart'])
    request.session.modified = True
    params = {}
    params['current_cart'] = request.session['shopping_cart']

    list = request.session['shopping_cart']

    x = Counter(list)

    params['y'] = request.session['rental_shopping_cart']
    params['x'] = x



    print(x)


    return templater.render_to_response(request, 'ShoppingCart.html', params)

@view_function
def add_rental_to_cart(request):
    params = {}
    if 'rental_shopping_cart' not in request.session:
        request.session['rental_shopping_cart'] = []
        print("a rental shopping cart was created")
    print('there is a rental shopping cart')

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = []
        print("a shopping cart was created")
    print('there is a shopping cart')

    pid = request.urlparams[0]
    rentalToAdd = hmod.WardrobeItem.objects.get(id=pid)

    if rentalToAdd.is_available_for_rental:
        request.session['rental_shopping_cart'].append(int(pid))
        print(request.session['rental_shopping_cart'])
        print(request.session['shopping_cart'])
        request.session.modified = True
    else:
        params['warnings'] = "The item you have selected for rental is unavailable, please check back at a future date"

    params['current_cart'] = request.session['shopping_cart']
    params['current_rental_cart'] = request.session['rental_shopping_cart']

    params['x'] = Counter(request.session['shopping_cart'])
    params['y'] = request.session['rental_shopping_cart']

    return templater.render_to_response(request, 'ShoppingCart.html', params)

@view_function
def send_email(request):
    params = {}
    send_mail('Your Purchase', 'Thanks', 'from@gmail.com', )

    return templater.render_to_response(request, 'ShoppingCart.html', params)

@view_function
def delete_cart(request):
    del request.session['shopping_cart']
    del request.session['rental_shopping_cart']
    return HttpResponseRedirect('/Store/StoreView')

class card_form(forms.Form):
    card_number = forms.IntegerField(required=True)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    exp_month = forms.IntegerField(required=True)
    exp_year = forms.IntegerField(required=True)
    security_code = forms.IntegerField(required=True)

    def clean(self):
        API_URL='http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY='d925f0b977da6ed6d44855a37c340c16'
        card_check= self.cleaned_data.get('card_number')
        card_count = len(str(card_check))
        if card_count != 16:
            raise forms.ValidationError("the card number is not correct")
        else:
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': '5.99',
                'type': 'Visa',
                'number': '4732817300654',
                'exp_month': '10',
                'exp_year': '15',
                'cvc': '411',
                'name': 'Cosmo Limesandal',
                'description': 'Charge	for	cosmo@is411.byu.edu',
            })
            print(r.text)

            resp = r.json()

            if 'error' in resp:
                print('ERROR: ', resp['error'])
            else:
                print("Charge SUCCESSFUL!!!!")
                print(resp.keys())
                print(resp['ID'])
                self.ID=resp['ID']
            return self.cleaned_data

class address_form(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    number = forms.IntegerField(required=True)
    street = forms.CharField(required=True, max_length=100)
    apt_number = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=True)
    state = forms.IntegerField(required=True)
    ZIP = forms.IntegerField(required=True)

