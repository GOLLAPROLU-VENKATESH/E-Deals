# Generated by Django 3.1.5 on 2021-05-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0005_auto_20210511_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techblog',
            name='heading',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='techblog',
            name='para1',
            field=models.TextField(max_length=200),
        ),
    ]
