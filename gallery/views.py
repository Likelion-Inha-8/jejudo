from django.shortcuts import render, redirect
# from akmai.edgeauth import EdgeAuth
import os
from .models import Post, Image

# Create your views here.

ET_ENCRYPTION_KEY = os.environ.get('AKAMAI_KEY')


def generateUrl(path, token):
    host = 'll-rcw-media-prod.scdn.pw'
    url = 'https://' + host + path + '?hdnts=' + token
    return url


def test(request):
    return render(request, 'test.html')


def view(request):
    #    et = EdgeAuth(**{'key': ET_ENCRYPTION_KEY,
    #                     'window_seconds': 3600})
    #    acl_path = "/images/{}/{}/*".format(group.id, post.id)
    #    token = et.generate_acl_token(acl_path)
    #    url = generateUrl(path, token)
    pass


def new(request):
    return render(request, 'new.html')


def edit(request):
    pass


def proc(request):
    if(request.method == 'POST'):
        if (request.POST['proc'] == 'new'):
            print(os.environ.get('S3_SECRET_KEY'))
            post = Post()
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.user = request.user
            post.save()
            for img in request.FILES.getlist('imgs'):
                image = Image()
                image.post = post
                image.user = request.user
                image.image = img
                image.save()
    return redirect('home')


def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})
