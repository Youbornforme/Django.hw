from django.shortcuts import render
from django.http import HttpResponse

import random
import string


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s

def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
    })

def first(request):
    return render(request, 'first.html')


def main_article(request):
    return render(request, 'main_article.html')


def archive_article(request): 
    return render(request, 'archive_article.html')


def users(request):
    return render(request, 'users.html')


def article_number(request, *callback_args, **callback_kwargs):
    my_num = callback_kwargs.get('article_number')
    return render(request, 'article_number.html', {
        'check': my_num % 2,
    })


def article_number_archive(request, *callback_args, **callback_kwargs):
    my_num = callback_kwargs.get('article_number')
    return render(request, 'article_number.html', {
        'check': my_num % 2,
    })


def article_number_text(request, *callback_args, **callback_kwargs):
    my_num = callback_kwargs.get('article_number')
    text = callback_kwargs.get('slug_text')
    return render(request, 'article_number.html', {
        'check': my_num % 2,
        'text': text,
    })


def article_user_number(request, *callback_args, **callback_kwargs):
    return HttpResponse("article_user_number")


def phone_number(request, *callback_args, **callback_kwargs):
    return HttpResponse("right_phone_number")


def hexadecimal(request, *callback_args, **callback_kwargs):
    return HttpResponse("right_hexadecimal")


def random_page(request, *callback_args, **callback_kwargs):
    pages = ['first.html', 'main_article.html', 'archive_article.html', 'users.html']
    rnd_page = pages[random.randint(0, 3)]
    return render(request, rnd_page)


def random_slug(request):
    letters = string.ascii_lowercase
    pages = ['main_article.html', 'archive_article.html', 'users.html']
    rnd_page = pages[random.randint(0, 2)]
    rnd_slug = ''.join(random.choice(letters) for i in range(random.randint(5,10)))
    return render(request, rnd_page, {
        'text': rnd_slug,
    })
    
