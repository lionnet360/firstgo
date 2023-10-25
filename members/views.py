from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



from django.views.generic import ListView, DetailView
from .models import Poost
from .formss import PostForm












def login_user(request):
        if request.method == 'POST':
                formmm = AuthenticationForm(data = request.POST)
                if formmm.is_valid():
                      
                      return redirect('hhhome')
        else:
            formmm = AuthenticationForm()              
        return render(request, 'logins.html', {"fform": formmm})
    

def register_user(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('www')
        else:
          form = UserCreationForm()       
        return render(request, 'register.html', {"formm": form})

def saclogs(request):
      return render(request, "saclog.html")

def ddd(request):
      return render(request, "dd.html")

@login_required
def profile(request):
      return render(request, 'pro.html')



@login_required
def add_pro(request):
      form = PostForm(request.POST or None, request.FILES or None)
      if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('hhhome')
        else:
                form = PostForm()  
      return render(request, 'add_post.html', {'form': form})