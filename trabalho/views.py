from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("index.html")
    context = {
        "title": "programa em python",
        "information": "Gui GEY"
    }
    return HttpResponse(template.render(context, request))