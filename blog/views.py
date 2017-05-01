from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.order_by('-post_date')
    return render(request, 'blog/index.html', {'posts': posts})


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})
