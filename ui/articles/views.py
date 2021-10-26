from django.shortcuts import render


def all_articles(request):
    return render(request, 'articles/all_articles.html')
