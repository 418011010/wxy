from django.urls import path
from . import views,tdb
urlpatterns = {
    path("helloApi", views.hello, name='hello'),#第一个参数表示路径
    path("test", views.test, name='test'),#第一个参数表示路径
    path("tdb", tdb.testdb)
}