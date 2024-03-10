from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
        # return HttpResponse('<h1> Hey,Welcome </h1>')
      features = Feature.objects.all()

      return render(request,'index.html', {'feature':features})

def counter(request):
        text = request.POST['text']
        amount_of_word = len(text.split())
        return render(request,'counter.html',{'amount':amount_of_word})

def register(request):
#        if request.method == 'POST':
              
   return render(request,'register.html')