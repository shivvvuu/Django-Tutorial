# Generated by Django 4.1.5 on 2023-04-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='alum_logo',
            field=models.ImageField(upload_to=''),
        ),
    ]