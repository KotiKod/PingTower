from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,'interface/index.html')

def about(request):
    return HttpResponse("<h4>About</4>")