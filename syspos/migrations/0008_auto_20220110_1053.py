# Generated by Django 3.2.2 on 2022-01-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0007_rename_comapany_tbl_supplier_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_branch',
            name='company',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tbl_branch',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]