# Generated by Django 4.2.10 on 2024-02-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_paymentrecords_transactionid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maharashtracounselling',
            old_name='score',
            new_name='pcmscore',
        ),
        migrations.AddField(
            model_name='maharashtracounselling',
            name='centralscore',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maharashtracounselling',
            name='pcbscore',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
