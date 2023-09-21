# Generated by Django 4.2.2 on 2023-09-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0015_auto_20230503_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='BPUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BPID', models.IntegerField(default=0)),
                ('CardCode', models.CharField(blank=True, max_length=50, unique=True)),
                ('EmployeeCode', models.CharField(blank=True, max_length=50)),
                ('EmployeeName', models.CharField(blank=True, max_length=50)),
                ('EmployeeID', models.CharField(blank=True, max_length=30)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(blank=True, max_length=50)),
                ('LastName', models.CharField(blank=True, max_length=50)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('Mobile', models.CharField(blank=True, max_length=15)),
                ('CountryCode', models.CharField(blank=True, max_length=15)),
                ('Role', models.CharField(blank=True, max_length=50)),
                ('Position', models.CharField(blank=True, max_length=50)),
                ('Branch', models.CharField(blank=True, max_length=20)),
                ('Active', models.CharField(blank=True, max_length=20)),
                ('PasswordUpdatedOn', models.CharField(blank=True, max_length=30)),
                ('LastLoginOn', models.CharField(blank=True, max_length=30)),
                ('LogedIn', models.CharField(blank=True, max_length=20)),
                ('FCM', models.CharField(blank=True, max_length=250)),
                ('CreateDate', models.CharField(blank=True, max_length=30)),
                ('CreateTime', models.CharField(blank=True, max_length=30)),
                ('UpdateDate', models.CharField(blank=True, max_length=30)),
                ('UpdateTime', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyPointsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardCode', models.CharField(blank=True, max_length=30)),
                ('SourceId', models.CharField(blank=True, max_length=30)),
                ('CreditPoints', models.CharField(blank=True, max_length=250)),
                ('Remarks', models.CharField(blank=True, max_length=250)),
                ('Datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='bpbranch',
            name='CountryCode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bpemployee',
            name='CountryCode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='CountryCode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='LoyaltyPoints',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='U_EMIRATESID',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='U_SOURCE',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='U_VATNUMBER',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
