from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def show(request, id=None):
    print(id)
    return HttpResponseRedirect(reverse("admin:index"))
