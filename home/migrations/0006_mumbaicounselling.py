# Generated by Django 4.2.10 on 2024-02-09 09:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_score_maharashtracounselling_pcmscore_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MumbaiCounselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(blank=True, max_length=40, null=True)),
                ('studentEmail', models.EmailField(blank=True, max_length=40, null=True)),
                ('studentPhone', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(6000000000, message='Invalid contact number'), django.core.validators.MaxValueValidator(9999999999, message='Invalid contact number')])),
                ('studentTelegram', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(6000000000, message='Invalid contact number'), django.core.validators.MaxValueValidator(9999999999, message='Invalid contact number')])),
                ('studentGender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=40, null=True)),
                ('studentpcmscore', models.PositiveIntegerField(blank=True, null=True)),
                ('studentjeescore', models.PositiveIntegerField(blank=True, null=True)),
                ('academy', models.CharField(blank=True, choices=[('wakade', "Wakade's Classes"), ('saraswati', 'Saraswati Coaching Classes'), ('nota', 'None Of The Above')], max_length=40, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
