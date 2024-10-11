from django.http import HttpResponse
from django.template import loader

def haha(request):
    template = loader.get_template('dasal.html')
    return HttpResponse(template.render())

def lala(request):
    template = loader.get_template('dasal2.html')
    return HttpResponse(template.render())

def kaka(request):
    template = loader.get_template('dasal3.html')
    return HttpResponse(template.render())