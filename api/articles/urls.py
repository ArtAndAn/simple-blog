from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('', views.AllArticles.as_view(), name='all_articles'),
    path('check', views.data_check, name='data_check')
]
