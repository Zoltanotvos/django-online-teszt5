# Generated by Django 4.2 on 2024-02-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Felhasználó',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('név', models.CharField(max_length=20)),
                ('jelszó', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'regisztrált felhasználók',
            },
        ),
    ]
