from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

import sys
import os

# Create your views here.
class GeneratorView(DetailView):
    template_name = 'generators/generator.html'

def generator(request):
    try:
        os.system('python3 train.py')
        os.system('python3 predict.py')
        os.system('python3 playsong.py')
    except:
        return HttpResponse('Unable to run the algorithm. Try again.')