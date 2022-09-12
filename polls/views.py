from msilib.schema import Class
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request
from .models import Color
from django.views.generic import ListView


def index(request):
    return HttpResponse("Hello, world!")

class Colorlistview(ListView):
    model = Color
    template_name = 'main.html'
    #return ListView.as_view()(request, queryset=Color.objects.filter(hex=hex),
    #   template_name = 'main.html')