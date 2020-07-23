# Generated by Django 3.0 on 2020-03-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querying', '0003_auto_20200323_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='querying.Entry')),
            ],
        ),
    ]