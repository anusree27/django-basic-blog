from django.shortcuts import render
from .models import Blogs
# Create your views here.
def home(request):
    blogs = Blogs.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'home.html', context)

def blog(request,pk):
    blog = Blogs.objects.get(id=pk)
    context = {'blog':blog}
    return render(request, 'blog.html', context)