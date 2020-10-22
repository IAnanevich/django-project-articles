from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest

from blog_app.models import Author, Article, Comment, Category


class TestApi:
    @pytest.fixture()
    def setUp(self):
        Author.objects.create(
            first_name="firstname",
            last_name="lastname",
            email="user@gmail.com",
            photo=SimpleUploadedFile(
                name="adam.jpeg", content=open("media/author/adam.jpg", "rb").read()
            ),
        )

        Category.objects.create(
            name="category",
            description="about category"
        )

        Article.objects.create(
            title="test_title",
            description="about test title",
            author=Author.objects.get(),
            category=Category.objects.get(),
            image=SimpleUploadedFile(
                name="adam.jpeg", content=open("media/author/adam.jpg", "rb").read()
            ),
            register_date="2020-01-01"
        )

        Comment.objects.create(
            comment="test comment",
            author=Author.objects.get(),
            article=Article.objects.get(),
            date="2020-01-01"
        )

        self.client = APIClient()
        self.client.login()

    @pytest.mark.django_db
    def test_get_author(self, setUp):
        response = self.client.get("/author/")
        assert response.status_code == 200
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_category(self, setUp):
        response = self.client.get("/category/")
        assert response.status_code == 200
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_article(self, setUp):
        response = self.client.get("/article/")
        assert response.status_code == 200
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_comment(self, setUp):
        response = self.client.get("/comment/")
        assert response.status_code == 200
        assert len(response.data) == 1
