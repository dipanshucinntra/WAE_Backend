# Generated by Django 3.2.13 on 2022-10-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='UomNo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]