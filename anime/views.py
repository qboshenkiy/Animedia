from django.shortcuts import render
from .models import postAdd

# Create your views here.
def index(req):
    return render(req, 'index.html', context={'post': postAdd.objects.all()})