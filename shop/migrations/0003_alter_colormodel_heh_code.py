# Generated by Django 5.1.5 on 2025-01-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productmodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colormodel',
            name='heh_code',
            field=models.CharField(max_length=125),
        ),
    ]
