# Generated by Django 3.2.13 on 2023-04-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0007_auto_20230221_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressextension',
            name='BillToStreet',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='addressextension',
            name='ShipToStreet',
            field=models.TextField(blank=True),
        ),
    ]