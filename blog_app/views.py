from django.shortcuts import render, redirect
from .models import Article, Author, Category, Comment
from .forms import ArticleForm, AuthorForm, CategoryForm, CommentForm


# class ArticleView:
def home(request):
    context = {"all_info": Article.objects.all()}
    return render(request, "articles/home.html", context)


def get_users(request):
    context = {"all_info": Author.objects.all()}
    return render(request, "authors/authors.html", context)


def create(request):
    return render(request, "create.html")


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            author = form.cleaned_data.get("author")
            category = form.cleaned_data.get("category")
            image = form.cleaned_data.get("image")
            text_article = form.cleaned_data("text_article")
            obj = Article.objects.create(
                title=title,
                description=description,
                author=author,
                category=category,
                image=image,
                text_article=text_article,
            )
            obj.save()
            return redirect("home")
    form = ArticleForm()
    context = {"form": form}
    return render(request, "articles/create-article.html", context)


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            photo = form.cleaned_data.get("photo")
            obj = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                photo=photo,
            )
            obj.save()
            return redirect("authors")
    form = AuthorForm()
    context = {"form": form}
    return render(request, "authors/create-authors.html", context)


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {"form": form}
    return render(request, "categories/create-category.html", context)


def article_details(request, pk):
    article = Article.objects.get(pk=pk)
    author = article.author
    context = {"info": article, "author": author}
    return render(request, "articles/article-details.html", context)


def get_categories(request):
    context = {"all_info": Category.objects.all()}
    return render(request, "categories/categories.html", context)


def get_comments(request):
    context = {"all_info": Comment.objects.all()}
    return render(request, "comments/comments.html", context)


def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comments")
    form = CommentForm()
    context = {"form": form}
    return render(request, "comments/create-comment.html", context)
