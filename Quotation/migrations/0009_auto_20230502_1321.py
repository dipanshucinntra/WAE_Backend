# Generated by Django 3.2.13 on 2023-05-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0008_auto_20230426_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressextension',
            name='BillToRemark',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='addressextension',
            name='ShipToRemark',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentlines',
            name='FreeText',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentlines',
            name='ItemDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='Comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='OthInstruct',
            field=models.TextField(blank=True),
        ),
    ]