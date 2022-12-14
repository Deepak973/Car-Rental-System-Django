# Generated by Django 3.2.5 on 2021-07-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField()),
                ('l_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_brand', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=100)),
                ('vehicle_name', models.CharField(max_length=100)),
                ('vehicle_image', models.URLField()),
                ('price_per_day', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=100)),
                ('seating_capacity', models.CharField(max_length=100)),
                ('aircondition', models.CharField(max_length=100)),
                ('airbag', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
