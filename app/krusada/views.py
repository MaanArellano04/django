from django.http import HttpResponse
from django.template import loader

def krus(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def pic(request):
    template = loader.get_template('wallpaper.html')
    return HttpResponse(template.render())
def bili(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())