from django.db import models


# Create your models here.
class Author(models.Model):
    """Author"""

    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    email = models.EmailField("Email")
    register_date = models.DateField("Registration date", auto_now=True)
    photo = models.ImageField("Photo", null=True, blank=False, upload_to="author/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(models.Model):
    """Category"""

    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    """Article"""

    title = models.CharField("Title", max_length=30)
    description = models.TextField("Description", max_length=1000)
    author = models.ForeignKey(
        Author, verbose_name="Author", on_delete=models.PROTECT, null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.PROTECT, null=True
    )
    image = models.ImageField("Image", null=True, blank=False, upload_to="article/")
    register_date = models.DateField("Registration date", auto_now=True)
    article_text = models.TextField("Text")

    def __str__(self):
        return self.title

    def short_description(self):
        return self.description[:20]

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    """Comment"""

    comment = models.TextField("Comment")
    author = models.CharField("Name", max_length=100)
    article = models.ForeignKey(Article, verbose_name="Article", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} -> {self.article}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
