__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import logout

templater = get_renderer('Account')

@view_function
def process_request(request):
    logout(request)
    return HttpResponseRedirect('/Account/login/')
