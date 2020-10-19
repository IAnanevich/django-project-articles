from blog_app.models import Category, Author, Article, Comment
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "email", "register_date", "photo", "url")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "description", "category", "author", "register_date", "image", "url")

    def to_representation(self, instance):
        rep = super(ArticleSerializer, self).to_representation(instance)
        rep['author'] = f"{instance.author.first_name} {instance.author.last_name}"
        rep['category'] = instance.category.name
        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "description", "url")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("comment", "article", "author", "date", "url")

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['author'] = f"{instance.author.first_name} {instance.author.last_name}"
        rep['article'] = instance.article.title
        return rep
