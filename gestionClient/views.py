from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from gestionClient.models import Contact


def home(request):
    message = "Bonjour tout le monde!"
    context = {'message': message}
    return render(request, "pages/index.html", context)


def about(request):
    return render(request,"pages/about.html")


def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(auteur=user)
    return render(request,"contacts/contact_list.html", {"contacts": contacts})



def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, "contacts/contact_details.html", {"contact": contact})


def new_contact(request):
    if request.method == "POST":
        auteur = request.user
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        contact = Contact.objects.create(
            auteur=auteur,
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
        )

        contact.save()
        return redirect("/contacts/")

    return render(request, "contacts/new_contact.html")


def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        contact_to_update = Contact.objects.filter(pk=contact.id)
        contact_to_update.update(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            )
        return redirect("/contacts/")

    return render(request, "contacts/edit_contact.html", {"contact": contact})


def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact_to_delete = Contact.objects.filter(pk=contact.id)
        contact_to_delete.update(
            archive=True
            )
        contact.delete()
        return redirect("/contacts/")
    return render(request, "contacts/delete_contact.html", {"contact": contact})