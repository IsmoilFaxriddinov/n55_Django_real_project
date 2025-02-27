# Generated by Django 5.1.4 on 2025-01-18 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthormodel',
            name='avatar',
            field=models.ImageField(upload_to='blogs/avatars/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='blogauthormodel',
            name='first_name',
            field=models.CharField(max_length=125, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='blogauthormodel',
            name='last_name',
            field=models.CharField(max_length=125, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='blogauthormodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blogs.blogauthormodel', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='blogauthormodel',
            name='title',
            field=models.CharField(max_length=125, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogcategorymodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blogs.blogcategorymodel', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='blogcategorymodel',
            name='title',
            field=models.CharField(max_length=125, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='author',
            field=models.ManyToManyField(to='blogs.blogauthormodel', verbose_name='blog_author'),
        ),
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='categories',
            field=models.ManyToManyField(to='blogs.blogcategorymodel', verbose_name='blogs'),
        ),
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='comment',
            field=models.CharField(max_length=125, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.ManyToManyField(to='blogs.blogauthormodel', verbose_name='blogs'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='categories',
            field=models.ManyToManyField(to='blogs.blogcategorymodel', verbose_name='blog'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blogs', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=125, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogtagmodel',
            name='title',
            field=models.CharField(max_length=125, verbose_name='title'),
        ),
    ]
