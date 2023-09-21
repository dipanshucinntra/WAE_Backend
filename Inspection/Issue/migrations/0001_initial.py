# Generated by Django 4.1.4 on 2023-06-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=250)),
                ('IssueCategory', models.CharField(blank=True, max_length=250)),
                ('CreatedBy', models.CharField(blank=True, max_length=150)),
                ('CreatedDate', models.CharField(blank=True, max_length=50)),
                ('CreatedTime', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]