from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count

from memelordapp.forms import AddPostForm
from .models import Post


def home(request):
    user = User.objects.annotate(post_count=Count('post')).order_by('-post_count').first()
    context = {
        'posts': Post.objects.all(),
        'postsCount': Post.objects.all().count(),
        'lastPostDate': Post.objects.order_by('-date_posted').first().date_posted,
        'memeLeader': user,
        'contribution': Post.objects.filter(author=user).count()
    }
    return render(request, 'memelordapp/home.html', context)


def myMemes(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
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
    return render(request, 'memelordapp/addpost.html', {'form': form})


def success(request):
    return HttpResponse('Meme Uploaded!!!')
