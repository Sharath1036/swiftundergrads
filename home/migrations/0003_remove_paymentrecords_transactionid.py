# Generated by Django 4.2.10 on 2024-02-09 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_transactionid_paymentrecords_transactionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentrecords',
            name='transactionid',
        ),
    ]
