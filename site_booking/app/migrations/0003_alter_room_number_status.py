# Generated by Django 5.1.4 on 2024-12-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_country_country_name_en_country_country_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number_status',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=10, null=True),
        ),
    ]