from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,"index.html")

def somma(request):
    dic = { 
        'var1' : random.randint(1,10),
        'var2' : random.randint(1,10)}
    return render(request, "somma.html", dic)

def media(request):
    lista1 = [random.randint(1,10)for i in range(0, 30)]
    lista1.append(random.randint(1,20))
    somma = 0
    media = 0

    for i in range (0,30):
        somma += lista1[i]
    media += somma / 30
    dic = {"lista1": lista1}

    return render(request,"media.html", dic)

def voti(request):
    return render(request, "voti.html")