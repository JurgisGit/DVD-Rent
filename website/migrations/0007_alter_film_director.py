# Generated by Django 4.1.1 on 2022-10-16 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_rentals_rented_films_rentals_rented_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.director'),
        ),
    ]
