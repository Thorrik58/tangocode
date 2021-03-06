# coding= utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    template = get_template('rango/index.html')
    return HttpResponse(template.render(context_dict), request)