# Generated by Django 3.2.13 on 2023-04-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0030_auto_20230426_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Address',
            field=models.TextField(blank=True),
        ),
    ]
