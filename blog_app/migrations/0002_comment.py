# Generated by Django 3.1.2 on 2020-10-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.article', verbose_name='Article')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.author', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
