from django.urls import path
from gallery import views
app_name = "gallery"
urlpatterns = [
    path('test', views.test, name="test"),
    path('new', views.new, name="new"),
    path('', views.home, name="home"),
    path('proc', views.proc, name="proc"),
]
