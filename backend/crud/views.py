from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Blood
from .forms import CreateBlood

def some(self, request):
    return HttpResponse("Hello")

def readBlood(request):
    blood = Blood.objects.all()

    context = {"blood": blood}

    return render(request, "blood_read.html", context )

def createBlood(request):
    if request.method == "GET":
        return render(request,"index.html")
    if request.method == "POST":
        blood = CreateBlood(request.POST)
        if blood.is_valid():
            blood.save()
            return redirect("/crud/readblood")

        return HttpResponse("Blood not created")

    
def editBlood(request, id):
    if request.method == "POST":
        blood_instance = Blood.objects.get(id=id)
        blood = CreateBlood(request.POST, instance=blood_instance)
        if blood.is_valid():
            blood.save()
            return redirect("/crud/readblood")
    if request.method == "GET":
        blood = Blood.objects.get(id=id)
        print(blood)
        return render(request, "blood_update.html", {"blood": blood})


def deleteBlood(request, id):
    blood = Blood.objects.get(id=id)

    blood.delete()

    return redirect("/crud/readblood")