# Generated by Django 3.0.7 on 2020-06-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200611_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(default='https://google.com'),
        ),
    ]
