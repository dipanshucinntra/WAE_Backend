# Generated by Django 4.2.2 on 2023-09-19 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0002_department_subdepartment_employee_countrycode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticDropDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DropDownName', models.CharField(blank=True, max_length=250)),
                ('DropDownValue', models.CharField(blank=True, max_length=250)),
                ('DropDownDescription', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DropDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DropDownName', models.CharField(blank=True, max_length=250)),
                ('DropDownValue', models.CharField(blank=True, max_length=250)),
                ('DropDownDescription', models.TextField(blank=True)),
                ('Data', models.TextField(blank=True)),
                ('Parent', models.CharField(blank=True, max_length=100)),
                ('Field1', models.CharField(blank=True, max_length=100)),
                ('Field2', models.CharField(blank=True, max_length=100)),
                ('Field3', models.CharField(blank=True, max_length=100)),
                ('Field4', models.CharField(blank=True, max_length=100)),
                ('Field5', models.CharField(blank=True, max_length=100)),
                ('CreateDate', models.CharField(blank=True, max_length=100)),
                ('CreateTime', models.CharField(blank=True, max_length=100)),
                ('UpdateDate', models.CharField(blank=True, max_length=100)),
                ('UpdateTime', models.CharField(blank=True, max_length=100)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CreatedBy', to='Employee.employee', to_field='SalesEmployeeCode')),
                ('UpdatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UpdatedBy', to='Employee.employee', to_field='SalesEmployeeCode')),
            ],
        ),
    ]
