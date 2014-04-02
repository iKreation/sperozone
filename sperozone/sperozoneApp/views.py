from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from sperozoneApp.models import Ocorrencia
from django.views.decorators.csrf import csrf_exempt
import json

def get_ocorrencia(ocorrencia_id):
	ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
	return HttpResponse("A aceder a ocorrencia "+ocorrencia_id+" "+ocorrencia.title)

def list_ocorrencias():
    return HttpResponse(Ocorrencia.objects.all())

def remove_ocorrencia(oc_id):
    Ocorrencia.objects.filter(id=oc_id).delete()
    return HttpResponse(Ocorrencia.objects.all())

def edit_ocorrencia(request, oc_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=oc_id)
    data = json.loads(request.body)
    ocorrencia.title = data['title']
    ocorrencia.description = data['description']
    ocorrencia.report_date = timezone.now()
    ocorrencia.status = data['title']
    ocorrencia.lat = data['lat']
    ocorrencia.lon = data['lon']
    ocorrencia.save()
    return HttpResponse("Ocorrencia modificada")

def new_ocorrencia(request):
    data = json.loads(request.body)

    ocorrencia = Ocorrencia(title=data['title'],description=data['description'],report_date=timezone.now(),status=data['status'], lat=data['lat'], lon=['lon'])
    #ocorrencia = Ocorrencia(title="stuff",description="Not much",report_date=timezone.now(),status="Never", lat=1.4, lon=1.4)
    ocorrencia.save()
    return HttpResponse("Nova ocorrencia adicionada")

@csrf_exempt
def controller(request, pk=None):
    print "method "+request.method
    if request.method == 'DELETE':
        return remove_ocorrencia(pk)
    elif request.method == 'GET':
        if pk!=None:
            return get_ocorrencia(pk)
        else:
            return list_ocorrencias()
    elif request.method == 'PUT' or 'POST':
        print "entrez!"
        data = json.loads(request.body)
        print data
        if (pk==None):
            print "NUEVO!"
            return new_ocorrencia(request)
        else:
            return edit_ocorrencia(request,pk)