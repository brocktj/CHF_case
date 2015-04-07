__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    event1 = hmod.Event()

    event1.description='This is our event, it is super awesome'
    event1.endDate = '10/15/2015'
    event1.name = 'Coolest Event Ever!!'

    return templater.render_to_response(request, 'SaleItem.html', params)