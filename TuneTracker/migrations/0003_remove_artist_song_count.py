# Generated by Django 4.2.2 on 2024-01-13 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TuneTracker', '0002_artist_song_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='song_count',
        ),
    ]
