from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'inicio/index.html', context)

def post(request, pk):
    post = Post.objects.get(pk=pk)
    context={'post':post}
    return render(request, 'inicio/post.html',context)

def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    context={'form':form}
    return render(request, 'inicio/form_post.html', context)