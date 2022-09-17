# Generated by Django 3.2.5 on 2021-08-08 05:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='quantity',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='vehicle_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]