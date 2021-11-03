from django.shortcuts import render


def all_articles(request):
    context = {'api_link': '/api/', 'content': 'All'}
    return render(request, 'articles/all_articles.html', context=context)


def topic_articles(request, topic):
    context = {'api_link': f'/api/category/{topic}', 'content': topic}
    return render(request, 'articles/category_articles.html', context=context)


def author_articles(request, author):
    context = {'api_link': f'/api/user/{author}', 'content': author}
    return render(request, 'articles/author_articles.html', context=context)


def single_article(request, slug):
    return render(request, 'articles/single_article.html', context={'api_link': f'/api/article/{slug}'})


def check(request):
    return render(request, 'articles/check.html', context={'url': '/api/check'})
