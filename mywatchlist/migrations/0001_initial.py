# Generated by Django 4.1 on 2022-09-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=30)),
                ('title', models.TextField()),
                ('rating', models.CharField(max_length=5)),
                ('release_date', models.CharField(max_length=50)),
                ('review', models.TextField()),
            ],
        ),
    ]
