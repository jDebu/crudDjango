# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from sigebasa.apps.catalogo.forms import HospitalForm
from sigebasa.apps.catalogo.models import Hospital,Producto,Pedido

def ver(request):
    hospitales  = Hospital.objects.all()
    context     = RequestContext(request, {'hospitales': hospitales})
    return render_to_response('hospital/listar.html',context)
def crear(request):
    formulario= HospitalForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/hospitales/')

    context = RequestContext(request, {'cookie': formulario})
    return render_to_response('hospital/nuevoHospital.html',context)

def actualizar(request,id):
    hospital= Hospital.objects.get(pk=id)
    form=HospitalForm()
    if  request.method=='POST':
        form=HospitalForm(request.POST, instance=hospital)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hospitales/')
    else:
        form = HospitalForm(instance=hospital)
        context = RequestContext(request,{'form':form,'id':id})

    return render_to_response('hospital/actualizar.html',context)


def borrar(request,id):
    hospital=Hospital.objects.get(pk=id)
    if  request.method=='POST':
         hospital.delete()
         return HttpResponseRedirect('/hospitales/')
    context= RequestContext(request,{'hospital':hospital})
    return render_to_response('hospital/eliminar.html',context)


def metroboot(request):
    context=RequestContext(request)
    return render_to_response('index2.html',context)
def metrobootbase(request):
    context=RequestContext(request)
    return render_to_response('basecss.html',context)
def metrobootcomponents(request):
    context=RequestContext(request)
    return render_to_response('components.html',context)


