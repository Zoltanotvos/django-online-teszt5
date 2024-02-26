from django.shortcuts import render, redirect
from . models import Adatbázismodell, Felhasználó
# Create your views here.
jelszó = "kzbwinneroffll"
szöveg = ""
szöveg2 = ""
szabad = False
szabad2 = False
i = False
# print(list(Felhasználó.objects.all()))
def főoldal(request):
    global szöveg
    global szöveg2
    global szabad
    szöveg = ""
    szöveg2 = ""
    szabad = False
    return render(request,"főoldal.html", {"data": Adatbázismodell.objects.all()})
def adatbekérő(request):
    global szabad
    global szöveg2
    if request.method == "GET":
        global szöveg
        szöveg = ""
        szöveg2 = ""
        szabad = False
        return render(request, "adatbekérő.html")
    elif request.method == "POST":
        szöveg1 = request.POST.get("szöveg")
        szám1 = request.POST.get("szám")
        boool1 = request.POST.get("boool")
        if boool1 == "on":
            boool1 = True
        else:
            boool1 = False
        
        try:
            adatbázis_elem = Adatbázismodell(szöveg = szöveg1, szám = szám1, boool = boool1, id = list(Adatbázismodell.objects.all())[-1].pk + 1)
        except:
            adatbázis_elem = Adatbázismodell(szöveg = szöveg1, szám = szám1, boool = boool1, id = 1)

        adatbázis_elem.save()
        return redirect("főoldal")
def bejelentkezés(request):
    global szöveg
    global szöveg2
    global szabad
    global szabad2
    global i

    if request.method == "GET":
        
        szöveg = ""
        szöveg2 = ""
        szabad = False
        return render(request, "bejelentkezés.html", {"felhasználók":Felhasználó.objects.all(), "igené": i})
    elif request.method == "POST":
        szöveg = request.POST.get("jelszó")
        szöveg2 = request.POST.get("felhasználónév")
        for nber in Felhasználó.objects.all():        
            if nber.jelszó == szöveg and nber.név == szöveg2:
                szabad2 = True
                i = False
                return redirect("választó")
        i = True
        return redirect("bejelentkezés")
def választó(request):
    if request.method == "GET":
        global szöveg
        global szabad
        global szabad2
        if szabad2:
            
            szabad = True
            szabad2 = False
            return render(request, "választó.html")
        else:
            szabad = False
            return redirect("bejelentkezés")
def soundboard(request):
    global szabad
    if szabad:
        return render(request, "szaundbórd.html")
    else:
        return redirect("főoldal")
def zotler(request):
    global szabad
    if szabad:
        return render(request, "zotler.html")
    else:
        return redirect("főoldal")