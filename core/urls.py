from django.urls import path
from core import views
from .views import LikeView, AddQueryView

urlpatterns = [
    path('',views.index,name="index"),
    path('blog',views.blog,name='blog'),
    path('post/<slug>/',views.posts,name='posts'),
    path('pquery',views.pquery,name="pquery"),
    path('pcomment/<int:pk>',views.pcomment,name="pcomment"),
    path('pcomment/csave',views.csave,name="csave"),
    path('psave',views.psave,name="psave"),
    path('like/<int:pk>', LikeView, name='like'),
    path('addquery',AddQueryView.as_view(),name="addquery"),
    path('knowscore',views.knowscore,name='knowscore'),
    path('Diet', views.diet,name="Diet"),
    path('dietres',views.dietres,name='dietres'),

]