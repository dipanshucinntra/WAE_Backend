# Generated by Django 3.2.13 on 2023-02-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0006_quotation_bpemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentlines',
            name='IT_Intall',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='documentlines',
            name='IT_LOCharges',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='documentlines',
            name='IT_MICharges',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
