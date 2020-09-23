from django.urls import path
from board import views
app_name = "board"
urlpatterns = [
    path('', views.board, name='board'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name="edit"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete,name="delete"),
    path('newreply/<int:post_id>', views.newreply, name="newreply"),
    path('comment_delete/<int:post_id>/<int:comment_id>', views.comment_delete, name="comment_delete"),   
    path('board_list/', views.board_list, name='board_list'),
]
