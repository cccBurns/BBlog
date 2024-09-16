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

def deletePost (request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    
    context = {'post':post}
    
    return render(request, 'delete_template.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    update = 1
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        form.save()
        return redirect('index')
    
    context = {'form': form, "update": update}
    return render(request, 'inicio/form_post.html', context)