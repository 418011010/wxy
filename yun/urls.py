from django.urls import path
from . import views
urlpatterns = {
    path("helloApi", views.hello, name='hello')#第一个参数表示路径
}