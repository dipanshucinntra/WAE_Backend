# Generated by Django 3.2.13 on 2023-09-01 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0007_remove_item_itemsgroupmastercode'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ItemsGroupMasterCode',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ItemsGroupMasterCode', to='Item.itemgroupmaster', to_field='Number'),
        ),
    ]
