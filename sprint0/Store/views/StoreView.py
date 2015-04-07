__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('Store')

@view_function
def process_request(request):
    params = {}

    blkProductForm = blkCartForm(initial={
        'quantity': 1
    })
    params['blkProductForm'] = blkProductForm

    params['wdbItems'] = hmod.WardrobeItem.objects.all().order_by('name')
    params['blkProducts'] = hmod.BulkProduct.objects.all().order_by('name')
    params['persProducts'] = hmod.PersonalProduct.objects.all().order_by('name')
    return templater.render_to_response(request, 'StoreView.html', params)

@view_function
def loginform(request):
    params = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            params['user'] = user
            return HttpResponse(
                '''
                <script>
                    window.location.href = "/Account/Account"
                </script>


            ''')

    params['warnings'] = ''
    params['form'] = form
    print("end of method reached")
    return templater.render_to_response(request, 'login.loginform.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def edit(request):
    params = {}
    try:
        blkProduct = hmod.BulkProduct.objects.get(id=request.urlparams[0])

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/Store/BulkProduct.edit/')

    blkProductForm = blkCartForm(initial={
        'quantity': 1
    })
    form = blkProductEditForm(initial={

        'name': blkProduct.name,
        'description': blkProduct.description,
        'category': blkProduct.category,
        'current_price': blkProduct.current_price,
        'quantity_on_hand': blkProduct.quantity_on_hand,
        })

    if request.method == 'POST':
        form = blkProductEditForm(request.POST)
        if form.is_valid():
            print("form is valid what is happening")
            blkProduct.name = form.cleaned_data['name']
            blkProduct.description = form.cleaned_data['description']
            blkProduct.category = form.cleaned_data['category']
            blkProduct.current_price = form.cleaned_data['current_price']
            blkProduct.quantity_on_hand = form.cleaned_data['quantity_on_hand']
            blkProduct.save()

            return HttpResponseRedirect('/Store/BulkProduct/')


    params['bulkProductForm'] = blkProductForm
    params['form'] = form
    return templater.render_to_response(request, 'BulkProduct.edit.html', params)


class blkProductEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    description = forms.CharField(required=True, max_length=255)
    category = forms.CharField(required=True, max_length=50)
    current_price = forms.DecimalField(required=True)
    quantity_on_hand = forms.IntegerField(required=False)

class blkCartForm(forms.Form):
    quantity = forms.IntegerField(required=False)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Create(request):
    blkProduct = hmod.BulkProduct()

    blkProduct.name = ''
    blkProduct.description = ''
    blkProduct.category = ''
    blkProduct.current_price = 0.00
    blkProduct.quantity_on_hand = 0
    blkProduct.save()

    return HttpResponseRedirect('/homepage/BulkProduct.edit/{}/'.format(blkProduct.id))

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Delete(request):
    try:
        blkProduct = hmod.BulkProduct.objects.get(id=request.urlparams[0])
    except hmod.BulkProduct.DoesNotExist:
        return HttpResponseRedirect('/Store/BulkProduct/')
        print("item does not exist")
    blkProduct.delete()

    return HttpResponseRedirect('/Store/BulkProduct/')