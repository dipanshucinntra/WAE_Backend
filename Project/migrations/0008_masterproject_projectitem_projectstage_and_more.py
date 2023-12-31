# Generated by Django 4.2.2 on 2023-09-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_rename_cardcode_project_cardcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact_person', models.CharField(blank=True, max_length=250)),
                ('start_date', models.CharField(blank=True, max_length=50)),
                ('target_date', models.CharField(blank=True, max_length=50)),
                ('details', models.CharField(blank=True, max_length=1000)),
                ('CardCode', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('project_owner', models.CharField(blank=True, max_length=250)),
                ('project_cost', models.CharField(blank=True, max_length=250)),
                ('project_status', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('CreatedDate', models.CharField(blank=True, max_length=50)),
                ('CreatedTime', models.CharField(blank=True, max_length=50)),
                ('UpdateDate', models.CharField(blank=True, max_length=50)),
                ('UpdateTime', models.CharField(blank=True, max_length=50)),
                ('DepName', models.CharField(blank=True, max_length=100)),
                ('CreatedBy', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LineNum', models.IntegerField(default=0)),
                ('ProjectId', models.CharField(blank=True, max_length=20)),
                ('Quantity', models.IntegerField(default=0)),
                ('UnitPrice', models.FloatField(default=0)),
                ('DiscountPercent', models.FloatField(default=0)),
                ('ItemDescription', models.CharField(blank=True, max_length=250)),
                ('CategoryName', models.CharField(blank=True, max_length=250)),
                ('ItemCode', models.CharField(blank=True, max_length=50)),
                ('TaxRate', models.CharField(blank=True, default=0, max_length=10)),
                ('TaxCode', models.CharField(blank=True, max_length=50)),
                ('U_FGITEM', models.CharField(blank=True, max_length=50)),
                ('CostingCode2', models.CharField(blank=True, max_length=50)),
                ('ProjectCode', models.CharField(blank=True, max_length=50)),
                ('FreeText', models.CharField(blank=True, max_length=500)),
                ('ItemSerialNo', models.CharField(blank=True, max_length=100)),
                ('Frequency', models.CharField(blank=True, max_length=20)),
                ('StartDate', models.CharField(blank=True, max_length=50)),
                ('EndDate', models.CharField(blank=True, max_length=50)),
                ('IsService', models.CharField(default='tNO', max_length=10)),
                ('ReferenceItem', models.CharField(blank=True, max_length=255)),
                ('ReferenceSerial', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectId', models.CharField(blank=True, max_length=50)),
                ('Name', models.CharField(max_length=150)),
                ('Stageno', models.FloatField(default=0)),
                ('PaymentPercentage', models.FloatField(default=0)),
                ('Status', models.IntegerField(default=0)),
                ('StageOwner', models.CharField(blank=True, max_length=5)),
                ('StageAssign', models.CharField(blank=True, max_length=5)),
                ('Comment', models.CharField(blank=True, max_length=500)),
                ('Data', models.TextField(blank=True)),
                ('File', models.CharField(blank=True, max_length=250)),
                ('DepName', models.CharField(blank=True, max_length=250)),
                ('CreateDate', models.CharField(blank=True, max_length=100)),
                ('CreateTime', models.CharField(blank=True, max_length=100)),
                ('UpdateDate', models.CharField(blank=True, max_length=100)),
                ('UpdateTime', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStaticstage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Stageno', models.FloatField(default=0)),
                ('PaymentPercentage', models.FloatField(default=0)),
                ('DepName', models.CharField(blank=True, default='New Product', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='CreatedBy',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='CurrentStageNo',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='DepName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='ItemCode',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='master_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
