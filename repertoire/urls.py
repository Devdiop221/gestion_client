"""repertoire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gestionClient.views import home, about, contact_list, new_contact, contact_details, edit_contact, delete_contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("contacts/", contact_list, name="contacts"),
    path("contacts/new/", new_contact, name = "new_contact"),
    path("contacts/<int:id>/", contact_details, name="details"),
    path("contacts/edit/<int:id>/", edit_contact, name="edit_contact"),
    path("contacts/delete/<int:id>/", delete_contact, name="delete_contact")
]
