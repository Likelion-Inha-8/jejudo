from django.urls import path
from user import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('proc', views.proc, name="proc"),
    path('', views.home, name="home"),
]
