from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.


def board(request):
    boards = Board.objects.order_by('-created_at')
    return render(request, 'board.html', {'boards': boards})


def new(request):
    return render(request, 'new.html')


def create(request):
    print(request.method)
    if(request.method == 'POST'):
        post = Board()
        post.title = request.POST['title']
        post.writer = request.user
        post.body = request.POST['body']
        post.save()
    return redirect('board')


def detail(request, post_id):
    board = get_object_or_404(Board, pk=post_id)
    return render(request, 'detail.html', {'board': board})


def edit(request, post_id):
    # board = Board.objects.get(id=post_id)
    board = get_object_or_404(Board, pk=post_id)
    try:
        if(board.writer == request.user):
            return render(request, 'edit.html', {'board': board})
        return render(request, 'message.html', {'message': '수정불가: 당신의 게시글이 아닙니다.','urltype':'detail_id', 'd_id':board.pk})
    except Board.writer.RelatedObjectDoesNotExist:
        return render(request, 'message.html', {'message': '수정불가: 당신의 게시글이 아닙니다.','urltype':'detail_id', 'd_id':board.pk})
        

def update(request, post_id):
    board = get_object_or_404(Board, pk=post_id)
    board.title = request.POST['title']
    board.body = request.POST['body']
    board.save()
    return redirect('detail', post_id)


def delete(request, post_id):
    board = Board.objects.get(id=post_id)
    try:
        if(board.writer == request.user):
            delete = get_object_or_404(Board, pk=post_id)
            delete.delete()
            return redirect('board')
        return render(request, 'message.html', {'message': '삭제불가: 당신의 게시글이 아닙니다.', 'urltype':'detail_id', 'd_id':board.pk})
    except Board.writer.RelatedObjectDoesNotExist:
        return render(request, 'message.html', {'message': '삭제불가: 당신의 게시글이 아닙니다.', 'urltype':'detail_id', 'd_id':board.pk})
    

def newreply(request, post_id):
    if(request.method == 'POST'):
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        # comment.board = Board.objects.get(pk=request.POST['board']) # id로 객체 가져오기
        comment.board = get_object_or_404(Board, pk=post_id)
        # comment.comment_user = request.POST['comment_user']
        comment.comment_user = request.user
        comment.save()
        return redirect('detail', str(comment.board.id))
    else:
        return redirect('board')  # 홈으로


def comment_delete(request, post_id, comment_id):
    # if(request.method == 'POST'):
    post = get_object_or_404(Board, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    try:
        if(comment.comment_user == request.user):
            comment.delete()
            return redirect('detail', str(comment.board.id))
        return render(request, 'message.html', {'message': '삭제불가: 당신의 댓글이 아닙니다.', 'urltype':'detail_id', 'd_id':post.pk})
    except Board.writer.RelatedObjectDoesNotExist:
        return render(request, 'message.html', {'message': '삭제불가: 당신의 댓글이 아닙니다.', 'urltype':'detail_id', 'd_id':post.pk})

    
def board_list(request):
    # boards = Board.objects
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 6)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})