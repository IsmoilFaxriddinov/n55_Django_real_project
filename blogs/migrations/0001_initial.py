# Generated by Django 5.1.4 on 2025-01-14 10:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'blog tag',
                'verbose_name_plural': 'blog tags',
            },
        ),
        migrations.CreateModel(
            name='BlogAuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('avatar', models.ImageField(upload_to='blogs/avatars/')),
                ('title', models.CharField(max_length=125)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blogs.blogauthormodel')),
            ],
            options={
                'verbose_name': 'Blog author',
                'verbose_name_plural': 'Blog authors',
            },
        ),
        migrations.CreateModel(
            name='BlogCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=125)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blogs.blogcategorymodel')),
            ],
            options={
                'verbose_name': 'blog category',
                'verbose_name_plural': 'blog cetegories',
            },
        ),
        migrations.CreateModel(
            name='BlogCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('comment', models.CharField(max_length=125)),
                ('author', models.ManyToManyField(related_name='blog_author', to='blogs.blogauthormodel')),
                ('categories', models.ManyToManyField(related_name='blogs', to='blogs.blogcategorymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog comment',
                'verbose_name_plural': 'Blog comments',
            },
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='blogs')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
                ('author', models.ManyToManyField(related_name='blogs', to='blogs.blogauthormodel')),
                ('categories', models.ManyToManyField(related_name='blog', to='blogs.blogcategorymodel')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
