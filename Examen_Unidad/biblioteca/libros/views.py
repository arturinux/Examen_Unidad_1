from django.shortcuts import render

# Create your views here.

def homeperro(request):
    context=locals()
    template='home.html'
    return render(request, template, context)
