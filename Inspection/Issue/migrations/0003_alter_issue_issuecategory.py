# Generated by Django 3.2.13 on 2023-06-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0002_alter_issue_issuecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='IssueCategory',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
