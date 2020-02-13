from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count

from memelordapp.forms import AddPostForm
from .models import Post

user = User.objects.annotate(post_count=Count('post')).order_by('-post_count').first()
postCount = Post.objects.all().count()
posts = Post.objects.all()
contribution = Post.objects.filter(author=user).count()
lastPostDate = Post.objects.order_by('-date_posted').first().date_posted


def home(request):
    context = {
        'posts': posts,
        'postsCount': postCount,
        'lastPostDate': lastPostDate,
        'memeLeader': user,
        'contribution': contribution
    }
    return render(request, 'memelordapp/home.html', context)


def myMemes(request):
    context = {
        'posts': Post.objects.filter(author=request.user),
        'postsCount': postCount,
        'lastPostDate': lastPostDate,
        'memeLeader': user,
        'contribution': contribution
    }
    return render(request, 'memelordapp/home.html', context)


def add_post_view(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, request=request)

        if form.is_valid():
            form.save()
            return redirect(home)

    else:
        form = AddPostForm()

    context = {
        'form': form,
        'postsCount': postCount,
        'lastPostDate': lastPostDate,
        'memeLeader': user,
        'contribution': contribution
    }
    return render(request, 'memelordapp/addpost.html', context)


def success(request):
    return HttpResponse('Meme Uploaded!!!')
