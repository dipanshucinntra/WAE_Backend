# Generated by Django 3.2.13 on 2023-03-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DraftOrder', '0003_auto_20230307_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftorder',
            name='arch_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='arch_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='arch_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='cli_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='cli_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='cli_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='contr_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='contr_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='contr_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='fcm_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='fcm_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='fcm_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='kit_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='kit_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='kit_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='mep_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='mep_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='mep_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='oth_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='oth_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='oth_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='pm_consultant_code',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='pm_consultant_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='draftorder',
            name='pm_contact_person',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]