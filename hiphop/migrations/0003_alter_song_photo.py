# Generated by Django 4.2.2 on 2023-07-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphop', '0002_singer_photo_song_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='photo',
            field=models.ImageField(default='defaults/song-default.jpg', upload_to='hiphop/songs/%Y/%m/%d'),
        ),
    ]