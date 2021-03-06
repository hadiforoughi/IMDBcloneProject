# Generated by Django 3.0.4 on 2020-03-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=400)),
                ('viewcount', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='movie')),
                ('category', models.CharField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('R', 'Romance')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'English'), ('Ge', 'Germany')], max_length=2)),
                ('yearOfProduction', models.DateField()),
                ('status', models.CharField(choices=[('RA', 'Recently added'), ('MW', 'Most Watched'), ('TR', 'Top reted')], max_length=2)),
            ],
        ),
    ]
