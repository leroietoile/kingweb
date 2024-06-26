# Generated by Django 5.0.2 on 2024-06-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0013_section_recollect_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('profession', models.CharField(blank=True, max_length=300)),
                ('age', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('facebook', models.CharField(blank=True, default='', max_length=200)),
                ('tiktok', models.CharField(blank=True, default='', max_length=200)),
                ('reddit', models.CharField(blank=True, default='', max_length=200)),
                ('discord', models.CharField(blank=True, default='', max_length=200)),
                ('telegram', models.CharField(blank=True, default='', max_length=200)),
                ('instagram', models.CharField(blank=True, default='', max_length=200)),
                ('twitter', models.CharField(blank=True, default='', max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=200)),
                ('english_profil', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
    ]
