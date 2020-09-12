from django.shortcuts import render
# from akmai.edgeauth import EdgeAuth
import os

# Create your views here.

ET_ENCRYPTION_KEY = os.environ.get('AKAMAI_KEY')


def generateUrl(path, token):
    host = 'll-rcw-media-prod.scdn.pw'
    url = 'https://' + host + path + '?hdnts=' + token
    return url


def test(request):
    return render(request, 'test.html')


def view(request):
    et = EdgeAuth(**{'key': ET_ENCRYPTION_KEY,
                     'window_seconds': 3600})
    acl_path = "/images/{}/{}/*".format(group.id, post.id)
    token = et.generate_acl_token(acl_path)
    url = generateUrl(path, token)
    pass


def new(request):
    pass


def edit(request):
    pass


def proc(request):
    pass
