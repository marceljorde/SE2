from django.urls import path
from . import views
from .models import Post, Comment, Question, Choice, Todo 

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_screen, name='login_screen'),
    path('se2/', views.menue, name='menue'),

    path('se2/post/', views.post_list, name = 'post_list'),
    path('se2/post/<int:pk>/',views.post_detail,name='post_detail'),
    path('se2/post/new/', views.post_new, name='post_new'),
    path('se2/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('se2/post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('se2/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('se2/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('se2/poll/', views.poll, name='poll'),
    path('se2/poll/<int:question_id>/', views.detail, name='poll_detail'),
    path('se2/poll/<int:question_id>/results', views.results, name='poll_results'),
    path('se2/poll/<int:question_id>/vote/', views.vote, name='vote'),

    path('se2/todo/', views.todo, name='todo'),
    path('se2/todo/<int:todo_id>/', views.todo_detail, name='todo_detail'),

 
     
]