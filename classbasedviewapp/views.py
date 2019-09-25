from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        try:
            a=request.GET['t1']
            x=int(a)
            b=request.GET['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=cyan><h1>sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            print("invalid input")
    def post(self,request):
        try:
            a=request.POST['t1']
            x=int(a)
            b=request.POST['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=lightgreen><h1>sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            print("invalid input")
def index(request):
    return render(request,'index.html')