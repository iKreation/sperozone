from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import json

from sperozoneApp.models import Ocorrencia

def get_ocorrencia(ocorrencia_id):
	ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
	return HttpResponse("A aceder a ocorrencia "+ocorrencia_id+" "+ocorrencia.title)

def remove_ocorrencia(oc_id):
    Ocorrencia.objects.filter(id=oc_id).delete()
    return HttpResponse("Ocorrencia eliminada")

def edit_ocorrencia(request, oc_id):
    ocorrencia = Ocorrencia.objectos.filter(id=oc_id)
    data = json.loads(request.body)
    ocorrencia.title = data['title']
    ocorrencia.description = data['description']
    ocorrencia.report_date = timezone.now()
    ocorrencia.status = data['title']
    ocorrencia.save()
    return HttpResponse("Ocorrencia modificada")

def new_ocorrencia(request):
    data = json.loads(request.body)

    ocorrencia = Ocorrencia(title=data['title'],description=data['description'],report_date=timezone.now(),status=data['status'])
    ocorrencia.save()
    return HttpResponse("Nova ocorrencia adicionada")

def controller(request, pk):
    print "method "+request.method
    print request
    if request.method == 'DELETE':
        return remove_ocorrencia(pk)
    elif request.method == 'GET':
        return get_ocorrencia(pk)
    elif request.method == 'PUT' or 'POST':
        data = json.loads(request.body)
        if data.has_key('id') and data['id'] == 0:
            return new_ocorrencia(request)
        else:
            return edit_ocorrencia(request,pk_id)