from django.shortcuts import render
from forms.forms import FeedbackForm

def index_form(request):
    return render(request, 'formularios/index.html')

def form_modelform(request):
    if request.method == "GET":
        form = FeedbackForm()
        context = {
            'form':form
        }
        return render(request, 'formularios/formulario.html',context = context)
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            form = FeedbackForm()
            
        context = {
            'form':form
        }
        return render(request, 'formularios/formulario.html',context = context)
# Create your views here.
