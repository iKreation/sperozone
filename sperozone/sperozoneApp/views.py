from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import simplejsons

from sperozoneApp.models import Ocorrencia

class IndexView(generic.ListView):
    template_name = 'sperozoneApp/index.html'
    context_object_name = 'lista_de_ocorrencias'

    def get_queryset(self):
        return Ocorrencia.objects.all()


class DetailView(generic.DetailView):
    model = Ocorrencia
    template_name = 'sperozoneApp/detail.html'

def index(request):
	ocorrencias = Ocorrencia.objects.all()
	context = {'lista_de_ocorrencias':ocorrencias}
	return render(request,'sperozoneApp/index.html',context)

def get_ocorrencia(request, ocorrencia_id):
	ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
	return render(request, 'sperozoneApp/detail.html',{'ocorrencia':ocorrencia})

def remove_ocorrencia(oc_id):
    return Ocorrencia.objects.filter(id=oc_id).delete()

def edit_ocorrencia(request, oc_id):
    ocorrencia = Ocorrencia.objectos.filter(id=oc_id)
    data = simplejson.loads(request.body)
    ocorrencia.title = data['title']
    ocorrencia.description = data['description']
    ocorrencia.report_date = timezone.now()
    ocorrencia.status = data['title']
    ocorrencia.save()
    return

def new_ocorrencia(request):
    data = simplejson.loads(request.body)

    ocorrencia = Ocorrencia(title=data['title'],description=data['description'],report_date=timezone.now(),status=data['status'])
    ocorrencia.save()
    return

def controller(request, oc_id):
    if request.method == 'DELETE':
        return remove_ocorrencia(oc_id)
    elif request.method == 'GET':
        return get_ocorrencia(request,oc_id)
    elif request.method == 'PUT' or 'POST':
        data = simplejson.loads(request.body)
        if data.has_key('id') and data['id'] == 0:
            return new_ocorrencia(request)
        else:
            return edit_ocorrencia(request,oc_id)