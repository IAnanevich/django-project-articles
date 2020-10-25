from django.urls import path, include
from blog_app import views


urlpatterns = [
    path("", views.home, name="home"),
    path("authors/", views.get_users, name="authors"),
    path("categories/", views.get_categories, name="categories"),
    path("comments/", views.get_comments, name="comments"),
    path("create/", views.create, name="create"),
    path("create/comment", views.create_comment, name="create-comment"),
    path("create/article", views.create_article, name="create-article"),
    path("create/author", views.create_author, name="create-author"),
    path("create/category", views.create_category, name="create-category"),
    path("<int:pk>", views.article_details, name="article-details"),
]