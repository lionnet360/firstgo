from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from members.models import Poost

from .models import Post

    

def hoome(request):
    pooosts = Poost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'poosts': pooosts})


