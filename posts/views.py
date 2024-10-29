from django.shortcuts import render, redirect
from .import forms
from .import models
from .models import Post


def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')


def search_blog(request):
    query = request.GET.get("q")
    category = request.GET.get("category")
    results = Post.objects.all()

    if query:
        results = results.filter(title__icontains=query)
    if category:
        results = results.filter(category__name__icontains=category)

    return render(request, 'search_result.html', {"results": results, "query": query, "category": category})