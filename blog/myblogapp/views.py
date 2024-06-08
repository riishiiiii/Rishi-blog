from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def hello(request: object) -> object:
    posts = PostModel.objects.all()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("/blog")
    else:
        form = PostModelForm()
    context = {"posts": posts, "form": form}
    return render(request, "blog/index.html", context)


@login_required
def post_details(request: object, pk: int) -> object:
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect("blog-post-detail", pk=post.id)

    else:
        c_form = CommentForm()
    context = {"post": post, "c_form": c_form}
    return render(request, "blog/post_detail.html", context)


@login_required
def post_edit(request: object, pk: int) -> object:
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog-post-detail", pk=post.id)

    else:
        form = PostUpdateForm(instance=post)
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "blog/post_edit.html", context)


@login_required
def post_delete(request: object, pk: int) -> object:
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("/blog")
    context = {"post": post}
    return render(request, "blog/post_delete.html", context)


def social_share(request: object, pk: int) -> object:
    post = PostModel.objects.get(id=pk)
    context = {"post": post}
    return render(request, "social.html", context)


def myblogs(request: object) -> object:
    email = request.session["email"]
    user = User.objects.get(email=email)
    posts = PostModel.objects.filter(author=user)
    context = {"posts": posts}
    return render(request, "blog/myblogs.html", context)
