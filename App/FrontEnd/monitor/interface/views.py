from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render (request,'interface/index.html')

def my_sites(request):
    return render (request,'interface/my_sites.html')

def account(request):
    return render (request,'interface/account.html')