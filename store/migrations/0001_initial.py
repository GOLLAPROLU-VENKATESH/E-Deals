# Generated by Django 3.1.5 on 2021-01-18 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seller_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('mrp', models.IntegerField(default=0)),
                ('selling_price', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=500)),
                ('img_1', models.ImageField(upload_to='uploads/product/')),
                ('img_2', models.ImageField(upload_to='uploads/product/')),
                ('start_time', models.DateTimeField(blank=True)),
                ('End_time', models.DateTimeField(blank=True)),
                ('uploaded_time', models.DateTimeField()),
            ],
        ),
    ]