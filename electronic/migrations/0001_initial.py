# Generated by Django 4.2.2 on 2023-07-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('photo', models.ImageField(default='defaults/singer-default.png', upload_to='electronic/singers/%Y/%m/%d')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('about', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='defaults/song-default.jpg', upload_to='electronic/songs/%Y/%m/%d')),
                ('release_date', models.DateField()),
                ('authors', models.ManyToManyField(to='electronic.singer')),
            ],
        ),
        migrations.AddIndex(
            model_name='singer',
            index=models.Index(fields=['slug'], name='electronic__slug_5453b0_idx'),
        ),
    ]
