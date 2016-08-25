from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User, Poke
import bcrypt
from collections import Counter

def index(request):
    return render(request, 'sf_con/index.html')

def test(request):
    return render(request, 'sf_con/test.html')

def user_page(request, user_id):
    return render(request, 'sf_con/user.html')
