from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
# from models import User, Book, Review
import bcrypt
from collections import Counter

def index(request):
    return render(request, 'sf_con/index.html')
