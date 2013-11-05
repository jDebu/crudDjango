from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from sigebasa.apps.home.forms import
#from sigebasa.apps.home.models import

def inicio(request):
    context=RequestContext(request)
    return render_to_response('index.html',context)

