# Generated by Django 5.0.2 on 2024-03-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_alter_visitormessage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitormessage',
            name='recieving_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
