from django.urls import path

from . import views;

urlpatterns = [
    path("1/", views.debri_1),
    path("2/", views.debri_2),
    path("3/", views.debri_3),
    path("4/", views.debri_4)
]