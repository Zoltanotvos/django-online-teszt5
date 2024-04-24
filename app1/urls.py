from django.urls import path
from . import views
urlpatterns = [
    path("", views.főoldal, name="főoldal"),
    path("bejelentkezes/", views.bejelentkezés, name="bejelentkezés"),
    path("kijelentkezés/", views.kejelentkezés, name="kijelentkezés"),
    path("bejelentkezes/visszaigazol/", views.email_bejelentkezés_kód, name="visszaigazol"),
    path("bejelentkezes/valaszto/", views.választó, name="választó"),
    path("bejelentkezes/valaszto/soundboard/", views.soundboard, name="soundboard"),
    path("bejelentkezes/valaszto/zotler/", views.zotler, name="zotler"),
    path("rolunk/", views.rólunk, name="rólunk"),
    path("regisztral/", views.regisztrál, name="regisztrál"),
    path("tesztbejelentkezés/", views.tesztlogin, name="tesztlogin"),
]
