# Generated by Django 3.2.13 on 2023-04-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0010_businesspartner_u_landline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpaddresses',
            name='Street',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
