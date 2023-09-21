# Generated by Django 4.2.2 on 2023-09-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0002_auto_20230220_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceDocEntry', models.CharField(blank=True, max_length=10)),
                ('DocEntry', models.CharField(blank=True, max_length=10)),
                ('CardCode', models.CharField(blank=True, max_length=50)),
                ('CardName', models.CharField(blank=True, max_length=50)),
                ('DocDate', models.CharField(blank=True, max_length=100)),
                ('DocTotal', models.CharField(blank=True, max_length=100)),
                ('SalesPersonCode', models.CharField(blank=True, max_length=100)),
                ('Comments', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='IncomingPaymentInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncomingPaymentsId', models.CharField(blank=True, max_length=10)),
                ('LineNum', models.CharField(blank=True, max_length=100)),
                ('InvoiceDocEntry', models.CharField(blank=True, max_length=100)),
                ('SumApplied', models.CharField(blank=True, max_length=100)),
                ('AppliedFC', models.CharField(blank=True, max_length=100)),
                ('AppliedSys', models.CharField(blank=True, max_length=100)),
                ('DiscountPercent', models.CharField(blank=True, max_length=100)),
                ('TotalDiscount', models.CharField(blank=True, max_length=100)),
                ('TotalDiscountFC', models.CharField(blank=True, max_length=100)),
                ('TotalDiscountSC', models.CharField(blank=True, max_length=100)),
                ('DocDate', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IncomingPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocNum', models.CharField(blank=True, max_length=100)),
                ('DocType', models.CharField(blank=True, max_length=100)),
                ('DocDate', models.CharField(blank=True, max_length=100)),
                ('CardCode', models.CharField(blank=True, max_length=100)),
                ('CardName', models.CharField(blank=True, max_length=100)),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('DocCurrency', models.CharField(blank=True, max_length=100)),
                ('CheckAccount', models.CharField(blank=True, max_length=100)),
                ('TransferAccount', models.CharField(blank=True, max_length=100)),
                ('TransferSum', models.CharField(blank=True, max_length=100)),
                ('TransferDate', models.CharField(blank=True, max_length=100)),
                ('TransferReference', models.CharField(blank=True, max_length=100)),
                ('Series', models.CharField(blank=True, max_length=100)),
                ('DocEntry', models.CharField(blank=True, max_length=100)),
                ('DueDate', models.CharField(blank=True, max_length=100)),
                ('BPLID', models.CharField(blank=True, max_length=100)),
                ('BPLName', models.CharField(blank=True, max_length=100)),
                ('Comments', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]