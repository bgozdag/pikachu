from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Barista
from .forms import BaristaForm

def index(request):
    template = loader.get_template("app/index.html")
    return HttpResponse(template.render({}, request))


def baristas(request):
    template = loader.get_template("app/baristas.html")
    baristas_list = Barista.objects.all()
    context = {
        'baristas_list': baristas_list,
    }
    return HttpResponse(template.render(context, request))


def history(request):
    template = loader.get_template("app/history.html")
    return HttpResponse(template.render({}, request))


def createbarista(request):
    if request.method == "POST":
        form = BaristaForm(request.POST or None)
        if form.is_valid():
            form.save()
            template = loader.get_template("app/createbarista.html")
            return HttpResponse(template.render({}, request))
        else:
            return HttpResponseBadRequest()
    elif request.method == "GET":
        template = loader.get_template("app/createbarista.html")
        return HttpResponse(template.render({}, request))
    else:
        return HttpResponseBadRequest()


def createrecord(request):
    template = loader.get_template("app/createrecord.html")
    return HttpResponse(template.render({}, request))


def barista(request, barista_name):
    template = loader.get_template("app/barista.html")
    return HttpResponse(template.render({}, request))
