# Generated by Django 3.2.5 on 2021-08-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_booking_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='to_date',
            field=models.DateTimeField(),
        ),
    ]