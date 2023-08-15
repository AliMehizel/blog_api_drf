from django.urls import path
from .views import *




urlpatterns = [
    #articles
    
    path('articles/', GetArticles, name='articles'),
    path('p-articles/',GetPArticles, name='particles'),
    path('article/<str:pk>/', GetArticle, name='article'),
    path('create-article/', createArticle, name='create-article'),
    path('update-article/<str:pk>/',updateArticle,name='update-article'),
    path('delete-article/<str:pk>/', deleteArticle,name='delete-article'),
    #comments
    path('comments/<str:pk>/', GetComment, name='comments'),
    path('comments/', createComment, name='comments'),
    #rating it included with articles view
    path('ratings/', addRating, name='ratings'),
    
]