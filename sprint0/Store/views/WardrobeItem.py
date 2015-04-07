__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
import datetime
from decimal import Decimal
from django.core.mail import send_mail

templater = get_renderer('Store')

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def rented_list(request):
    params = {}
    params['wdbItems'] = hmod.RentedLineItem.objects.filter(date_in=None)

    return templater.render_to_response(request, 'RentedWardrobeItem.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def process_request(request):
    params = {}
    params['wdbItems'] = hmod.WardrobeItem.objects.all().order_by('name')

    return templater.render_to_response(request, 'WardrobeItem.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def check_in(request):
    params = {}
    form = check_in_form()
    if request.method == 'POST':
        print('the method is post')
        form = check_in_form(request.POST)

        if form.is_valid():
            print('the form is valid')
            fees = 0
            returnItem = hmod.RentedLineItem.objects.get(id=request.urlparams[0])
            print('a return object has been created')
            if form.cleaned_data['new_damage']:
                print('there are new damages')
                returnItem.new_damage = form.cleaned_data['damage_description']
            if form.cleaned_data['override_late_fee']:
                print('late fees will be overridden')
                #returnItem.fees_paid = form.cleaned_data['non_standard_fee']
            else:
                print('standard late fees will be charges')
                due_date = returnItem.date_due.strftime("%Y-%m-%d")
                d1 = datetime.datetime.strptime(due_date, "%Y-%m-%d")
                current_date = datetime.datetime.now()
                current_date1 = current_date.strftime("%Y-%m-%d")
                d2 = datetime.datetime.strptime(current_date1, "%Y-%m-%d")
                total_days = abs((d2 - d1).days)
                print(total_days)
                fee_multiplier = Decimal(total_days/7)
                print(fee_multiplier)
                print(returnItem.wardrobe_item_ID.standard_rental_value)
                late_fees = (fee_multiplier * returnItem.wardrobe_item_ID.standard_rental_value)
                fees += late_fees
                print(late_fees)
                print(fees)
            if form.cleaned_data['non_standard_fee'] is not None:
                print('there will be nonstandard late fees as well')
                fees += form.cleaned_data['non_standard_fee']
            returnItem.fees_paid =  fees
            returnItem.wardrobe_item_ID.is_available_for_rental = True
            returnItem.date_in = current_date
            returnItem.save()
            print(fees)
            return HttpResponseRedirect('/Store/WardrobeItem.rented_list/')

    params['form'] = form
    rentalItem = hmod.RentedLineItem.objects.get(id=request.urlparams[0])
    params['check_in_item'] = rentalItem
    return templater.render_to_response(request, 'WardrobeItem.check_in.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def edit(request):
    params = {}
    try:
        wdbitem = hmod.WardrobeItem.objects.get(id=request.urlparams[0])

    except hmod.WardrobeItem.DoesNotExist:
        return HttpResponseRedirect('/Store/WardrobeItem.edit/')

    form = wdbItemEditForm(initial={

        'size_modifier': wdbitem.size_modifier,
        'size': wdbitem.size,
        'gender': wdbitem.gender,
        'color': wdbitem.color,
        'pattern': wdbitem.pattern,
        'start_year': wdbitem.start_year,
        'end_year': wdbitem.end_year,
        'note': wdbitem.note,
        })

    if request.method == 'POST':
        form = wdbItemEditForm(request.POST)
        if form.is_valid():
            wdbitem.size_modifier = form.cleaned_data['size_modifier']
            wdbitem.size = form.cleaned_data['size']
            wdbitem.color = form.cleaned_data['color']
            wdbitem.gender = form.cleaned_data['gender']
            wdbitem.pattern = form.cleaned_data['pattern']
            wdbitem.start_year = form.cleaned_data['start_year']
            wdbitem.end_year = form.cleaned_data['end_year']
            wdbitem.note = form.cleaned_data['note']
            wdbitem.is_rentable = form.cleaned_data['is_rentable']
            wdbitem.save()

            return HttpResponseRedirect('/Store/WardrobeItem/')



    params['form'] = form
    return templater.render_to_response(request, 'WardrobeItem.edit.html', params)


class wdbItemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    size_modifier = forms.CharField(required=True, max_length=255)
    size = forms.CharField(required=True, max_length=20)
    gender = forms.CharField(required=True, max_length=20)
    color = forms.CharField(required=True, max_length=20)
    pattern = forms.CharField(required=True, max_length=50)
    start_year = forms.IntegerField(required=True)
    end_year = forms.IntegerField(required=True)
    note = forms.CharField(required=False, max_length=255)
    is_rentable =forms.BooleanField(widget=forms.CheckboxInput)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Create(request):

    wdbitem = hmod.WardrobeItem()
    wdbitem.name = ''
    wdbitem.note = ''
    wdbitem.start_year = None
    wdbitem.pattern = ''
    wdbitem.gender = ''
    wdbitem.color = ''
    wdbitem.end_year = None
    wdbitem.size = ''
    wdbitem.size_modifier = ''
    wdbitem.value = None
    wdbitem.standard_rental_value = None
    wdbitem.is_rentable = True
    wdbitem.save()

    return HttpResponseRedirect('/Store/WardrobeItem.edit/{}/'.format(wdbitem.id))

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Delete(request):
    try:
        wdbitem = hmod.WardrobeItem.objects.get(id=request.urlparams[0])
    except hmod.WardrobeItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/WardrobeItem/')
        print("item doesn't exist")
    wdbitem.delete()

    return HttpResponseRedirect('/Store/WardrobeItem/')

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def send_late_emails(request):

    params = {}

    results = get_late_lists()

    send_overdue_email(results['30'])
    send_overdue_email(results['60'])
    send_overdue_email(results['90'])

    params["late_items_30"] = results['30']
    params["late_items_60"] = results['60']
    params["late_items_90"] = results['90']

    return templater.render_to_response(request, 'WardrobeItem.get_late_items.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def get_late_items(request):

    params = {}

    results = get_late_lists()
    print("got the late items!")


    params["late_items_30"] = results['30']
    params["late_items_60"] = results['60']
    params["late_items_90"] = results['90']

    return templater.render_to_response(request, 'WardrobeItem.get_late_items.html', params)

class check_in_form(forms.Form):
    new_damage = forms.BooleanField(required=False)
    damage_description = forms.CharField(required=False, max_length=500, label='description')
    override_late_fee = forms.BooleanField(required=False, label='override fees')
    non_standard_fee = forms.DecimalField(required=False)

def send_overdue_email(items_list):
    for hmod.RentedLineItem in items_list:
        email = hmod.RentedLineItem.transaction_ID.customer.email
        print(email)
        item = hmod.RentedLineItem.wardrobe_item_ID.name
        print(item)
        due_date = hmod.RentedLineItem.date_due
        email_text = 'Your rental item: %s was due on %s\r ' \
                 'Please return the item to the colonial heritage ' \
                 'foundation to avoid incurring more charges' % (item, due_date)
        send_mail('Your overdue rental', email_text,
              'brock@chfoundation.us', [email], fail_silently=True)
        print("method success!!!")

def get_late_lists():
    now1 = datetime.datetime.now()
    now30 = now1 - datetime.timedelta(days=30)
    print(now30)
    now60 = now1 - datetime.timedelta(days=60)
    print(now60)
    now90 = now1 - datetime.timedelta(days=90)
    print(now90)
    params = {}
    #something goes here
    #get a list of items between [30 and ]60 days
    late_list30 = hmod.RentedLineItem.objects.filter(date_in__exact=None, date_due__lte=now30, date_due__gt=now60)
    #get a list of items between [60 and ]90 days
    late_list60 = hmod.RentedLineItem.objects.filter(date_in__exact=None, date_due__lte=now60, date_due__gt=now90)
    #get a list of items over 90 days late
    late_list90 = hmod.RentedLineItem.objects.filter(date_in__exact=None, date_due__lte=now90)
    return {'30': late_list30, '60': late_list60, '90': late_list90}
