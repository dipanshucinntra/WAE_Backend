# Generated by Django 3.2.7 on 2022-09-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorrigendumList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('Type', models.CharField(blank=True, max_length=200)),
                ('Title', models.CharField(blank=True, max_length=200)),
                ('File', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CoverDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('CoverTitle', models.CharField(blank=True, default='', max_length=100)),
                ('CoverDocType', models.CharField(blank=True, default='', max_length=100)),
                ('CoverDesc', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CritcalDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('PublishDate', models.CharField(blank=True, max_length=200)),
                ('BidOpeningDate', models.CharField(blank=True, max_length=200)),
                ('SaleStartDate', models.CharField(blank=True, default='', max_length=200)),
                ('SaleEndDate', models.CharField(blank=True, default='', max_length=200)),
                ('ClarificationStartDate', models.CharField(blank=True, default='', max_length=200)),
                ('ClarificationEndDate', models.CharField(blank=True, default='', max_length=200)),
                ('BidSubStartDate', models.CharField(blank=True, default='', max_length=200)),
                ('BidSubEndDate', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('Type', models.CharField(blank=True, max_length=200)),
                ('Title', models.CharField(blank=True, max_length=200)),
                ('Description', models.CharField(blank=True, default='', max_length=200)),
                ('File', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LowestOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('CompanyName', models.CharField(blank=True, max_length=200)),
                ('QuotedModel', models.CharField(blank=True, max_length=100)),
                ('Price', models.IntegerField(blank=True, default=0)),
                ('Remarks', models.CharField(blank=True, max_length=100)),
                ('Status', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('PaymentType', models.CharField(blank=True, default='', max_length=50)),
                ('InstrumentType', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('CompanyName', models.CharField(blank=True, max_length=200)),
                ('QuotedModel', models.CharField(blank=True, max_length=100)),
                ('Part', models.CharField(blank=True, max_length=100)),
                ('Status', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalesPersonCode', models.CharField(blank=True, max_length=5)),
                ('OrganisationChain', models.CharField(blank=True, max_length=200)),
                ('TReferenceNo', models.CharField(blank=True, max_length=100)),
                ('TID', models.CharField(blank=True, max_length=100)),
                ('TType', models.CharField(blank=True, max_length=100)),
                ('TCategoey', models.CharField(blank=True, default='', max_length=100)),
                ('GeneralTechEveAll', models.CharField(blank=True, default='', max_length=50)),
                ('PaymentMode', models.CharField(blank=True, default='', max_length=50)),
                ('MultiCurrency', models.CharField(blank=True, default='', max_length=50)),
                ('FormOfContact', models.CharField(blank=True, default='', max_length=50)),
                ('NoOfCovers', models.CharField(blank=True, default='', max_length=50)),
                ('ItemTechEveAll', models.CharField(blank=True, default='', max_length=50)),
                ('MultiCurrencyForBoq', models.CharField(blank=True, default='', max_length=50)),
                ('TwoStageBidding', models.CharField(blank=True, default='', max_length=50)),
                ('TenderFee', models.CharField(blank=True, default='', max_length=100)),
                ('PayableTo', models.CharField(blank=True, default='', max_length=100)),
                ('FeeExemptionAllow', models.CharField(blank=True, default='', max_length=50)),
                ('FeePayableAt', models.CharField(blank=True, default='', max_length=100)),
                ('EMDAmount', models.CharField(blank=True, default='', max_length=100)),
                ('EMDFeeType', models.CharField(blank=True, default='', max_length=50)),
                ('EMDPayableTo', models.CharField(blank=True, default='', max_length=50)),
                ('EMDPayableAt', models.CharField(blank=True, default='', max_length=50)),
                ('EMDExemptionAllow', models.CharField(blank=True, default='', max_length=50)),
                ('EMDPercentage', models.CharField(blank=True, default='', max_length=50)),
                ('InvitingAuthorityName', models.CharField(blank=True, default='', max_length=100)),
                ('InvitingAuthorityAddress', models.CharField(blank=True, default='', max_length=200)),
                ('Status', models.CharField(blank=True, default='', max_length=50)),
                ('Comments', models.CharField(blank=True, default='', max_length=200)),
                ('TenderSubStatus', models.IntegerField(default=0)),
                ('TenderOpenStatus', models.IntegerField(default=0)),
                ('TechOpenStatus', models.IntegerField(default=0)),
                ('LowestOneStatus', models.IntegerField(default=0)),
                ('U_LEADID', models.IntegerField(default=0)),
                ('U_LEADNM', models.CharField(blank=True, max_length=150)),
                ('U_OPPID', models.CharField(blank=True, max_length=5)),
                ('U_OPPRNM', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TenderOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('CompanyName', models.CharField(blank=True, max_length=200)),
                ('QuotedModel', models.CharField(blank=True, max_length=100)),
                ('Part', models.CharField(blank=True, max_length=100)),
                ('Status', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TenderSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('FeeStatus', models.CharField(blank=True, max_length=100)),
                ('PaymentRegNo', models.CharField(blank=True, max_length=100)),
                ('PaymentMode', models.CharField(blank=True, max_length=100)),
                ('FeeAmount', models.CharField(blank=True, max_length=100)),
                ('BankName', models.CharField(blank=True, max_length=100)),
                ('AccountNo', models.CharField(blank=True, max_length=100)),
                ('IFSCCode', models.CharField(blank=True, max_length=100)),
                ('EMDFeeStatus', models.CharField(blank=True, max_length=100)),
                ('EMDTerms', models.CharField(blank=True, max_length=100)),
                ('EMDPaymentMode', models.CharField(blank=True, max_length=100)),
                ('EMDFeeAmount', models.CharField(blank=True, max_length=100)),
                ('EMDBankName', models.CharField(blank=True, max_length=100)),
                ('EMDAccountNo', models.CharField(blank=True, max_length=100)),
                ('EMDIFSCCode', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LineNum', models.IntegerField(default=0)),
                ('TenID', models.CharField(blank=True, max_length=5)),
                ('Quantity', models.IntegerField(default=0)),
                ('UnitPrice', models.FloatField(default=0)),
                ('DiscountPercent', models.FloatField(default=0)),
                ('ItemCode', models.CharField(blank=True, max_length=20)),
                ('ItemDescription', models.CharField(blank=True, max_length=150)),
                ('TaxCode', models.CharField(blank=True, max_length=10)),
                ('U_FGITEM', models.CharField(blank=True, max_length=20)),
                ('CostingCode2', models.CharField(blank=True, max_length=20)),
                ('ProjectCode', models.CharField(blank=True, max_length=20)),
                ('FreeText', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenderId', models.IntegerField(default=0)),
                ('Title', models.CharField(blank=True, max_length=200)),
                ('Description', models.TextField(blank=True)),
                ('PreQualficationDetails', models.CharField(blank=True, default='', max_length=200)),
                ('Remarks', models.CharField(blank=True, default='', max_length=200)),
                ('TenderValue', models.CharField(blank=True, default='', max_length=200)),
                ('ProductCategory', models.CharField(blank=True, default='', max_length=200)),
                ('ProductSubCategory', models.CharField(blank=True, default='', max_length=200)),
                ('ContactType', models.CharField(blank=True, default='', max_length=200)),
                ('BidValidity', models.CharField(blank=True, default='', max_length=200)),
                ('PeriodOfWork', models.CharField(blank=True, default='', max_length=200)),
                ('Location', models.CharField(blank=True, default='', max_length=200)),
                ('Pincode', models.CharField(blank=True, default='', max_length=200)),
                ('PreBidMeetingPlace', models.CharField(blank=True, default='', max_length=200)),
                ('PreBidMeetingAddress', models.CharField(blank=True, default='', max_length=200)),
                ('PreBidMeetingDate', models.CharField(blank=True, default='', max_length=200)),
                ('BidOpeningPlace', models.CharField(blank=True, default='', max_length=200)),
                ('NDATenderAllow', models.CharField(blank=True, default='', max_length=200)),
                ('PreferentialBidderAllow', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
    ]
