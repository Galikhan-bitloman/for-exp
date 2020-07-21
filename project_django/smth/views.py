from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request, question_id = 34):
    return render(request, 'smth/index.html', {'header': 'Inndex'})

def votes(request):
    return HttpResponse("Gello")





