__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO


templater = get_renderer('Account')

@view_function
def process_request(request):
    params = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #this will need to be changed to our server once we get it up and running
            netid = username=form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password')
            s = Server('byuldap.byu.edu', port=389, get_info=GET_ALL_INFO)
            c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='cn=%S,ou=people,o=ces' % netid, password=password1, authentication=AUTH_SIMPLE)
            #check if the the information provided is valid
            if c:
                #print c to view how it it is set up
                print(c)
                u = hmod.User.objects.get_or_create(username=netid)
                #now check djangos auth system for the user, and if they're there log them in
                if u:
                    #update user information to match the active directory information
                    u.first_name = 'info from active directory'
                    u.last_name = 'info from active directory'
                    u.email = 'email from active directory'
                    u.set_password('xxx')
                    u.save

                    user = authenticate(username=netid, password=password1)
                    login(request, user)
                #otherwise log the user in normally,
                else:
                    user = authenticate(username=netid, password=password1)
                    login(request, user)
            params['user'] = user
            return HttpResponseRedirect('/Account/Account/')

    params['warnings'] = ''
    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)


@view_function
def loginform1(request):
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
def test_server(request):
    params = {}
    form = LoginForm()

    s = Server('chfoundation.us', port=8889, get_info=GET_ALL_INFO)
    print('connected')
    c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='brock@chfoundation.local', password='Password1', authentication=AUTH_SIMPLE)
    print("connection established")
    params['warnings'] = ''
    params['form'] = form
    print("end of method reached")
    return templater.render_to_response(request, 'login.loginform.html', params)

@view_function
def loginform(request):
    params = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #this will need to be changed to our server once we get it up and running
            netid = username=form.cleaned_data.get('username')
            user_string = 'cn=' +  netid + ',ou=people,o=ces'
            print(user_string)
            print(netid)
            password1 = form.cleaned_data.get('password')
            print(password1)
            s = Server('chfoundation.us', port=8889, get_info=GET_ALL_INFO)
            print('connected')
            c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='brock@chfoundation.local', password='Password1', authentication=AUTH_SIMPLE)
            print("connection established")
            #check if the the information provided is valid
            if c:
                #print c to view how it it is set up
                print('totes authenticated')
                print(c)
                u = hmod.User.objects.get(username=netid)
                print(u.first_name)
                #now check djangos auth system for the user, and if they're there log them in
                if u:
                    print('connection successful')
                    user1 = authenticate(username=netid, password=password1)
                    if user1.is_authenticated():
                        print("authenticated")
                    login(request, user1)
                    print("logged in")
                #otherwise log the user in normally,
                else:
                    user1 = authenticate(username=netid, password=password1)
                    login(request, user1)
            else:
                user1 = authenticate(username=netid, password=password1)
                login(request, user1)
            params['user'] = user1
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
def unauthorized_access(request):
    params = {}
    form = LoginForm()
    params['warnings']='You do not have access to view this page, please contact an administrator'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            params['user'] = user
            return HttpResponseRedirect('/Account/Account/')
    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, label='password', widget=forms.PasswordInput())

    #def clean(self):
       # user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
       # if user == None:
      #      raise forms.ValidationError("Invalid username/password combination, please try again")
       # return self.cleaned_data
