# Generated by Django 3.2.2 on 2022-01-07 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0003_tbl_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_supplier',
            name='comapany',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='syspos.tbl_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_supplier',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
