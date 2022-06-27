from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogs:post', post_id=post.id)
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)
