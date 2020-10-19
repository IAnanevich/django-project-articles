from rest_framework.viewsets import ModelViewSet

from .serializers import ArticleSerializer, AuthorSerializer, CategorySerializer, CommentSerializer
from blog_app.models import Article, Author, Category, Comment


# Create your views here.
class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
