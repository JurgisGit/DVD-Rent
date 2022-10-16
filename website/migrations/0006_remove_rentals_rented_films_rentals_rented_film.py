# Generated by Django 4.1.1 on 2022-10-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rentals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentals',
            name='rented_films',
        ),
        migrations.AddField(
            model_name='rentals',
            name='rented_film',
            field=models.CharField(default='', max_length=250, verbose_name='Rented film'),
            preserve_default=False,
        ),
    ]
