# Generated by Django 4.2.2 on 2023-07-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='photo',
            field=models.ImageField(default='defaults/singer-default.png', upload_to='hiphop/singers/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='song',
            name='photo',
            field=models.ImageField(default='defaults/song-default.jpg', upload_to='hiphop/sings/%Y/%m/%d'),
        ),
    ]
