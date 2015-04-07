__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login

templater = get_renderer('Account')

@view_function
def process_request(request):
    params = {}
    params['users'] = hmod.User.objects.all().order_by('first_name')

    return templater.render_to_response(request, 'SignUp.html', params)

@view_function
def edit(request):
    l = request.user.groups.values_list('name',flat=True)
    print(l)
    params = {}

    try:
        User = hmod.User.objects.get(id=request.urlparams[0])

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/Account/SignUp/')

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
    params['user'] = User
    params['form'] = form
    return templater.render_to_response(request, 'SignUp.edit.html', params)


@view_function
def loginform(request):
    print(request.urlparams[0])
    params = {}
    User = hmod.User.objects.get(id=request.urlparams[0])
    form = UserEditForm()
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            User.username = form.cleaned_data['username']
            User.first_name = form.cleaned_data['first_name']
            User.last_name = form.cleaned_data['last_name']
            User.email = form.cleaned_data['email']
            User.set_password(form.cleaned_data['password'])
            User.security_question = form.cleaned_data['security_question']
            User.security_answer = form.cleaned_data['security_answer']
            User.address = form.cleaned_data['security_answer']
            User.city = form.cleaned_data['city']
            User.state = form.cleaned_data['state']
            User.zip = form.cleaned_data['zip']
            User.phone = form.cleaned_data['phone']
            User.save()


            group = Group.objects.get(name='GuestGroup')
            User.groups.add(group)
            User.save()
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
    return templater.render_to_response(request, 'SignUp.loginform.html', params)

@view_function
def Create(request):
    user = hmod.User()
    user.first_name = ''
    user.last_name = ''
    user.password = ''
    user.save()

    return HttpResponseRedirect('/Account/SignUp.edit/{}/'.format(user.id))

@view_function
def Delete(request):
    user = hmod.User.objects.get(id=request.urlparams[0])
    user.delete()

    return HttpResponseRedirect('/homepage/Users/')

class UserEditFormNonSensitive(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.IntegerField()
    phone = forms.CharField()
    email = forms.EmailField(required=True, max_length=100)

class UserEditForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.IntegerField()
    phone = forms.CharField()
    security_question = forms.CharField(required=True, max_length=250)
    security_answer = forms.CharField(required=True, max_length=250)
    password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(required=True, max_length=100)

    def clean(self):
        try:
            user = hmod.User.objects.get(username=self.cleaned_data.get('username'))
        except:
            return self.cleaned_data