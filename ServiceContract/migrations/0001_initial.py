# Generated by Django 4.2.2 on 2023-09-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterServiceContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.CharField(blank=True, max_length=25)),
                ('MNo', models.CharField(blank=True, max_length=100)),
                ('ProjectID', models.CharField(blank=True, max_length=50)),
                ('ServiceContractID', models.CharField(blank=True, max_length=100)),
                ('ServiceContractType', models.CharField(blank=True, max_length=50)),
                ('ContractPersoneName', models.CharField(blank=True, max_length=250)),
                ('ContractPersoneNumber', models.CharField(blank=True, max_length=25)),
                ('LineManagerCode', models.IntegerField(default=0)),
                ('LineManagerName', models.CharField(blank=True, max_length=150)),
                ('TotalCost', models.FloatField(default=0)),
                ('PaymentTerm', models.TextField(blank=True, max_length=250)),
                ('CountryCode', models.CharField(blank=True, max_length=25)),
                ('Frequency', models.CharField(blank=True, max_length=50)),
                ('FromDate', models.CharField(blank=True, max_length=50)),
                ('ToDate', models.CharField(blank=True, max_length=50)),
                ('CardCode', models.CharField(blank=True, max_length=50)),
                ('BPName', models.CharField(blank=True, max_length=50)),
                ('Remarks', models.CharField(blank=True, max_length=50)),
                ('ContractType', models.CharField(blank=True, max_length=50)),
                ('Status', models.IntegerField(blank=True, default=0)),
                ('CreatedBy', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_id', models.CharField(blank=True, max_length=100)),
                ('OrderID', models.CharField(blank=True, max_length=100)),
                ('ProjectID', models.CharField(blank=True, max_length=100)),
                ('MNo', models.CharField(blank=True, max_length=100)),
                ('ProductSerialNo', models.CharField(blank=True, max_length=250)),
                ('ProductCate', models.CharField(blank=True, max_length=250)),
                ('ProductSubCate', models.CharField(blank=True, max_length=250)),
                ('ServiceContractID', models.CharField(blank=True, max_length=100)),
                ('ServiceContractType', models.CharField(blank=True, max_length=100)),
                ('ContractPersoneName', models.CharField(blank=True, max_length=150)),
                ('ContractPersoneNumber', models.CharField(blank=True, max_length=50)),
                ('LineManagerCode', models.IntegerField(default=0)),
                ('LineManagerName', models.CharField(blank=True, max_length=150)),
                ('CountryCode', models.CharField(blank=True, max_length=50)),
                ('Frequency', models.CharField(blank=True, max_length=50)),
                ('FromDate', models.CharField(blank=True, max_length=50)),
                ('ToDate', models.CharField(blank=True, max_length=50)),
                ('CheckList', models.CharField(blank=True, max_length=250)),
                ('CardCode', models.CharField(blank=True, max_length=100)),
                ('BPName', models.CharField(blank=True, max_length=250)),
                ('Remarks', models.TextField(blank=True)),
                ('ServiceContractOwner', models.IntegerField(default=0)),
                ('ServiceContractOwnerName', models.CharField(blank=True, max_length=150)),
                ('SiteEngineerAssigned', models.IntegerField(default=0)),
                ('SiteEngineerAssignedName', models.CharField(blank=True, max_length=150)),
                ('ContractType', models.CharField(blank=True, max_length=100)),
                ('Status', models.IntegerField(default=0)),
                ('ServiceContractsItem', models.TextField(blank=True)),
                ('ServiceItem', models.TextField(blank=True)),
            ],
        ),
    ]