# Generated by Django 5.0.2 on 2024-02-24 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='en_profil',
            new_name='english_profil',
        ),
    ]
