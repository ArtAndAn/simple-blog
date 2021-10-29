from django.shortcuts import render


def all_articles(request, topic=None, author=None):
    if topic:
        context = {'api_link': f'/api/category/{topic}', 'content': topic}
    elif author:
        context = {'api_link': f'/api/user/{author}', 'content': author}
    else:
        context = {'api_link': '/api/', 'content': 'All'}
    return render(request, 'articles/all_articles.html', context=context)


def single_article(request, slug):
    return render(request, 'articles/single_article.html', context={'url': f'article/{slug}'})


def check(request):
    return render(request, 'articles/check.html', context={'url': '/api/check'})

