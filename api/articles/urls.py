from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('', views.AllArticles.as_view(), name='all_articles'),
    path('check/', views.data_check, name='data_check'),
    path('category/<str:category>', views.AllArticles.as_view(), name='category_articles'),
    path('user/<str:author>', views.AllArticles.as_view(), name='user_articles'),
    path('<str:slug>', views.SingleArticle.as_view(), name='single_article')
]
