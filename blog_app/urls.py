from django.urls import path, include
from blog_app import views


urlpatterns = [
    path("create-article/", views.create_article),
]