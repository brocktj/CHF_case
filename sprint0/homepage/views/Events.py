__author__ = 'brock'
import datetime

from django.http import HttpResponseRedirect
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    params['events'] = hmod.Event.objects.all()

    return templater.render_to_response(request, 'Events.html', params)



@view_function
def view_details(request):
    params = {}
    params['event'] = hmod.Event.objects.get(id=request.urlparams[0])
    areas = hmod.Area.objects.filter(event_ID=request.urlparams[0])
    area1 = {}
    x = 0

    params['areas'] = areas

    return templater.render_to_response(request, 'EventDetails.html', params)

@view_function
@permission_required('homepage.manager_rights', login_url='/homepage/login.unauthorized_access')
def edit(request):
    params = {}
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])

    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/Events/')

    form = EventEditForm(initial={
        'event_name': event.name,
        'event_description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,


    })

    if request.method == 'POST':
        form = EventEditForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data['event_name']
            event.description = form.cleaned_data['event_description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.save()
            return HttpResponseRedirect('/homepage/Events/')



    params['form'] = form
    return templater.render_to_response(request, 'Events.edit.html', params)


class EventEditForm(forms.Form):
    event_name = forms.CharField(required=True, max_length=100)
    event_description = forms.CharField(required=True, max_length=100)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    map_path = forms.CharField(required=False)

@view_function
@permission_required('homepage.manager_rights', login_url='/Account/login.unauthorized_access')
def Create(request):
    dateitem = datetime.datetime.now()
    event = hmod.Event()
    event.description = ''
    event.start_date = dateitem.strftime("%Y-%m-%d")
    event.end_date = dateitem.strftime("%Y-%m-%d")
    event.mapFileName = ''

    event.save()

    return HttpResponseRedirect('/homepage/Events.edit/{}/'.format(event.id))

@view_function
@permission_required('homepage.manager_rights', login_url='/Account/login.unauthorized_access')
def Delete(request):
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except:
        return HttpResponseRedirect('/homepage/Events/')
        print("event doesn't exist")
    event.delete()

    return HttpResponseRedirect('/homepage/Events/')