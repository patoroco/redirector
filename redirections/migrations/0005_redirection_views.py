# Generated by Django 2.1.5 on 2019-02-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirections', '0004_auto_20190125_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirection',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
