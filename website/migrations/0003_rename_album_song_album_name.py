# Generated by Django 5.1.3 on 2024-12-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_part_of_song_album_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='album_name',
        ),
    ]
