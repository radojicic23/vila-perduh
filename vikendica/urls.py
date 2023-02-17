from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcome, name='home'),
    path("contacts/", views.contacts, name='contacts'),
    path("features/", views.features, name='features'),
    path("about/", views.about, name='about')
]
