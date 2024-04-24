from django.shortcuts import render, redirect
from . models import Adatbázismodell, Felhasználó
from email.message import EmailMessage
import ssl
import smtplib
import random
from . forms import Felhasználókészítés, Bejelentkezőformula
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
def emailküld_kzb(fogad):
    jelszó = "apor exza norl zdat "
    felad = "kzbwinneroffll@gmail.com"
    cím = "kzb azonosító"
    törzs = ""
    for i in range(5):
        törzs += str(random.randint(0,9))
    em = EmailMessage()
    em["From"] = felad
    em["To"] = fogad
    em["Subject"] = cím
    em.set_content(törzs)
    konteksztus = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=konteksztus) as smtp:
        smtp.login(felad, jelszó)
        smtp.sendmail(felad, fogad, em.as_string())
    return törzs
# Create your views here.
szabad_kód = False
kód = ""
i = 1
email_kód_hiba = 0
felhasználó = None

def zárol():
    global szabad_kód
    if szabad_kód == True:
        return 0
    else:
        return 1

def főoldal(request):
    global email_kód_hiba
    email_kód_hiba = 0
    print(request.user.is_authenticated)
    return render(request,"főoldal.html")

def bejelentkezés(request):
    global i
    global felhasználó
    if request.method == "GET":
        bejelentkezéssi_hiba = {"igené": i}
        i = 1
        return render(request, "bejelentkezés.html", bejelentkezéssi_hiba)
    elif request.method == "POST":
        form = Bejelentkezőformula(request, data=request.POST)
        print("asd")
        if form.is_valid():
            print("asd")
            email = request.POST.get("username")
            password = request.POST.get("password")
            felhasználó = authenticate(request, username=email, password=password)
            # print(felhasználó.get_username())
            if felhasználó is not None:
                #auth.login(request, felhasználó)
                return redirect("visszaigazol")
        else:
            i = 2
        return redirect("bejelentkezés")



        # szöveg = request.POST.get("jelszó")
        # szöveg2 = request.POST.get("e-mail")
        # for nber in Felhasználó.objects.all():        
        #     if nber.jelszó == szöveg and nber.e_mail == szöveg2:
        #         szabad = True
        #         i = 1
        #         return redirect("visszaigazol")
        # i = 2
        # return redirect("bejelentkezés")

def email_bejelentkezés_kód(request):
    global felhasználó
    global kód
    global szabad_kód
    global email_kód_hiba
    if request.method == "GET":
        if felhasználó is not None:
            if email_kód_hiba == 0:
                if szabad_kód == False:
                    kód = emailküld_kzb(felhasználó.get_username())
            email_bejelentkezés_kód_hiba = {"email_cód_hiba":email_kód_hiba}
            email_kód_hiba = 0
            return render(request, "email_bejelentkezés_kód.html", email_bejelentkezés_kód_hiba)
        else:
            return redirect("bejelentkezés")
    elif request.method == "POST":
        kód_be = request.POST.get("kód")
        if kód_be == kód:
            szabad_kód = True
            email_kód_hiba = 0
            auth.login(request, felhasználó)
            return redirect("választó")
        else:
            email_kód_hiba = 1
            return redirect("visszaigazol")

def kejelentkezés(request):
    global szabad_kód
    szabad_kód = False
    auth.logout(request)
    return redirect("főoldal")

def rólunk(request):
    return render(request, "rólunk.html", {"zárol": zárol()})

def választó(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "választó.html", {"zárol": zárol()})
        else:
            return redirect("bejelentkezés")

def soundboard(request):
    if request.user.is_authenticated:
        return render(request, "szaundbórd.html")
    else:
        return redirect("főoldal")

def zotler(request):
    if request.user.is_authenticated:
        return render(request, "zotler.html")
    else:
        return redirect("főoldal")



def regisztrál(request):
    form = Felhasználókészítés()
    # form = Felhasználókészítés({"email":"asddsa@gmail.com", "password1":"asdf0123", "password2":"asdf0123"})
    # form.save()
    if request.method == "POST":
        print(request.POST.get("email"))
        form = Felhasználókészítés(request.POST)
        if form.is_valid():
            form.save()
            return redirect("főoldal")
    konteksztus = {"regisztrálóformula":form}
    return render(request, "regisztrál.html", context=konteksztus)

def tesztlogin(request):
    form = Bejelentkezőformula()
    if request.method == "POST":
        form = Bejelentkezőformula(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = request.POST.get("username")
            password = request.POST.get("password")
            felhasználó = authenticate(request, username=email, password=password)
            if felhasználó is not None:
                auth.login(request, felhasználó)
                return redirect("főoldal")
    konteksztus = {"formula": form}
    return render(request, "tesztlogin.html", konteksztus)