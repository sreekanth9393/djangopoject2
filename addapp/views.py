from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    try:
        x=request.GET["t1"]
        y=request.GET["t2"]
        i=int(x)
        j=int(y)
        k=i+j
        return HttpResponse("<html><body bgcolor=gray><h1>sum is:"+str(k)+"</h1></body></html>")
    except(ValueError):
        return render(request,'input.html')
