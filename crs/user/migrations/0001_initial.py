# Generated by Django 3.2.5 on 2021-07-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('veh_id', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('from_destination', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=12)),
                ('lic_no', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
    ]
