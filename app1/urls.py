from django.urls import path
from . import views
urlpatterns = [
    path("", views.főoldal, name="főoldal"),
    path("adatbekero/", views.adatbekérő, name="adatbekérő"),
    path("bejelentkezes/", views.bejelentkezés, name= "bejelentkezés"),
    path("bejelentkezes/valaszto/", views.választó, name="választó"),
    path("bejelentkezes/valaszto/soundboard/", views.soundboard, name="soundboard"),
    path("bejelentkezes/valaszto/zotler/", views.zotler, name="zotler")
]
