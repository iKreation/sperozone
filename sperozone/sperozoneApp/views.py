from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

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

def detail(request, poll_id):
	ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
	return render(request, 'sperozoneApp/detail.html',{'ocorrencia':ocorrencia})