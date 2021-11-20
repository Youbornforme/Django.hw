from django.contrib import admin


from .models import Article, Author, Comment, Like, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'text')


class LikesAdmin(admin.ModelAdmin):
    list_display = ('like', 'comment', 'article')

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)