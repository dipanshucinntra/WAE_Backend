# Generated by Django 3.2.13 on 2023-03-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Opportunity', '0007_auto_20230222_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='category',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='intProdCat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='intProjCat',
            field=models.TextField(blank=True),
        ),
    ]
