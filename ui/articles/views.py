from django.shortcuts import render


def all_articles(request, topic=None, author=None):
    if topic:
        context = {'filter': topic}
    elif author:
        context = {'filter': author}
    else:
        context = {'filter': 'All'}
    return render(request, 'articles/all_articles.html', context=context)


def single_article(request):
    return render(request, 'articles/single_article.html')
