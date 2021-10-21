from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView

from .models import Article, Category
from .serializers import ArticleFullSerializer


class AllArticles(ListAPIView):
    """View for showing all articles data (only GET method)"""
    queryset = Article.objects.all()

    def get_serializer_class(self):
        return ArticleFullSerializer


def data_check(request):
    if not Category.objects.all():
        cat_list = ['Photography', 'Investigations', 'Tech', 'World', 'Sports', 'Arts', 'Entertainment', 'Business',
                    'Climate', 'Environment', 'Education', 'Food', 'Health', 'History', 'Lifestyle', 'Media', 'Science',
                    'Weather', 'Magazine', 'Opinions']
        Category.objects.bulk_create([Category(name=category) for category in cat_list])
    if not User.objects.all():
        user_list = [
            {'name': 'irritabledirector', 'password': 'Wt}4t@X@~S2=/+pC'},
            {'name': 'starchyotter', 'password': 'M*43Hwkbk<YTqQ/@'},
            {'name': 'wombposse', 'password': 'k@_KHwmkSh7$d9wZ'},
            {'name': 'fireworkbeloved', 'password': '4Cwbbws</S2!3sb]'},
            {'name': 'cornettotrustee', 'password': 'csP<+7S!Ef97C'},
            {'name': 'choirbeloved', 'password': 'L{,+.w8wmQH]>e/a'},
            {'name': 'unsungduct', 'password': 'pV=E/ZhEd84?b";@'},
            {'name': 'fumerebel', 'password': 'Vs!$~MW8/%mX]8X%'},
            {'name': 'affectmalaysian', 'password': 'Zwq5;&SR9LWJSjc<'},
            {'name': 'fizzmojang', 'password': '<5Fg%Nyadh}X5:mc'}
        ]
        for user in user_list:
            User.objects.create_user(username=user['name'], password=user['password'])
    if not Article.objects.all():
        pass
    return redirect('all_articles')

