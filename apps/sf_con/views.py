from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
# from models import User, Poke
import bcrypt


def index(request):
    return render(request, 'sf_con/index.html')

def test(request):
    return render(request, 'sf_con/test.html')
