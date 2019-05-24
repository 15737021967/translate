from django.shortcuts import render, HttpResponse
from .models import *
from packages.middleware import Translate
import json
# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        stringType = request.POST.get('translateType')
        words = request.POST.get('words')
        froms, to = stringType.split('2')
        trans = Translate(froms, to, words)
        word = trans.get_translate()
        # print(froms, to, word)
        return HttpResponse(json.dumps(word))






