from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path("home", views.home),
    path("home/<int:id>", views.home),
    path("home/<int:id>/<int:play_list>", views.home),
    path("", views.redirectHome),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
