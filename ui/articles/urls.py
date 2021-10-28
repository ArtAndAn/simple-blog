from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    # path('check/', views.data_check, name='data_check'),
    path('user/<str:author>', views.all_articles, name='user_articles'),
    path('topic/<str:topic>', views.all_articles, name='topic_articles'),
    path('article/<str:slug>', views.single_article, name='single_article')
]
