from django.http import HttpResponse
from django.shortcuts import render, redirect

from memelordapp.forms import AddPostForm
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
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
