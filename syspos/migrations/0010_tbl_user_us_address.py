# Generated by Django 3.2.2 on 2022-01-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0009_auto_20220110_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='us_address',
            field=models.TextField(null=True),
        ),
    ]
