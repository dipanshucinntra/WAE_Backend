# Generated by Django 3.2.7 on 2022-09-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BPLId', models.CharField(max_length=5)),
                ('BPLName', models.CharField(blank=True, max_length=250)),
                ('Address', models.CharField(blank=True, max_length=250)),
                ('MainBPL', models.CharField(blank=True, max_length=5)),
                ('Disabled', models.CharField(blank=True, max_length=5)),
                ('UserSign2', models.CharField(blank=True, max_length=5)),
                ('UpdateDate', models.CharField(blank=True, max_length=50)),
                ('DflWhs', models.CharField(blank=True, max_length=50)),
                ('TaxIdNum', models.CharField(blank=True, max_length=100)),
                ('StreetNo', models.CharField(blank=True, max_length=100)),
                ('Building', models.CharField(blank=True, max_length=100)),
                ('ZipCode', models.CharField(blank=True, max_length=100)),
                ('City', models.CharField(blank=True, max_length=100)),
                ('State', models.CharField(blank=True, max_length=100)),
                ('Country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=35)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('natureOfIndustry', models.CharField(blank=True, max_length=100)),
                ('ERP', models.CharField(blank=True, max_length=100)),
                ('serverIP', models.CharField(blank=True, max_length=100)),
                ('port', models.IntegerField(default=0)),
                ('user', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('license_limit', models.IntegerField(default=1)),
                ('active', models.IntegerField(default=1)),
                ('timestamp', models.CharField(max_length=30)),
            ],
        ),
    ]
