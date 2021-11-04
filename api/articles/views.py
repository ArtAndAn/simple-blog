import random

from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Article, Category
from .serializers import ArticleFullSerializer


class AllArticles(ListAPIView):
    """View for showing all articles (only GET method)"""
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer


class CategoryArticles(ListAPIView):
    """View for showing all articles filtered by category (only GET method)"""
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer

    def get_queryset(self):
        articles = Article.objects.filter(category__name=self.kwargs['category'].title())
        return articles


class AuthorArticles(ListAPIView):
    """View for showing all articles filtered by author (only GET method)"""
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer

    def get_queryset(self):
        articles = Article.objects.filter(author__username=self.kwargs['author'])
        return articles


class SingleArticle(RetrieveAPIView):
    """View for showing single article data (only GET method)"""
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer
    lookup_field = 'slug'


def data_check(request):
    """
    View that checks:
        - if there are no categories in DB - add 20 categories;
        - if there are no users in DB - add 10 users;
        - if there are no articles in DB - add 1 article with random author and category from DB
    :return - redirect to AllArticles view
    """

    categories = Category.objects.all()
    users = User.objects.all()

    if not categories:
        cat_list = ['Photography', 'Investigations', 'Tech', 'World', 'Sports', 'Arts', 'Entertainment', 'Business',
                    'Climate', 'Environment', 'Education', 'Food', 'Health', 'History', 'Lifestyle', 'Media', 'Science',
                    'Weather', 'Magazine', 'Opinions']
        Category.objects.bulk_create([Category(name=category) for category in cat_list])

    if not users:
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
        Article(title='Motoball. A Big Ball Near the Fortress',
                text='Motoball is an exclusively European sport originating from France, which has gained enormous '
                     'popularity in Ukraine during Soviet Union times. Motoball tournaments and several motoball teams '
                     'have survived until today only on enthusiasm of players, coaches, and few spectators. In '
                     'Kamianets-Podilskyi motoball has already been existing for 52 years, and with a lack of local '
                     'teams’ success in other sports, the Podillia motoball club has become famous in Ukraine during '
                     'this time. There is a separate motoball stadium that you can find only in Kamianets-Podilskyi. '
                     'Here, motoball is a local highlight, still unknown to many guests. '
                     'Amotoball match is played on a football field with slightly different marks: the field doesn’t '
                     'have a central circle, and the goalpost area has a semi-circle shape. Asphalt and gravel are '
                     'usually used as a field cover. To improve motorcycle maneuverability, the asphalt is lightly '
                     'sprinkled with sand. The ball used for the sport is several times bigger than a football. Each '
                     'team has five players including a goalkeeper, and all players, with not exception, are on '
                     'motorcycles. In English, motoball is also called “motorcycle polo”. '
                     'There is almost no difference between a motoball bike and a regular cross motorcycle. The main '
                     'difference lies in the control levers. The motoball motorcycle is equipped with a duplicated '
                     'rear-brake pedal on either side of the bike. Since a motoball player uses one leg to control the '
                     'ball, the front wheel is armed with arches for moving the ball. The front of the motorcycle is '
                     'also equipped with “plows” that make it impossible for the ball to get under the motorcycle. In '
                     'some motorcycles of this type, gear-shift levers are connected directly to the handlebar to '
                     'control the motorcycle easier. '
                     'From a motorcyclist to a minibus driver'
                     'The oldest motoball player and the Kamianets-Podilskyi team captain, Volodymyr Danyliak, was once'
                     ' in demand by many teams, but now he earns his living by driving a minibus. For six months he '
                     'works in Kyiv, and then, after the motoball season starts, he returns to Kamianets. Volodymyr’s '
                     'love for football on wheels has only grown with age. '
                     'Once in Sovetskiy Sport, a former Soviet newspaper that today is a Russian sports daily, there '
                     'was an article about “a big match under the walls of an old fortress”. It described the Kamianets'
                     ' fortress and the motoball. The city was known only for the motoball team and the fortress. Many '
                     'people were coming to watch the games in 2008 and 2009 — back then the team was winning almost '
                     'every match. '
                     '— Currently there is a rapid team rejuvenation. Because other teams have only two older men, and,'
                     ' well, I am the oldest in Ukraine, — said Volodymyr, 65. —I was training today — got such a buzz,'
                     'the real deal. My wife says, “Oh my god, you look so alive. Your eyes began to sparkle. '
                     'So come on. '
                     'Keep up with the training.” As for now I work as a minibus driver in Kamianets. So, I got off the'
                     ' route and had training, and now I’m going back to the route. For the last seven to eight years I'
                     ' have tried every job.',
                author=random.choice(User.objects.all()),
                category=random.choice(Category.objects.all())
                ).save()
    return redirect('all_articles')
