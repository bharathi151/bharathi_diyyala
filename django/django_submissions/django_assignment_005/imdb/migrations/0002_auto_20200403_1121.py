# Generated by Django 3.0 on 2020-04-03 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast',
            old_name='actor_id',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='cast',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
