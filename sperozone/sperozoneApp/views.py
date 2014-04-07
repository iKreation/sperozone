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
	return HttpResponse(json.dumps(ocorrencia.to_dict()),content_type="application/json")

def list_ocorrencias():
    ocorrencias = Ocorrencia.objects.all()
    list_to_json = [oc.to_dict() for oc in ocorrencias]
    return HttpResponse(json.dumps(list_to_json),content_type="application/json")

def remove_ocorrencia(oc_id):
    Ocorrencia.objects.filter(id=oc_id).delete()
    ocorrencias = Ocorrencia.objects.all()
    list_to_json = [oc.to_dict() for oc in ocorrencias]
    return HttpResponse(json.dumps(list_to_json),content_type="application/json")

def edit_ocorrencia(request, oc_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=oc_id)
    data = json.loads(request.body)
    ocorrencia.title = data['title']
    ocorrencia.description = data['description']
    ocorrencia.report_date = timezone.now()
    ocorrencia.status = data['status']
    ocorrencia.lat = data['lat']
    ocorrencia.lon = data['lon']
    ocorrencia.save()
    return HttpResponse(json.dumps(ocorrencia.to_dict()),content_type="application/json")

def new_ocorrencia(request):
    print "CARGANDO!"
    data = json.loads(request.body)
    print data
    ocorrencia = Ocorrencia(title=data['title'],description=data['description'],report_date=timezone.now(),status=data['status'], lat=data['lat'], lon=data['lon'])
    ocorrencia.save()
    return HttpResponse(json.dumps(ocorrencia.to_dict()),content_type="application/json")

@csrf_exempt
def controller(request, pk=None):
    if request.method == 'DELETE':
        print request
        return remove_ocorrencia(pk)
    elif request.method == 'GET':
        if pk!=None:
            return get_ocorrencia(pk)
        else:
            return list_ocorrencias()
    elif request.method == 'PUT' or 'POST':
        print request.body+"\n"
        
        if (pk==None):
            print "NUEVO\n"
            return new_ocorrencia(request)
        else:
            return edit_ocorrencia(request,pk)