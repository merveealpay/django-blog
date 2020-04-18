from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Başarılı bir şekilde oluşmuştur.")
            return redirect("post:index")
    # return redirect("post:index")
    else:
        form = PostForm()
    return render(request, 'post/form.html', {'form': form})


def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect(post.get_absolute_url())
    return render(request, 'post/form.html', {'form': form})


def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('post:index')
