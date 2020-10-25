from django.contrib import admin
from .models import Author, Article, Category, Comment


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "id",)


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
