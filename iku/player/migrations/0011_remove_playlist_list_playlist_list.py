# Generated by Django 5.0.4 on 2024-05-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0010_remove_playlist_list_playlist_list"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="list",
        ),
        migrations.AddField(
            model_name="playlist",
            name="list",
            field=models.ManyToManyField(blank=True, default=1, to="player.song"),
        ),
    ]
