# Generated by Django 3.2.13 on 2023-08-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0039_addondocumentlineshistory_documentlineshistory_orderhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentlines',
            name='customize',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
