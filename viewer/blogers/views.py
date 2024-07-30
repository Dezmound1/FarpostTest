from django.shortcuts import render
from .dash_app import app


def index(reqest):
    return render(reqest, "index.html")
