from django.urls import path
from gallery import views

urlpatterns = [
    path('test', views.test, name="test"),
]
