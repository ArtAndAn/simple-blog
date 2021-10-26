from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_articles),
    # path('check/', views.data_check, name='data_check'),
    # path('category/<str:category>', views.category_articles, name='category_articles'),
    # path('user/<str:author>', views.user_articles, name='user_articles'),
    # path('article/<str:slug>', views.single_article, name='single_article')
]
