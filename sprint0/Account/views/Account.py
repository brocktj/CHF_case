__author__ = 'brock'
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Account.views.SignUp import UserEditFormNonSensitive


templater = get_renderer('Account')

@view_function
@permission_required('homepage.admin_rights', login_url='/Account/Account.ManagerTest/')
def process_request(request):
    params ={}
    return templater.render_to_response(request, 'Account.Admin.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/Account/Account.GuestTest/')
def ManagerTest(request):
    params ={}
    return templater.render_to_response(request, 'Account.Manager.html', params)

@view_function
def GuestTest(request):
    params ={}
    return templater.render_to_response(request, 'Account.html', params)

@view_function
def edit_user_info(request):
    params ={}
    User = request.user
    if request.method == 'POST':
        form = UserEditFormNonSensitive(request.POST)
        if form.is_valid():
            print('form is valid')
            User.first_name = form.cleaned_data['first_name']
            User.last_name = form.cleaned_data['last_name']
            User.email = form.cleaned_data['email']
            User.address = form.cleaned_data['address']
            User.city = form.cleaned_data['city']
            User.zip = form.cleaned_data['zip']
            User.state = form.cleaned_data['state']
            User.phone = form.cleaned_data['phone']
            User.save()
            return HttpResponseRedirect('/Account/Account')

    form = UserEditFormNonSensitive(initial={
        'first_name': User.first_name,
        'last_name': User.last_name,
        'email': User.email,
        'address': User.address,
        'city': User.city,
        'zip': User.zip,
        'phone': User.phone,
        'state': User.state,

        })

    id = request.user.id
    params['id'] = id
    params['form'] = form
    return templater.render_to_response(request, 'UpdateInfo.html', params)

@view_function
def update_password(request):
    params ={}
    User = request.user
    if request.method == 'POST':
        params['warnings'] = "you have entered a password that doesn't match our records, please try again"
        print("method is post")
        form = password_change_form(request.POST)
        if form.is_valid():
            user_name = request.user.username
            print(user_name)
            User1 = authenticate(username=request.user.username, password=form.cleaned_data['old_password'])
            if User1.is_authenticated():
                print("user is authenticated!")
                User.set_password(form.cleaned_data['new_password'])
                User.save()
                return HttpResponseRedirect('/Account/login')

    form = password_change_form()

    id = request.user.id
    params['warnings'] = ''
    params['id'] = id
    params['form'] = form

    return templater.render_to_response(request, 'UpdatePassword.html', params)

@view_function
def change_password(request):
    params ={}
    return templater.render_to_response(request, 'Account.html', params)

class password_change_form(forms.Form):
    old_password = forms.CharField(max_length=100, label='Old Password', widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=100, label='New Password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(max_length=100, label='Confirm New Password', widget=forms.PasswordInput())

    def clean(self):
        pswd1 = self.cleaned_data.get('new_password')
        pswd2 = self.cleaned_data.get('new_password2')
        if pswd1 != pswd2:
            raise forms.ValidationError("Passwords do not match, please retype them")
        return self.cleaned_data
