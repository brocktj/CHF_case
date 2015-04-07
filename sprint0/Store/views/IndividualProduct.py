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
    params['indProducts'] = hmod.IndividualProduct.objects.all().order_by('name')

    return templater.render_to_response(request, 'IndividualProduct.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def edit(request):
    params = {}
    try:
        indProduct = hmod.IndividualProduct.objects.get(id=request.urlparams[0])

    except hmod.IndividualProduct.DoesNotExist:
        return HttpResponseRedirect('/Store/IndividualProduct/')

    form = indProductEditForm(initial={

        'name': indProduct.name,
        'description': indProduct.description,
        'category': indProduct.category,
        'current_price': indProduct.current_price,
        'date_made': indProduct.date_made,
        })

    if request.method == 'POST':
        form = indProductEditForm(request.POST)
        if form.is_valid():
            print("form is valid what is happening")
            indProduct.name = form.cleaned_data['name']
            indProduct.description = form.cleaned_data['description']
            indProduct.category = form.cleaned_data['category']
            indProduct.current_price = form.cleaned_data['current_price']
            indProduct.date_made = form.cleaned_data['date_made']
            indProduct.save()

            return HttpResponseRedirect('/Store/IndividualProduct/')



    params['form'] = form
    return templater.render_to_response(request, 'IndividualProduct.edit.html', params)


class indProductEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    description = forms.CharField(required=True, max_length=255)
    category = forms.CharField(required=True, max_length=50)
    current_price = forms.DecimalField(required=True)
    date_made = forms.DateField(required=False)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Create(request):
    indProduct = hmod.IndividualProduct()

    indProduct.name = ''
    indProduct.description = ''
    indProduct.category = ''
    indProduct.current_price = 0.00
    indProduct.date_made = None
    indProduct.save()

    return HttpResponseRedirect('/Store/IndividualProduct.edit/{}/'.format(indProduct.id))

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def Delete(request):
    try:
        indProduct = hmod.IndividualProduct.objects.get(id=request.urlparams[0])
    except hmod.IndividualProduct.DoesNotExist:
        return HttpResponseRedirect('/Store/IndividualProduct/')
    indProduct.delete()

    return HttpResponseRedirect('/Store/IndividualProduct/')