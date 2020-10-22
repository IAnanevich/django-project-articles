from django.shortcuts import render
import requests


# class ArticleView:
def create_article(request):
    return render(request, "article/create_article.html")
