from django.shortcuts import render
from .models import User, Post

def home(request):
    data = User.objects.first().post.all()  # type: ignore
    return render(request, 'pages/home.html', context={'data': data})