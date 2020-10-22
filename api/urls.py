from django.urls import path
from api.views import CategoryViewSet, ArticleViewSet, AuthorViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r"article", ArticleViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"comment", CommentViewSet)

urlpatterns = router.urls
