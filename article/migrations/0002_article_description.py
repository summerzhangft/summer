# Generated by Django 2.0.dev20170502021905 on 2017-08-25 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]