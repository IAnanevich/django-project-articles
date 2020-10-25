from .models import Article, Author, Category, Comment
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("title", "description", "author", "category", "image", "article_text")
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "article_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "email", "photo")
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name", "description")
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author", "article")
        widgets = {
            "comment": Textarea(attrs={
                "class": "form-control",
                "placeholder": "input",
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "placeholder": "input"
            }),
        }
