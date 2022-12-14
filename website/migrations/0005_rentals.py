# Generated by Django 4.1.1 on 2022-10-13 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rating_delete_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_films', models.CharField(max_length=250, verbose_name='Rented films')),
                ('rating', models.IntegerField(default=5, help_text='value 1 to 10', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('datetime', models.DateField()),
            ],
        ),
    ]
