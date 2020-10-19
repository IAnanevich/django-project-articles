from django.contrib import admin
from .models import Author, Article, Category, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
