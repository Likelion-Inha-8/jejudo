from django.urls import path
from board import views
urlpatterns = [
    path('', views.board, name='board'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name="edit"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete,name="delete"),
    path('newreply', views.newreply, name="newreply")    
]
