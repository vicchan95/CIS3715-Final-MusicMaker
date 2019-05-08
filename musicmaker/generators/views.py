from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

import sys
import os

# Create your views here.
class GeneratorView(DetailView):
    template_name = 'generators/generator.html'

def generator(request):
    return HttpResponse('Unable to run the algorithm. Try again.')