# Generated by Django 3.0 on 2020-03-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querying', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date publllished')),
            ],
        ),
    ]
