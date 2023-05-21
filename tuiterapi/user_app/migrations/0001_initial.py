# Generated by Django 4.2.1 on 2023-05-21 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('profile_picture', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_picture', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
