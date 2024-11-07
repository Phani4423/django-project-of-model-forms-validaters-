from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from app.forms import *


def verify(request):
    SF = studentsforms()
    d = {'SF': SF }
    if request.method == 'POST':
        abc = studentsforms(request.POST)
        if abc.is_valid():
            abc.save()
            return HttpResponse('created')
        else:
            return HttpResponse('not created')
    return render(request,'verify.html',d)