from django.shortcuts import render, redirect,get_object_or_404
from .models import Board, Comment
# Create your views here.
def board(request):
    boards = Board.objects
    return render(request, 'board.html', {'boards':boards})

def new(request):
    return render(request, 'new.html')

def create(request):
    print(request.method)
    if(request.method=='POST'):
        post = Board()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('board')

def detail(request, post_id):
    board = get_object_or_404(Board, pk = post_id)
    return render(request, 'detail.html', {'board':board})

def edit(request, post_id):
    board = get_object_or_404(Board, pk=post_id)
    return render(request, 'edit.html',{'board':board})

def update(request, post_id):
    board = get_object_or_404(Board, pk=post_id)
    board.title = request.POST['title']
    board.body = request.POST['body']
    board.save()
    return redirect('detail',post_id)

def delete(request, post_id):
    delete=get_object_or_404(Board, pk=post_id)
    delete.delete()
    return redirect('board')


def newreply(request):
    if(request.method == 'POST'):
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        comment.board = Board.objects.get(pk=request.POST['board']) # id로 객체 가져오기        
        comment.comment_user = request.POST['comment_user']
        # comment.comment_user = request.user.username
        comment.save()
        return redirect('detail', str(comment.board.id))
        # return redirect('/blog/'+ str(comment.blog.id))/
    else:
        return redirect('home') # 홈으로

# def comment_new(requset, pk):
#     print(request.method)
#     if request.method == 'POST':
#         comment = Board()
#         comment.title = request.POST['title']
#         board.body = request.POST['body']
#         board.save()

