# Generated by Django 3.2.13 on 2023-03-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DraftOrder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addondocumentlines',
            name='ParentItemCode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
