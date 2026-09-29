from django.shortcuts import render

# Create your views here.
def index(request):
    # render toma el request y el archivo html que queremos mostrar
    return render(request, "home/index.html")


def contacto(request):
    # render toma el request y el archivo html que queremos mostrar
    return render(request, "home/contacto.html")