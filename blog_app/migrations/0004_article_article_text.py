# Generated by Django 3.1.2 on 2020-10-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20201025_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_text',
            field=models.TextField(default=1, verbose_name='Text'),
            preserve_default=False,
        ),
    ]
