# Generated by Django 3.2.13 on 2023-06-09 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0037_orderstatusremarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderStatusRemarks',
        ),
    ]