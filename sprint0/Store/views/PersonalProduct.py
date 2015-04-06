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
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def process_request(request):
    params = {}
    params['persProducts'] = hmod.PersonalProduct.objects.all().order_by('name')

    return templater.render_to_response(request, 'PersonalProduct.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def edit(request):
    params = {}
    try:
        persProduct = hmod.PersonalProduct.objects.get(id=request.urlparams[0])

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/Store/PersonalProduct/')

    form = persProductEditForm(initial={

        'name': persProduct.name,
        'description': persProduct.description,
        'category': persProduct.category,
        'current_price': persProduct.current_price,
        'order_form_name': persProduct.order_form_name,
        'production_time': persProduct.production_time,
        })

    if request.method == 'POST':
        form = persProductEditForm(request.POST)
        if form.is_valid():
            print("form is valid what is happening")
            persProduct.name = form.cleaned_data['name']
            persProduct.description = form.cleaned_data['description']
            persProduct.category = form.cleaned_data['category']
            persProduct.current_price = form.cleaned_data['current_price']
            persProduct.order_form_name = form.cleaned_data['order_form_name']
            persProduct.production_time = form.cleaned_data['production_time']
            
            persProduct.save()

            return HttpResponseRedirect('/Store/PersonalProduct/')

    params['form'] = form
    return templater.render_to_response(request, 'PersonalProduct.edit.html', params)


class persProductEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    description = forms.CharField(required=True, max_length=255)
    category = forms.CharField(required=True, max_length=50)
    current_price = forms.DecimalField(required=True)
    order_form_name = forms.CharField(required=True)
    production_time = forms.CharField(required=True, label='Production time in days')

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Create(request):
    persProduct = hmod.PersonalProduct()

    persProduct.name = ''
    persProduct.description = ''
    persProduct.category = ''
    persProduct.current_price = 0.00
    persProduct.production_time = 0
    persProduct.order_form_name = ''
    persProduct.save()

    return HttpResponseRedirect('/Store/PersonalProduct.edit/{}/'.format(persProduct.id))

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Delete(request):
    try:
        persProduct = hmod.PersonalProduct.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/Store/PersonalProduct/')
    persProduct.delete()

    return HttpResponseRedirect('/Store/PersonalProduct/')