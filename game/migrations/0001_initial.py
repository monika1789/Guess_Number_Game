# Generated by Django 4.2.11 on 2024-04-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_number', models.IntegerField()),
                ('min_range', models.IntegerField(default=1)),
                ('max_range', models.IntegerField(default=10)),
            ],
        ),
    ]