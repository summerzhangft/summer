# Generated by Django 2.0.dev20170502021905 on 2017-09-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(editable=False),
        ),
    ]
