# Generated by Django 3.2.5 on 2021-08-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='diff_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='refund_price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
