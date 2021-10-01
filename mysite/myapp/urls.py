from django.urls import path,re_path

from .views import index, first, main_article, archive_article, users, article_number, article_number_archive
from .views import article_number_text, article_user_number, phone_number, hexadecimal, random_slug, random_page

urlpatterns = [
    path('', index, name='index'),
    path('first', first, name='first'),
    path('articles', main_article, name='main_article'),
    path('articles/archive/', archive_article, name='archive_article'),
    path('users/', users, name='users'),
    path('article/<int:article_number>/', article_number, name='article_number'),
    path('article/<int:article_number>/archive,/', article_number_archive, name='article_number'),
    path('article/<int:article_number>/<slug:slug_text>/', article_number_text, name='article_number'),
    path('users/<int:user_number>/', article_user_number, name='article_number'),
    re_path(r'^articles/(050|063|095)([0-9]{7})/', phone_number, name='phone_number'),
    re_path(r'^articles/(([a-f]|[0-9]){4}-([a-f]|[0-9]){6})/', hexadecimal, name='hexadecimal'),
    path('random_page/', random_page, name='random_page'),
    path('random_slug/', random_slug, name='random_slug')
]