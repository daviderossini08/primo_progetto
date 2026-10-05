from django.shortcuts import render

# Create your views here.

def index_root (request):
    return render(request,"index_root.html")

def es_if(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    dic = { 'var1' : 200,
    'var2' : 200,
    'var3' : 300 }
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render(request, "es_if.html", dic)
