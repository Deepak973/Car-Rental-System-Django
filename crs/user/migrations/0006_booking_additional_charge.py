# Generated by Django 3.2.5 on 2021-08-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210809_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_charge',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
