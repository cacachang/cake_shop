from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from .models import User
from .forms import UserForm

# Create your views here.



def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = User(**form.cleaned_data)
            user.save()

            return redirect("index")

    users = User.objects.all()    
    return render(request, "index.html", {"users": users})


def show(request, id=None):
    try:
        user = User.objects.get(id=id)
    except:
        return HttpResponse("沒有這號人物！", status=404)

    return render(request, "show.html", {"user": user})

def new(request):
    form = UserForm()
    return render(request, "new.html", {"form": form})

def edit(request, id=None):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user.name = form.cleaned_data["name"]
            user.age = form.cleaned_data["age"]
            user.email = form.cleaned_data["email"]
            user.address = form.cleaned_data["address"]
            user.phone = form.cleaned_data["phone"]

            user.save()

            return redirect("show", id=id)
    else:
        form = UserForm(user.__dict__)


    return render(request, "edit.html", {"form": form, "user": user})



def delete(request, id=None):
    if request.method == "POST":
        user = get_object_or_404(User, id=id)

        user.delete()
        return redirect("index")
    else:
        return HttpResponseNotAllowed(["POST"])