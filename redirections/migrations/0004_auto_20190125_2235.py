# Generated by Django 2.1.5 on 2019-01-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirections', '0003_auto_20190125_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirection',
            name='host',
            field=models.CharField(default='djredirector.labs.maroto.me', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='redirection',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterUniqueTogether(
            name='redirection',
            unique_together={('host', 'path')},
        ),
    ]
