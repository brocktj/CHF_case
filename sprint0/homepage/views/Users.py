__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')

@view_function
@permission_required('homepage.admin_rights', login_url='/Account/login.unauthorized_access')
def process_request(request):
    params = {}
    params['users'] = hmod.User.objects.all().order_by('first_name')

    return templater.render_to_response(request, 'Users.html', params)

@view_function
@permission_required('homepage.admin_rights', login_url='/Account/login.unauthorized_access')
def edit(request):
    l = request.user.groups.values_list('name',flat=True)
    print(l)
    params = {}

    try:
        User = hmod.User.objects.get(id=request.urlparams[0])

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/Users/')

    form = UserEditForm(initial={
        'first_name': User.first_name,
        'last_name': User.last_name,
        'email': User.email,
        'username': User.username,


    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            print('form is valid')
            User.username = form.cleaned_data['username']
            User.first_name = form.cleaned_data['first_name']
            User.last_name = form.cleaned_data['last_name']
            User.email = form.cleaned_data['email']
            User.set_password(form.cleaned_data['password'])
            User.save()
            group = Group.objects.get(name='GuestGroup')
            User.groups.add(group)
            User.save()
            return HttpResponseRedirect('/homepage/Users')

    params['form'] = form
    return templater.render_to_response(request, 'Users.edit.html', params)


class UserEditForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(required=True, max_length=100)


class PermissionChangeForm(forms.Form):
    admin = forms.BooleanField(required=False)
    manager = forms.BooleanField(required=False)
    guest = forms.BooleanField(required=False)

@view_function
@permission_required('homepage.admin_rights', login_url='/Account/login.unauthorized_access')
def ChangePermissions(request):
    params = {}
    form = PermissionChangeForm()
    user = hmod.User.objects.get(id=request.urlparams[0])
    if request.method == 'POST':
        form = PermissionChangeForm(request.POST)
        if form.is_valid():
            admin = form.cleaned_data['admin']
            manager = form.cleaned_data['manager']
            guest = form.cleaned_data['guest']
            user.groups.clear()

            if admin:
                adminGroup = Group.objects.get(name='AdminGroup')
                user.groups.add(adminGroup)
                user.save()
            if manager:
                managerGroup = Group.objects.get(name='ManagerGroup')
                user.groups.add(managerGroup)
                user.save()
            if guest:
                guestGroup = Group.objects.get(name='GuestGroup')
                user.groups.add(guestGroup)
                user.save()
            return HttpResponseRedirect('/homepage/Users/')
    params['form']=form
    return templater.render_to_response(request, 'Users.ChangePermissions.html', params)

@view_function
def Create(request):
    user = hmod.User()
    user.first_name = ''
    user.last_name = ''
    user.password = ''
    user.save()

    return HttpResponseRedirect('/homepage/Users.edit/{}/'.format(user.id))

@view_function
@permission_required('homepage.admin_rights', login_url='/Account/login.unauthorized_access')
def Delete(request):
    user = hmod.User.objects.get(id=request.urlparams[0])
    user.delete()

    return HttpResponseRedirect('/homepage/Users/')