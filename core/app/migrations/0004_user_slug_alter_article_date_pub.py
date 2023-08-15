# Generated by Django 4.2.4 on 2023-08-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(auto_created=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_pub',
            field=models.DateField(auto_now_add=True),
        ),
    ]